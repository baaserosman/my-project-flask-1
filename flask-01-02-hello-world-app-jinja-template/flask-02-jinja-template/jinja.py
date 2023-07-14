from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def head():
    return render_template('index.html', number1=2546, number2=7876)


@app.route('/mult')

def number():
    x=54
    y=58
    return render_template('body.html', num1=x, num2=y, mult=x*y)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host= '0.0.0.0', port=80)
