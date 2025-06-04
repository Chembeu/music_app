from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)  
@app.route('/')
def index():
    return'<h1>hello world</h1>'
@app.route('/user')
def user():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)