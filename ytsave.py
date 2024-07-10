from flask import Flask
from app import app, routes
import os

app = Flask(__name__)


if __name__ == '__main__':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port = port)
