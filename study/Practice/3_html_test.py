from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('html_test.html')

if __name__ == '__main__':
    app.run(debug = True, port = 8080, host = '0.0.0.0')