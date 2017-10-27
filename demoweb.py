from flask import Flask, request,render_template,session


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500

@app.route('/', methods=['GET', 'POST'])

def home():
    return render_template('home.html',message="呵呵",count=100)

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    session["uid"]="1245678"
    uu=session.get("uid")
    print(uu)
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=uu)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()