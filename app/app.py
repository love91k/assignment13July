# app.py

import os

import boto3

from flask import Flask, jsonify, request
app = Flask(__name__)

s3=boto3.resource('s3')

@app.route("/")
def s3_files():
    s3_files = []
    #BUCKET_NAME = 'myhelmrepo2401'
    BUCKET_NAME = os.environ.get('S3_BUCKET')
    allFiles = s3.Bucket(BUCKET_NAME).objects.all()
    for file in allFiles:
        if file.key[-1] != '/':
            s3_files.append(file.key)
    return jsonify(s3_files)



if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=5000)

