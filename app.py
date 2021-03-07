from flask import Flask, jsonify, render_template, redirect, request, session

app = Flask(__name__)

@app.route("/")
def home():
    print("Responding to the index page request...")
    return render_template("index.html")

@app.route("/projects")
def project():
    print("Responding to the project page request...")

if __name__ == "__main__":
    app.run(debug=True)
    
