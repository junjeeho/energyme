from flask import Flask, render_template

# 从Flask对象创建一个app对象, Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
# $ export FLASK_ENV=development
# $ export FLASK_APP=app.py
# $ flask run

# new folder 'templates'

@app.route('/')
def index():
    stuff = ['Tsitsipas', 'Theodore', 'Yvoline']
    return render_template('index.html',
        stuff=stuff,
    )

@app.route('/user/<name>')
def about(name):
    return render_template('user.html', user_name=name)

@app.route('/login')
def login():
    return render_template('login.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()