#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 10:27:30 2022

@author: liaoluyun
"""

import os
import sys
import json
import timeit

import pickle
import re
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from flask import Flask, request, make_response, jsonify
webapi = Flask(__name__)

# model_dir = '/Users/liaoluyun/Downloads/risk/model/'
# model_dir = '/risk-model-service/model/'
# 相对路径
model_dir = os.path.join(os.path.dirname(__file__), '../model/')

# NZB_card模型
fr = open(model_dir + 'NZB_card.pkl', 'rb')
NZB_card = pickle.load(fr)

# dk_card模型
fr = open(model_dir + 'dk_card.pkl', 'rb')
dk_card = pickle.load(fr)

# cd_card模型
fr = open(model_dir + 'cd_card.pkl', 'rb')
cd_card = pickle.load(fr)

# ld_card模型
fr = open(model_dir + 'ld_card.pkl', 'rb')
ld_card = pickle.load(fr)


@webapi.route('/')
def index():
    abort(401)


@webapi.route('/api/NZB_card', methods=['post'])
def api_NZB_card():
    start = timeit.default_timer()
    json = request.get_json()    

    data = pd.DataFrame(json["data"], index=[0])
    for x in data.columns:
        if json["data"][x] is None:
            data[x] = np.NAN
    
    my_card = NZB_card

    #得分
    score = my_card.predict(data)

    time = timeit.default_timer() - start
    
    response = {'code': 0, 'msg': "", 'data': {'score': score[0], 'time': time}}
    return make_response(jsonify(response), 200)

@webapi.route('/api/dk_card', methods=['post'])
def api_dk_card():
    start = timeit.default_timer()
    json = request.get_json()    

    data = pd.DataFrame(json["data"], index=[0])
    for x in data.columns:
        if json["data"][x] is None:
            data[x] = np.NAN
    
    my_card = dk_card

    #得分
    score = my_card.predict(data)

    time = timeit.default_timer() - start
    
    response = {'code': 0, 'msg': "", 'data': {'score': score[0], 'time': time}}
    return make_response(jsonify(response), 200)

@webapi.route('/api/cd_card', methods=['post'])
def api_cd_card():
    start = timeit.default_timer()
    json = request.get_json()    

    data = pd.DataFrame(json["data"], index=[0])
    for x in data.columns:
        if json["data"][x] is None:
            data[x] = np.NAN
    
    my_card = cd_card

    #得分
    score = my_card.predict(data)

    time = timeit.default_timer() - start
    
    response = {'code': 0, 'msg': "", 'data': {'score': score[0], 'time': time}}
    return make_response(jsonify(response), 200)

@webapi.route('/api/ld_card', methods=['post'])
def api_ld_card():
    start = timeit.default_timer()
    json = request.get_json()    

    data = pd.DataFrame(json["data"], index=[0])
    for x in data.columns:
        if json["data"][x] is None:
            data[x] = np.NAN
    
    my_card = ld_card

    #得分
    score = my_card.predict(data)

    time = timeit.default_timer() - start
    
    response = {'code': 0, 'msg': "", 'data': {'score': score[0], 'time': time}}
    return make_response(jsonify(response), 200)


if __name__ == '__main__':
    webapi.run()
