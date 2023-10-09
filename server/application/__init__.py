from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi



# Run local: python3 server.py 
# Secret: 'd1dfd4575b676126e8ca77b3d4d9721781263d60'
app = Flask(__name__)
app.config["SECRET_KEY"] = 'd1dfd4575b676126e8ca77b3d4d9721781263d60'
app.config["MONGO_URI"] = 'mongodb+srv://x389xu:x389xu@zootopia.njs8uvs.mongodb.net/'

CORS(app)


uri = "mongodb+srv://x389xu:x389xu@zootopia.njs8uvs.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"


# mongodb database
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

mongodb_client = MongoClient(uri)
entry_metadata_db = mongodb_client["entry_metadata"]
datasets_db = mongodb_client["datasets"]

# databases
# entry_metadata_db = mongodb_client["entry_metadata"]


from application import routes

# @app.route('/')
# def home():
#     return 'Hello, World!'

# # MongoDB
# @app.route("/getDatasetsMetadata", methods=['GET','POST'])
# def getDatasetsMetadata():
#     if request.method == 'POST':
#         data = request.form
#         print(data)
#     return render_template('index.html')


# if __name__ == "__main__":
#     app.run(debug=True, port=8080)



# # Localhost URL: http://127.0.0.1:5000/
# @app.route('/example', endpoint='example1')
# def home():
#     return jsonify({"hello":"222"}), 200

# # GET: placeholder
# @app.route("/api/fetch/<params>")
# def get_user(params):
#     user_data = {
#         "message": params
#     }
#     extra = request.args.get("extra")

#     # do processing here #

#     if extra:
#         user_data["extra"] = extra

#     return jsonify(user_data), 200





