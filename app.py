from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/project/templates/next.html')
def next_page():
    return render_template('next.html')

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
