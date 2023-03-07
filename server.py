from flask import Flask, render_template, request, flash, session, redirect, jsonify
import os
import crud
from model import connect_to_db, db
import requests 

from jinja2 import StrictUndefined

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
connect_to_db(app)


app.secret_key = os.environ["secret_key"]

@app.route('/')
def homepage():
    """Display homepage with calendar"""
    
    return render_template('homepage.html')

@app.route('/register')
def new_user():
    """Display form to create a new user"""


    return render_template('register.html')


@app.route('/register', methods=['POST'])
def user_registration():
    """Create a new user and add information to db"""


    email = request.form.get('email')
    password = request.form.get('password')
    fname = request.form.get('fname')
    lname = request.form.get('lname')

 

 

    user = crud.create_user(email, password, fname, lname)
    db.session.add(user)
    db.session.commit()
    flash('Account created with sucess! Please log in to your account.')

    return redirect('/')


@app.route('/login', methods=['POST'])
def login_form():
    """Process user login"""

    email = request.form.get('email')
    password = request.form.get('password')
    
    user = crud.get_user_by_email(email)
    
   
    if not user or password != user.password:

        flash('The email or password you entered was incorrect.')

        return redirect('/')
        
    else:

        session['user_email'] = user.email
        flash(f'Welcome {user.fname}!')

        return redirect('/appointment')
    
    
@app.route('/appointment', methods=['GET', 'POST'])
def calendar_schedule():
    """Display calendar to user """

    request.args.get=('show_appointment')
    available = crud.free_appointments()

    return render_template('calendar.html', available=available)



@app.route('/upcoming_appointment')
def show_appointments():
    """Display appointments"""

    email= session['user_email']
    user = crud.get_user_by_email(email)

    appointments = crud.get_appointments(user.user_id)
   
    

    return render_template('saved.html', appointments=appointments)


@app.route('/appointment_process', methods=['GET','POST'])
def process_appointment():
    """Upcoming appointment process"""

    email = session['user_email']
    user = crud.get_user_by_email(email)


   
    date = request.form.get('date')
    time = request.form.get('time')
    save = crud.create_saved(user.user_id, date, time)
    db.session.add(save)
    db.session.commit()


    return redirect('/upcoming_appointment')


@app.route('/logout', methods=['GET','POST'])
def process_logout():
    """Log out user in session"""

    request.form.get('logout')

    session['user_email']

    session.pop('user_email', None)
    flash('Logged out.')
    
    return redirect('/')



if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
   