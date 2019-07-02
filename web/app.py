from __future__ import absolute_import, division, print_function
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import requests
import json
import tensorflow as tf
from tensorflow import keras
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import pickle

app = Flask(__name__)
api = Api(app)

class Request(Resource):
    def post(self):
        posted_data = request.get_json()
        
        infile = open("./model_data/vectorizer",'rb')
        vectorizer = pickle.load(infile)
        infile.close()
        model = tf.keras.models.load_model(
            './model_data/trump_model',
            custom_objects=None,
            compile=True
        )
        tweet = posted_data["tweet"]
        tweet_parsed = [sparse_row.indices for sparse_row in  vectorizer.transform([tweet])][0].tolist()
        x =model.predict(np.array([tweet_parsed]))
        sim = x.tolist()[0][0]
        ret_json = {
            "status":200,
            "msg":sim
        }
        return jsonify(ret_json)
    
api.add_resource(Request, '/request')

if __name__=="__main__":
    app.run(host='0.0.0.0')
