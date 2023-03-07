"""Seed database for Isma Melon"""

from datetime import datetime
import os
from crud import FakeAppointment
import crud 
import model
import server

os.system("dropdb melons")
os.system("createdb melons")

model.connect_to_db(server.app)
model.db.create_all()

appointment1 = FakeAppointment(date=datetime(2023, 3, 8).date(), time=datetime(2023, 3, 8, 9, 0, 0).time())
appointment2 = FakeAppointment(date=datetime(2023, 3, 8).date(), time=datetime(2023, 3, 8, 10, 0, 0).time())
appointment3 = FakeAppointment(date=datetime(2023, 3, 8).date(), time=datetime(2023, 3, 8, 11, 0, 0).time())
appointment4 = FakeAppointment(date=datetime(2023, 3, 9).date(), time=datetime(2023, 3, 9, 14, 0, 0).time())
appointment5 = FakeAppointment(date=datetime(2023, 3, 9).date(), time=datetime(2023, 3, 9, 15, 0, 0).time())
appointment6 = FakeAppointment(date=datetime(2023, 3, 9).date(), time=datetime(2023, 3, 9, 16, 0, 0).time())

new_appointment =crud.create_free_appointment(date=datetime, time=datetime)
model.db.session.add_all([appointment1, appointment2, appointment3, appointment4, appointment5, appointment6])


model.db.session.commit()