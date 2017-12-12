from flask import Flask,render_template,request, session, redirect, url_for
from .forms import SignupForm, LoginForm
from .models import db, User
from . import app

db.init_app(app)
#connecting to heroku database link

#developer repo
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jfgrougikqidof:1fe420ca8edb738fac285e431414aa706e0023644c952259a9fe4e1a3ee13590@ec2-184-73-247-240.compute-1.amazonaws.com:5432/der80kevtgq4nt'

#master repo
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wfibcqxjvbzada:5ea7dff6b2fd7aa8add4fc96326defc8eadbb2a34661e1304a3de08053817567@ec2-54-235-90-125.compute-1.amazonaws.com:5432/d6s3p8sri4ie30'


# Yu Hao repo
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bnyzbaqdwqypbf:d0588f108aa8f33ee3d4700bc38c71668c0be639960247a7930c2933ef5801f9@ec2-50-19-86-17.compute-1.amazonaws.com:5432/d2gvs5fsf3vs0p'



#secretkey for login
app.secret_key = 'development-key'

# router to home page
@app.route("/")
def index():
    return render_template("index.html")

# router to singup page
@app.route("/signup", methods=['GET', 'POST'])
def signup():
	form = SignupForm()
    # based on the method do different stuff
	if request.method == "POST":
        # if the form is false, it go to signup html again
		if form.validate() == False:
			return render_template('signup.html', form = form)
		else:
            # when form is true, create a new user
			newuser = User(form.first_name.data,
						   form.last_name.data,
						   form.email.data,
						   form.password.data)
            # add user into database
			db.session.add(newuser)
			db.session.commit()

			session['email'] = form.email.data
            # return to index.html
			return redirect(url_for('index'))
        # if method is get, return signup
	elif request.method =="GET":
		return render_template('signup.html', form = form)

# router to create page
@app.route("/create")
def create_page():
	return render_template("create_page.html")


# router to login page with different methods
@app.route("/login" , methods = ["GET" , "POST"])
def login():
    # get the login form
	form = LoginForm()
    # if the method is post
	if request.method == "POST":
        # check if it is correct
		if form.validate() == False:
            # return login if it is false
			return render_template("login.html" , form = form)
		else:
            # when it is true, check the database
			email = form.email.data
			password = form.password.data
			user = User.query.filter_by(email=email).first()
			if user is not None and user.check_password(password):
				session['email'] = form.email.data
				#return redirect(url_for('home'))
				return render_template('index.html',userLoggedIn = True)
			else:
                # esle return log in
				return redirect(url_for('login'))
            # if method is get
	elif request.method == 'GET':
        # go to login page
		return render_template('login.html', form= form)


# router to logout
@app.route("/logout")
def logout():
	session.pop('email',None)
	return redirect(url_for('index'))


# router to search
@app.route("/search")
def browse():
	return render_template("search.html")



# router to chatroom
@app.route("/chatroom")
def chatroom():
	return render_template("chatroom.html")
# router to chatroom_video
@app.route("/chatroom_video")
def chatroom_video():
	return render_template("chatroomvideo.html")
# router to test.html 
@app.route("/yuhao_test")
def yh_test():
    return render_template("yuhao_test.html")

if __name__ == "__main__":
	app.run(debug=True)
