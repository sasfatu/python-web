from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def details():
    details = "hello world"
    return jsonify(details)
    
if __name__ == '__main__':
    app.run()