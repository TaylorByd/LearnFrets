from flask import Flask, request
import fretboard_logic
import fretboard_img_note_selected
import random

app = Flask(__name__)
detectedNote = ""
random_note = random.choice(random.choice(fretboard_logic.fretboard))

@app.route('/selectednote', methods=['POST', 'GET'])
def getSelectedNote():
    global detectedNote
    selectedNote = request.data.decode()
    detectedNote = selectedNote
    print("Selected Note: ", selectedNote)
    print(request.remote_addr)
    return "Data Received!"

@app.route('/correctnote')
def compareRandomNote():
    global random_note
    global detectedNote
    random_col = random.randint(0,24)
    random_row = random.randint(0,5)
    print("Random Note: ", random_note)
    if detectedNote == random_note:
        random_note = fretboard_logic.fretboard[random_row][random_col]
        fretboard_img_note_selected.place_dot_img(fretboard_img_note_selected.dot_coordinates[random_row][random_col])
        detectedNote = '0'
            # used in the case that we get two repeated random notes in a row and we do not want that repeated note to be skipped.
        return {"bool" : "True"}
    else:
        return {"bool" : "False"}

if __name__ == "__main__":
    app.run(debug=True)