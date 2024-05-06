from flask import Flask, request

app = Flask(__name__)
data1 = ""

@app.route('/data', methods=['POST', 'GET'])
def receive_data():
    data = request.data.decode()
    print(data)
    global data1
    data1 = data
    return "Data Received!"

@app.route('/correctnote')
def received():
    if data1 == 'C#':
        return {"bool" : "True"}
    else:
        return {"bool" : "False"}


if __name__ == "__main__":
    app.run(debug=True)