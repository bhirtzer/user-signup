from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/", methods['POST'])
def username():
    username = request.form['username']

    
@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template("index.html")

app.run()