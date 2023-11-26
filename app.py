from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def test():
    return "<h1>I am HTML</h1>"

@app.route("/home")
def test2():
    return render_template("home.html")


if __name__=='__main__':
    app.run()

    