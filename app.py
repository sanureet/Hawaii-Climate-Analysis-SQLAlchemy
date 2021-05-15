# import Flask
from Flask import Flask, jsonify


# Flask set up
app = Flask(_name_)

# Flask routes
@app.route("/")
def main():
    print("message")
    return "main page"


