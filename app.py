import json
from context import Context
from marker import Marker
from coordinates import *
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    data1 = request.get_data()
    data_json = json.loads(data1)
    poi_list = data_json["poi_list"]
    # for poi in poi_list:
    #     lat = poi["lat"]
    #     lng = poi["lon"]
    tuple_latlng_str = ["8.5208, 47.37288", "8.53410, 47.37290"]
    marker = tuple_latlng_str
    context = Context()

    # if center is not None:
    #     context.set_center(parse_latlng(center))
    # if zoom is not None:
    #     context.set_zoom(zoom)
    for coords in marker:
        context.add_object(Marker(parse_latlng(coords)))
    image = context.render(200, 200)

    return '<h1>Hello World! Your browser is {}</h1>'.format(user_agent)