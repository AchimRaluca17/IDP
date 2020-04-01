import sys
import requests

# api-endpoint
URL_ADD_RIDE = "http://managemenet_server:5000/add_ride"
URL_REMOVE_RIDE = "http://managemenet_server:5000/remove_ride"
URL_BOOK_TICKET = "http://service:6000/book_ride"
URL_BUY_TICKET = "http://service:6000/buy_ticket"

while True:
    print("""Commands:
            Press 1 to add a new ride
            Press 2 to remove a ride
            Press 3 to book a ticket
            Press 4 to buy a ticket""")

    inp = input("Your Command: ")

    if inp == "1":
        id = input("ID: ")
        source = input("Source: ")
        destination = input("Destination: ")
        departure_day = input("Departure day: ")
        departure_hour = input("Departure hour: ")
        duration = input("Duration: ")
        seats = input("Nr Of Seats: ")

        ok = True
        try:
            PARAMS = {
                "source": source,
                "destination": destination,
                "departureDay": int(departure_day),
                "departureHour": int(departure_hour),
                "duration": int(duration),
                "seats": int(seats),
                "id": id
            }
        except Exception as e:
            ok = False
            print("""Incorrect data inserted""")

        if ok:
            resp = requests.post(URL_ADD_RIDE, data=PARAMS)
            print(resp.status_code, resp.json())
            print("\n")

    if inp == "2":
        id = input("ID: ")

        PARAMS = {
            "id": id
        }
        resp = requests.post(URL_REMOVE_RIDE, data=PARAMS)
        print(resp.status_code, resp.json())
        print("\n")


    if inp == "3":
        ids = input("Insert the ID for which you want to make a reservation: ")

        PARAMS = {
            "ids": ids
        }
        resp = requests.post(URL_BOOK_TICKET, data=PARAMS)
        print(resp.status_code, resp.json())
        print("\n")


    if inp == "4":
        id = input("Reservation ID: ")

        PARAMS = {
            "reservation_id": id
        }
        resp = requests.post(URL_BUY_TICKET, data=PARAMS)
        print(resp.status_code, resp.json())
        print("\n")
