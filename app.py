from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=[{
        'description': 'List Item 1'
    },{
        'description': 'List Item 2'
    },{
        'description': 'List Item 3'
    }])