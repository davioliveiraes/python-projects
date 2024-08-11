from fakepinterest import app

@app.route("/")
def homepage():
   return "Welcome FakePinterest"
