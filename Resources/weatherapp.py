# Import dependancies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import extract
from flask import Flask, jsonify, session

# Define variables for queries
engine = create_engine("sqlite:///../hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
import weatherapp

# Define app and create welcome page
app = Flask(__name__)
@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/june_temp_stats<br/>"
        f"/api/v1.0/dec_temp_stats<br/>"
        f"/api/v1.0/comparison_temp_data<br/>"
        f"/api/v1.0/monthly_temp_data<br/>"
        f"/api/v1.0/june_precip_stats<br/>"
        f"/api/v1.0/dec_precip_stats<br/>"
        f"/api/v1.0/comparison_precip_data<br/>"
        f"/api/v1.0/monthly_precip_data<br/>"
    )

# Create function for listing descriptive stats for June temps
@app.route("/api/v1.0/june_temp_stats")
def june_temp_stat():
    """Query database for June temp data"""
    june_temps = session.query(Measurement.tobs).filter(extract('month', Measurement.date)==6).all()
    """ Create a list of the temperature data collected"""
    june_temps_list = [temp.tobs for temp in june_temps]
    """ Create a dataframe from the list"""
    june_temp_df = pd.DataFrame(june_temps_list, columns=['temp'])
    """ Get the descriptive statistics for June temperatures"""
    june_temp_stats = june_temp_df.describe()
    """ Convert stat data to json form"""
    june_data = june_temp_stats.to_json()
    return jsonify(june_data)

# Create function for listing descriptive stats for Dec temps
@app.route("/api/v1.0/dec_temp_stats")
def dec_temp_stat():
    """Query database for Dec temp data"""
    dec_temps = session.query(Measurement.tobs).filter(extract('month', Measurement.date)==12).all()
    """ Create a list of the temperature data collected"""
    dec_temps_list = [temp.tobs for temp in dec_temps]
    """ Create a dataframe from the list"""
    dec_temp_df = pd.DataFrame(dec_temps_list, columns=['temp'])
    """ Get the descriptive statistics for June temperatures"""
    dec_temp_stats = dec_temp_df.describe()
    """ Convert stat data to json form"""
    dec_data = dec_temp_stats.to_json()
    return jsonify(dec_data)

#
@app.route("/api/v1.0/comparison_temp_data")
def temp_avg_monthly():
    """ Query database for June and Dec temps and get the average for each year"""  
    sel = [func.avg(Measurement.tobs)]
    temp_data = session.query(*sel, Measurement.date).filter(func.strftime("%m", Measurement.date).in_(["06", "12"])).\
        group_by(func.strftime("%m", Measurement.date)).group_by(func.strftime("%Y", Measurement.date)).\
            order_by(Measurement.date).all() 
    total_avg_temp = list(np.ravel(temp_data))
    return jsonify(total_avg_temp)
        
@app.route("/api/v1.0/monthly_temp_data")
def monthly_temp_data():
    """ Query database for average temperature per month"""
    sel = [func.avg(Measurement.tobs)]
    temp_all = session.query(Measurement.date, *sel).group_by(func.strftime("%m", Measurement.date)).all()
    monthly_avg_temp = list(np.ravel(temp_all))
    return jsonify(monthly_avg_temp)
    
@app.route("/api/v1.0/june_precip_stats")
def june_precip_stat():
    """ Query database for June precipitation data"""
    results_june_prcp = session.query(Measurement.prcp).filter(extract('month', Measurement.date)==6).all()
    june_prcp_df = pd.DataFrame(results_june_prcp, columns=['prcp'])
    june_precip_stats = june_prcp_df.describe()
    june_precip_stats = june_precip_stats.to_json()
    return jsonify(june_precip_stats)

@app.route("/api/v1.0/dec_precip_stats")
def dec_precip_stat():
    """ Query database for Dec precipitation data"""
    dec_precip = session.query(Measurement.prcp).filter(extract('month', Measurement.date)==12).all()
    dec_precip_list = [precip.prcp for precip in dec_precip]
    dec_prcp_df = pd.DataFrame(dec_precip_list, columns=['prcp']).dropna()
    dec_precip_stats = dec_prcp_df.describe()
    dec_precip_stats = dec_precip_stats.to_json()
    return jsonify(dec_precip_stats)

@app.route("/api/v1.0/comparison_precip_data")
def precip_data_total():
    """Create DataFrame of the average prcp data of June and Dec by year"""
    sel = [func.avg(Measurement.prcp)]
    precip_data = session.query(*sel, Measurement.date).filter(func.strftime("%m", Measurement.date).\
        in_(["06", "12"])).group_by(func.strftime("%m", Measurement.date)).\
            group_by(func.strftime("%Y", Measurement.date)).order_by(Measurement.date).all() 
    total_avg_prcp = list(np.ravel(precip_data))
    return jsonify(total_avg_prcp)

@app.route("/api/v1.0/monthly_precip_data")
def monthly_precip_data():
    """Show average temp data per year by month"""
    sel = [func.avg(Measurement.prcp)]
    prcp_all = session.query(Measurement.date, *sel).group_by(func.strftime("%m", Measurement.date)).all()
    total_avg_prcp = list(np.ravel(prcp_all))
    return jsonify(total_avg_prcp)

if __name__ == "__main__":
    app.run(debug=True)
