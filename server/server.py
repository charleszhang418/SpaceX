from flask import Flask, request, jsonify
from flask_cors import CORS

# python3 server.py 
app = Flask(__name__)
CORS(app)

# Localhost URL: http://127.0.0.1:5000/api/home
@app.route("/api/home")
def home():
    return jsonify({"hello":"222"}), 200

# GET: placeholder
@app.route("/api/fetch/<params>")
def get_user(params):
    user_data = {
        "message": params
    }
    extra = request.args.get("extra")

    # do processing here #

    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

# POST 

# PUT

# DELETE

if __name__ == "__main__":
    app.run(debug=True, port=8080)


