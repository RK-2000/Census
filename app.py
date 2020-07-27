from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/sign-in')
def signin():
    return render_template('sign_in.html')

if __name__ == '__main__':
    app.run(debug=True)
