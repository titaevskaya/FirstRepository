from flask import Flask, render_template

app = Flask(__name__)


@app.route('/about/')
def about():
    return render_template('base.html')


@app.route('/about1/')
def about1():
    return render_template('my.html')


@app.route('/about2/')
def about2():
    return render_template('my_2.html')


app.run()
