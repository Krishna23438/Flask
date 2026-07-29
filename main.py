from flask import Flask,  render_template, url_for

app = Flask(__name__)

# URL => endpoint /
@app.route("/")
def hello_world():
  # static file  => dynamically generate the url
  print(url_for("static",filename="static.css"))
  return render_template("index.html")

@app.route("/login")
def prime():
  return render_template("login.html")


if __name__ == "__main__":
  app.run(debug=True)