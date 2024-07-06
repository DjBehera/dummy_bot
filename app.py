"""
Basic function to handle the python flask app
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """
    Handles the base web traffic
    """
    return "Hello, World! Updated from Dj"

if __name__ == '__main__':
    app.run(debug=True,port=3000)
