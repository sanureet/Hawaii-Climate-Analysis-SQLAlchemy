# import Flask
from flask import Flask, jsonify


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
    print("test values")
    return "precp page"



if __name__ == "__main__":
    app.run(debug=True)

