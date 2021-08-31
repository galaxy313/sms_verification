from flask import Flask,jsonify,request
app=Flask(__name__)


@app.route('/v1/process',methods=['POST'])
def process():
    data=request.form
    sender=data["from"]
    message=data["message"]
    print (f'recieve {message} from {sender}')
    ret={"message":"processed"}
    return jsonify(ret),200
def send_sms():
    pass
def check_serial():
    pass
if __name__ == "__main__":
    app.run("0.0.0.0",5000,debug=True)
