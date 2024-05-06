from flask import Flask, request
import fretboard_logic
import random

app = Flask(__name__)
detectedNote = ""
random_note = random.choice(random.choice(fretboard_logic.fretboard))

@app.route('/selectednote', methods=['POST', 'GET'])
def receive_data():
    selectedNote = request.data.decode()
    print("Selected Note: ", selectedNote)
    global detectedNote
    detectedNote = selectedNote
    return "Data Received!"

@app.route('/correctnote')
def received():
    global random_note
    print("Random Note: ", random_note)
    if detectedNote == random_note:
        random_note = random.choice(random.choice(fretboard_logic.fretboard))
        return {"bool" : "True"}
    else:
        return {"bool" : "False"}


if __name__ == "__main__":
    app.run(debug=True)