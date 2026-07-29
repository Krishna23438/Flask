from flask import Flask

app = Flask(__name__)

# URL => endpoint /
@app.route("/")
def hello_worl():
  return "<p>Hello, World!</p>"

app.run(debug=True)