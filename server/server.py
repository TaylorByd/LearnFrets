from flask import Flask, request, session, redirect, url_for
import fretboard_logic
import fretboard_img_note_selected
import random
import threading

app = Flask(__name__)
app.secret_key = 'add secret key later'

@app.route('/initialize')
def initialize():
    runFlag = session.get('runFlag')
    if runFlag is None:
        print("flag run")
        session['random_col'] = random.randint(0, 24)
        session['random_row'] = random.randint(0, 5)
        random_col = session.get('random_col', '')  # Retrieve random_row from session
        random_row = session.get('random_row', '')  # Retrieve random_col from session
        session['randomNote'] = fretboard_logic.fretboard[random_row][random_col]
        fretboard_img_note_selected.create_dot(255, 0, 255, fretboard_img_note_selected.dot_coordinates[random_row][random_col])
    session['runFlag'] = True
    return 'This function can only run once.'

@app.route('/selectednote', methods=['POST', 'GET'])
def getSelectedNote():
    selectedNote = request.data.decode()
    session['detectedNote'] = selectedNote
    print("Selected Note: ", selectedNote)
    return redirect(url_for('compareRandomNote'))

@app.route('/comparenote')
def compareRandomNote():
    detectedNote = session.get('detectedNote', '')  # Retrieve detectedNote from session
    randomNote = session.get('randomNote', '')      # Retrieve randomNote from session
    print("Random Note: ", randomNote)
    if detectedNote == randomNote:
        session['random_col'] = random.randint(0, 24)
        session['random_row'] = random.randint(0, 5)
        random_col = session.get('random_col', '')      # Retrieve random_row from session
        random_row = session.get('random_row', '')      # Retrieve random_col from session
        session['randomNote'] = fretboard_logic.fretboard[random_row][random_col]
        fretboard_img_note_selected.create_dot(255, 0, 255, fretboard_img_note_selected.dot_coordinates[random_row][random_col])
        print("New Random Note:", session['randomNote'])
        session['detectedNote'] = '0'  # Prevents the same repeating note from being skipped
        return {"bool": "True"}
    else:
        return {"bool": "False"}

@app.route('/correctnote')
async def greenDot():
    random_col = session.get('random_col', '')
    random_row = session.get('random_row', '')
    thread = threading.Thread(target=fretboard_img_note_selected.correct_note, args=(fretboard_img_note_selected.dot_coordinates[random_row][random_col],))
    thread.start()
    return "Green"

@app.route('/incorrectnote')
async def redDot():
    random_col = session.get('random_col', '')
    random_row = session.get('random_row', '')
    thread = threading.Thread(target=fretboard_img_note_selected.incorrect_note, args=(fretboard_img_note_selected.dot_coordinates[random_row][random_col],))
    thread.start()
    return "Red"

if __name__ == "__main__":
    app.run(debug=True)