from flask import Flask
from flask import jsonify, request
from main import *
from bson.json_util import dumps
import json
import socket

app = Flask(__name__)
conn = connect()
db = get_db(conn)

@app.route("/post", methods=['POST'])
def post():
    form = request.form
    print(form)
    data = form['data']
    id = post_document(data, db)
    return jsonify(post_id=json.loads(dumps(id)))

@app.route("/get", methods=['GET'])
def get():
    documents = get_documents(db)
    res = json.loads(dumps(list(documents)))
    res['hostname'] = socket.gethostname()
    return jsonify(posts=res)

if __name__ == "__main__":
    app.run()
