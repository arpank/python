from flask import Flask
from flask import Flask, jsonify, abort, request, make_response, url_for

from django.http import JsonResponse
from collections import OrderedDict

import sys, os
sys.path.insert(0, "/path/to/parent/of/courseware") # /home/projects/my-djproj

from manage import DEFAULT_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_SETTINGS_MODULE)

import django
django.setup()

app = Flask(__name__)

@app.route('/')
def index():
    data = OrderedDict([('doc', '546546545'), ('order', '98745'), ('nothing', '0.0')])
    return JsonResponse(data)

    #return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)

