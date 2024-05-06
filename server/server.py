from flask import Flask, request
import fretboard_logic
import random

app = Flask(__name__)
data1 = ""
random_note = random.choice(random.choice(fretboard_logic.fretboard))

@app.route('/selectednote', methods=['POST', 'GET'])
def receive_data():
    data = request.data.decode()
    print(data)
    global data1
    data1 = data
    return "Data Received!"

@app.route('/correctnote')
def received():
    global random_note
    print("random note: ",random_note)
    if data1 == random_note:
        random_note = random.choice(random.choice(fretboard_logic.fretboard))
        return {"bool" : "True"}
    else:
        return {"bool" : "False"}


if __name__ == "__main__":
    app.run(debug=True)