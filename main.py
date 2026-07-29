from flask import Flask,  render_template

app = Flask(__name__)

# URL => endpoint /
@app.route("/")
def hello_world():
  return render_template("index.html")

@app.route("/prime")
def prime():
  return "<p>Hello, Prime World!</p>"


if __name__ == "__main__":
  app.run(debug=True)