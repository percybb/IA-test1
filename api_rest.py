from flask import Flask, request
import pickle
import numpy as np


app = Flask(__name__)


@app.route("/eda", methods=(['POST']))
def mod():
    print("Hola")
    request_data = request.get_json(force=True)
    option = request_data['nom']
    age = request_data['prenom']
    print(option)
    print(age)
    return "todo bien"


if __name__ == '__main__':
    app.run(port=8008, debug=True)
