"""Model for Melon Scheduler"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    reservations = db.relationship('Reservation', back_populates = 'user')
    
    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email} fname={self.fname}>'
    

class Reservation(db.Model):

    __tablename__ = 'reservations'

    reservation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    date = db.Column(db.Date)
    time = db.Column(db.Time)

    user = db.relationship('User', back_populates = 'reservations')

    def __repr__(self):
        return f'<Reservation reservation_id={self.reservation_id} date={self.date}>'
    

class FakeAppointment(db.Model):

    __tablename__ = 'appointments_available'

    appointment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date)
    time = db.Column(db.Time)

    def __repr__(self):
        return f'<FakeAppointment appointment_id={self.appointment_id} date={self.date} time={self.time}>'


def connect_to_db(flask_app, db_uri="postgresql:///melons", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
    app.app_context().push()
    db.create_all()
