from app import models

def add_ride(source, destination, departureDay, departureHour, duration, seats, id):
    try:
        ride = models.Ride(id=id, source=source, destination=destination, duration=duration, seats=seats, departure_hour=departureHour, departure_day=departureDay)
        models.db.session.add(ride)
        models.db.session.commit()
        return True
    except Exception as _:
        return False


def remove_ride(id):
    try:
        obj = models.Ride.query.filter_by(id=id).one()
        models.db.session.delete(obj)
        models.db.session.commit()
        return True
    except Exception as _:
        return False
