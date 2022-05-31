from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route("/")
def hello_World():
    return "hello world"

contacts=[
    {
        "contact":999999222,
        "name":"Raju",
        "done":False,
        "id":1
    },
    {
        "contact":999254222,
        "name":"Rahul",
        "done":False,
        "id":2
    }

    ]

@app.route("/add-data",methods=["POST"])
def data_loading():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data!"
        }),400
    contact={
        'id':contacts[-1][id]+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',""),
        'done':False
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })


@app.route("/get-data")
def get_data():
    return jsonify({"data":contacts})

if __name__=="__main__":
    app.run(debug=True)

    