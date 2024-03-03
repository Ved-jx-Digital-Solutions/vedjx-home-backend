from flask import Flask

app = Flask(__name__)


@app.route('/home', methods=["GET"])
def get_user_data():
    # Returns fake data for now
    return {
        "name": "John Doe",
    }

