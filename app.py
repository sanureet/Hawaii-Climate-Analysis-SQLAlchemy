# import Flask
from flask import Flask, jsonify

# Import sqlalchemy
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Create engine and Base
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# make classes
measurement = Base.classes.measurement
Station = Base.classes.station


# Flask set up
app = Flask(__name__)

# Flask routes

@app.route("/")
def welcome():
    return (
        
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation:<br/>"
        f"/api/v1.0/stations:<br/>"
        f"/api/v1.0/tobs:<br/>"
        f"/api/v1.0/<start><br/>"
        f"put the start date in 'YYYY-MM-DD' format<br/>"
        f"/api/v1.0/<start>/<end><br/>"
        f"put the dates in 'YYYY-MM-DD/YYYY-MM-DD' format<br/>"
    )
       

@app.route("/api/v1.0/precipitation")
def precp():
 #   print("test values")
 #   return "precp page"
    session = Session(engine)
# calculate the date
    last_date = session.query(measurement.date).order_by(measurement.date.desc()).first()[0]
    last_date = dt.datetime.strptime(last_date, "%Y-%m-%d")

    last_year = last_date - dt.timedelta(days = 365)


    #perform a query to get data

    precip_results = (
    session.query(measurement.date,measurement.prcp)
    .filter(measurement.date > last_year)
    .order_by(measurement.date)
    .all()
    )
    return jsonify(precip_results)

@app.route("/api/v1.0/stations")  
def stations():
    # lists of stations
     session = Session(engine)
     station_count  = (
            session.query(measurement.station, func.count(measurement.station))
                .group_by(measurement.station)
                .order_by(func.count(measurement.station).desc())
                .all()
    )

     return jsonify(station_count)

@app.route("/api/v1.0/tobs") 
def tobs():

    session = Session(engine)

    temp_observation = station_count[0][0]
    results = (
        session.query(measurement.date, measurement.tobs).\
                filter(measurement.date >= "2016-08-24").\
                filter(measurement.date <= "2017-08-23").\
                filter(measurement.station == temp_observation).all()
    )
    
    return jsonify(results)

@app.route("/api/v1.0/<start>")
def start(start):
    session = Session(engine)
    most_active_station = 'USC00519281'

    temp = (
        session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
                filter(measurement.station == most_active_station).all()
    )
    
    return jsonify(temp)

@app.route("/api/v1.0/<start>/<end>")
def start_end_day(start, end):
    session = Session(engine)
    calc_temps=('2012-02-28', '2012-03-05')
    calc_temps=('start_date', 'end_date')
    start_date = '2012-02-28'
    end_date = '2012-03-05'


    results = (
        session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start_date).filter(measurement.date <= end_date).all()

    )
    return jsonify(results)





    if __name__ == "__main__":
        app.run(debug=True)

