from application import app
from flask import render_template, request, redirect, flash, url_for, Response

from bson import ObjectId

from application import entry_metadata_db
from application import datasets_db
from datetime import datetime
import pandas as pd
import csv
import json
from io import StringIO  # Import StringIO from the io module



@app.route('/')
def home():
    return 'Hello, World!'

@app.route("/getDatasetsMetadata")
def getDatasetsMetadata():
    datasets = []
    # entry_metadata = db.entry_metadata
    datasets_metadata = entry_metadata_db.datasets_metadata.find()

    for ds in datasets_metadata:
        ds["_id"] = str(ds["_id"])
        ds_str = json.dumps(ds)
        ds_json = json.loads(ds_str)
        datasets.append(ds_json)
    

    return datasets


@app.route("/getDataset")
def getDataset():
    title = request.args.get("title")
    datasets = []
    # dataset_coll = 
    # if title == 'mice_space_dnabert':
    dataset_coll = datasets_db.mice_space_dnabert.find()

    for ds in dataset_coll:
        ds["_id"] = str(ds["_id"])
        ds_str = json.dumps(ds)
        ds_json = json.loads(ds_str)
        datasets.append(ds_json)
    
     # Create a CSV string in memory
    csv_data = StringIO()
    csv_writer = csv.writer(csv_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    # Write CSV headers
    csv_writer.writerow(["_id", "notation", "DNA", "mass", "filename", "label"])
    
    # Write CSV data
    for x in datasets:
        csv_writer.writerow([
            x["_id"],
            x["notation"],
            x["DNA"],
            x["mass"],
            x["filename"],
            x["label"]
        ])


    # Set the appropriate headers for the CSV response
    response = Response(
        csv_data.getvalue(),
        content_type='text/csv',
    )
    response.headers['Content-Disposition'] = 'attachment; filename="dataset.csv"'

    return response