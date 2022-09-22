import model.scrapy
from flask import jsonify

def scrapy_get():
    execute_query_response = model.scrapy.scrapy_get()
    if execute_query_response['status']:
        data = execute_query_response['content']
    return jsonify(data),200