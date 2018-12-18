from datetime import datetime

from flask import Flask, request

app = Flask(__name__)

##
## Actually setup the Api resource routing here
##
from api import *


if __name__ == '__main__':
    app.run(debug=True)
