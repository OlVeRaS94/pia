from flask import flash, Flask, jsonify, request

app=Flask(__name__)

port=8090

@app.route("/saluda",methods=["POST"])
def saluda():
    body=request.get_json();
    resp="Hola <b>" + body["name"]+"</b>"
    ret={
        "resposta":resp
    }

    return jsonify(ret),201

@app.post("/suma")
def suma():
    body=request.get_json()
    if not all(param in body for param in ("x","y")):
        return "Error de format al body", 400
    x=body["x"]
    y=body["y"]
    suma=x+y
    ret={
        "suma":suma
    }

    return jsonify(ret),200

@app.route('/cliente')
def get_cliente():
    username = request.args.get('username')
    password = request.args.get('password')

    return f'He demanat el client {username} & {password}'


# /cliente/12
@app.route('/cliente/<id_Cliente>')
def get_cliente_by_Id(id_Cliente):
    return f'He demanat el client {id_Cliente}'



if __name__=="__main__":
    app.run(port=port)
