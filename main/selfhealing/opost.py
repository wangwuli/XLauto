from flask import request
from . import selfhealing


@selfhealing.route('/selfhealing/opost', methods=['GET', 'POST', 'PUT', 'DELETE'])
def opost():
    data_dict = request.get_json()


    return data_dict