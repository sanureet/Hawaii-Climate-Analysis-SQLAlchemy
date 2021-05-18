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
    )

@app.route("/api/v1.0/precipitation")
def precp():
    print("test values")
    return "precp page"



if __name__ == "__main__":
    app.run(debug=True)

