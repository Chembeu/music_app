from flask import Flask
app= Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'
app.run('/about/<username>')
def about(username):
    return f'<h1>About {username}</h1>'