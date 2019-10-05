"""Simple Flask Application."""
"""
1. Install Flask using: pip install Flask
2. Execute the following commands to run the file "flask_app.py"
  export FLASK_APP=flask_app
  export FLASK_ENV=development
  flask run
3. Browse to: http://127.0.0.1:5000/hello
"""


from flask import Flask

app = Flask(__name__)

@app.route('/')
def start():
  return 'Got to server'

@app.route('/hello')
def hello():
  return 'Hello, World!'

@app.route('/goodbye')
def goodbye():
  return 'Goodbye, World!'
