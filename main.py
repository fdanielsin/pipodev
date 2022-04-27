from flask import Flask, render_template

app = Flask(__name__)

# Base PAGE
@app.route("/")
def hello_world():
    return 'Hello World'

# Home PAGE
@app.route('/home')
def about():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1000, debug=True)
