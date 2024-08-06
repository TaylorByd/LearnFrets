from flask import Flask, request, session, redirect, url_for
import fretboard_logic
import fretboard_img_note_selected
import random

app = Flask(__name__)
app.secret_key = 'add secret key later'

@app.route('/initialize')
def initialize():
    runFlag = session.get('runFlag')
    if runFlag is None:
        print("flag run")
        random_col = random.randint(0, 24)
        random_row = random.randint(0, 5)
        session['randomNote'] = fretboard_logic.fretboard[random_row][random_col]
        fretboard_img_note_selected.place_dot_img(fretboard_img_note_selected.dot_coordinates[random_row][random_col])
    session['runFlag'] = True
    return 'This function can only run once.'

@app.route('/selectednote', methods=['POST', 'GET'])
def getSelectedNote():
    selectedNote = request.data.decode()
    session['detectedNote'] = selectedNote
    detectedNote = session.get('detectedNote', '')  # Retrieve detectedNote from session
    randomNote = session.get('randomNote', '')  # Retrieve randomNote from session
    print("Selected Note: ", selectedNote)
    if detectedNote == randomNote:
        return {"bool": "True"} and redirect(url_for('compareRandomNote'))
    else:
        return {"bool": "False"} and redirect(url_for('compareRandomNote'))

@app.route('/correctnote')
def compareRandomNote():
    random_col = random.randint(0, 24)
    random_row = random.randint(0, 5)
    detectedNote = session.get('detectedNote', '')  # Retrieve detectedNote from session
    randomNote = session.get('randomNote', '')  # Retrieve randomNote from session
    print("Random Note: ", randomNote)
    if detectedNote == randomNote:
        session['randomNote'] = fretboard_logic.fretboard[random_row][random_col]
        fretboard_img_note_selected.place_dot_img(fretboard_img_note_selected.dot_coordinates[random_row][random_col])
        print("New Random Note:", session['randomNote'])
        session['detectedNote'] = '0'  # Update detectedNote in session
        return {"bool": "True"}
    else:
        return {"bool": "False"}

if __name__ == "__main__":
    app.run(debug=True)