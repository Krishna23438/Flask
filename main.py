from flask import Flask,  render_template ,url_for, request

app = Flask(__name__)

# URL => endpoint /
@app.route("/")
def hello_world():
  # static file  => dynamically generate the url
  print(url_for("static",filename="static.css"))
  return render_template("index.html")

@app.route("/login",methods = ["GET","POST"])
def prime():
  if request.method == "POST":
      print(request.form) #ImmutableMultiDict([('username', 'Krishna Gupta'), ('password', '123')])
      name = request.form["username"]
      password = request.form["password"]
  
      return f"<h1>Welcome {name}! </h1>"
  else:
    return render_template("login.html")




  return "<p> this route is to handle login</p>"


if __name__ == "__main__":
  app.run(debug=True)