from flask import Flask
from chatbot import chatbot
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins=["http://192.168.38.158:3000"])

app.register_blueprint(chatbot, url_prefix='/chatbot')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
