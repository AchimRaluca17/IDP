from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask import jsonify

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def hello_world():
        return 'Hello World !'

    @app.route('/add_ride', methods=['GET'])
    def add_ride():
        return render_template('add_ride.html')

    @app.route('/add_ride', methods=['POST'])
    def add_ride_post():
        source = request.form['source']
        destination = request.form['destination']
        departureDay = request.form['departureDay']
        departureHour = request.form['departureHour']
        duration = request.form['duration']
        seats = request.form['seats']
        id = request.form['id']
        res = functions.add_ride(source, destination, departureDay, departureHour, duration, seats, id)
        if res:
            return jsonify(response="Ride added!"), 200
        else:
            return jsonify(response="Try another ID -> this route exists!"), 200

    @app.route('/remove_ride', methods=['GET'])
    def remove_ride():
        return render_template('remove_ride.html')

    @app.route('/remove_ride', methods=['POST'])
    def remove_ride_post():
        id = request.form['id']
        rsp = functions.remove_ride(id)
        if rsp:
            return jsonify(response="Ride removed!"), 200
        else:
            return jsonify(response="We can't find this route!"), 400

    login_manager.init_app(app)
    login_manager.login_message = 'You must be logged in to access this page'
    login_manager.login_view = 'auth.login'

    migrate = Migrate(app,db)

    from app import models
    from app import functions

    return app
