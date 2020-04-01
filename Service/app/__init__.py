from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask import jsonify
import requests

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def hello_world():
        return 'Hello I am the service running here! DB is with me'

    @app.route('/book_ride', methods=['GET'])
    def book_ride():
        return render_template('book_ride.html')

    @app.route('/buy_ticket', methods=['GET'])
    def buy_ticket():
        return render_template('buy_ticket.html')

    @app.route('/book_ride', methods=['POST'])
    def book_ride_post():
        ids = request.form['ids']
        response = functions.book_ride(ids)

        if response != 0:
            resp = "You booking id: " + str(response)
            return jsonify(response=resp), 200
        else:
            return jsonify(response="Sorry, the rides with this ID are overbooked!"), 400

    @app.route('/buy_ticket', methods=['POST'])
    def buy_ticket_post():
        reservation_id = request.form['reservation_id']
        response = functions.buy_ticket(reservation_id)

        if response != 0:
            return jsonify(response="Congratulations, you have a ticket now!"), 200
        else:
            return jsonify(response="You need to make a reservation first"), 400

    login_manager.init_app(app)
    login_manager.login_message = 'You must be logged in to access this page'
    login_manager.login_view = 'auth.login'

    migrate = Migrate(app,db)

    from app import models
    from app import functions

    return app
