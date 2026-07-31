from flask import Flask,  render_template ,url_for, request,jsonify

app = Flask(__name__)

# URL => endpoint /
#@app.route("/")
# def hello_world():
#   username = request.args.get("name",default="anonymous")
#   subject = request.args.get("subject",default="get Admission")
#   # static file  => dynamically generate the url
#   #print(url_for("static",filename="static.css"))
#   return render_template("index.html",name = username,sub=subject)

# @app.route("/")
# def hello_world():
#    data = {
#       "message":"Welcome to the platform"
#    }

#    return jsonify(data),501

@app.route("/")
def hello_world():
  return render_template("index.hmtl")
# @app.route("/login",methods = ["GET","POST"])
# def login():
#   if request.method == "POST":
#       #print(request.form) #ImmutableMultiDict([('username', 'Krishna Gupta'), ('password', '123')])
#       name = request.form["username"]
#       password = request.form["password"]

#       freinds = ["Bob", "Adam", "Charlie","Sam"]

#       header = "<header>ABC Website</header>"
#       return render_template("welcome.html",name = name, password = password, freinds = freinds, header = header)
      
#   else:
#     return render_template("login.html")

#   #return "<p> this route is to handle login</p>"


if __name__ == "__main__":
  app.run(debug=True)