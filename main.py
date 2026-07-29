from flask import Flask

app = Flask(__name__)

# URL => endpoint /
@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

@app.route("/prime")
def prime():
  return "<p>Hello, Prime World!</p>"


if __name__ == "__main__":
  app.run(debug=True)