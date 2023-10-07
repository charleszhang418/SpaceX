from flask import Flask, request, jsonify

app = Flask(__name__)

# Localhost URL: http://127.0.0.1:5000
@app.route("/")
def home():
    return "Hello World!"

# GET: placeholder
@app.route("/<params>")
def get_user(params):
    user_data = {
        "params": params
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
    app.run(debug=True)

