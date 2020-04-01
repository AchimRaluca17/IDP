from app import models


def verify_overbooking(id, bookings):
    try:
        obj = models.db.session.query(models.Ride).filter_by(id=id).one()
        seats = obj.seats
        overload = (seats * 11) / 10
        x = (bookings > overload)
        return x
    except Exception as _:
        return True


def book_ride(ids):
    try:
        ids_list = [x.strip() for x in ids.split(',')]
        bookings = models.Booking.query.all()
        for id in ids_list:
            count = 0
            for book in bookings:
                book_ids = [x.strip() for x in book.ids.split(',')]
                if id in book_ids:
                    count = count + 1
            rsp = verify_overbooking(id, count)
            if rsp is True:
                return 0
        booking = models.Booking(ids=ids)
        models.db.session.add(booking)
        models.db.session.commit()
        return booking.id
    except Exception as _:
        return 0


def buy_ticket(reservation_id):
    try:
        obj = models.db.session.query(models.Booking).filter_by(id=reservation_id).one()
        if obj:
            ticket = models.Ticket(reservation_id=reservation_id)
            models.db.session.add(ticket)
            models.db.session.commit()
            return 1
        return 0
    except Exception as _:
        return 0

