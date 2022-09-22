from flask import Flask
from route import routes

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
routes(app)
app.run(host='0.0.0.0',port=80)