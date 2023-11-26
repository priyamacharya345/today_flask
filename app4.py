from flask import Flask, render_template
app=Flask(__name__)

@app.route('/greet/<name>/<int:phone>')
def hello(name,phone):
    return render_template('user.html',name=name,phone=phone)

if __name__=='__main__':
    app.run()

    