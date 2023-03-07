"""Crud functions"""

from model import db, User, Reservation, FakeAppointment, connect_to_db

def create_user(email, password, fname, lname):

    user = User(email=email, password=password, fname=fname, lname=lname)

    return user

def get_users():
    

    return User.query.all()


def get_user_by_id(user_id):
    

    return User.query.get(user_id)


def get_user_by_email(email):
   

    return User.query.filter(User.email == email).first()

def free_appointments():

    appointments = FakeAppointment.query.all()

    return appointments

def create_free_appointment(date, time):

    create_appointment= Reservation(date=date, time=time)

    return  create_appointment



def create_appointment(user, date, time):

    reservations= Reservation(user_id=user, date=date, time=time)

    return  reservations


def get_appointments(user):

    return Reservation.query.filter_by(user_id=user).all()

def get_appointment(user, date, time):

    return Reservation.query.filter_by(user_id=user, date=date, time=time).first()


if __name__ == '__main__':
    from server import app

    connect_to_db(app)