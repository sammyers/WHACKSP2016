from flask import Flask

application = Flask(__name__)

import constants, models, database, forms, permutations
