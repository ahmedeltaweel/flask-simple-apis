# python
from json import dumps

# flask
from flask import Flask, request, Response


# internal
from utils import get_items, update_file

app = Flask(__name__)

'''
GET /api/v1/items/
GET /api/v1/items/<id>/
GET /api/v1/items/<id>/bids
POST /api/v1/v1/items/bid {'item_id', 'bid_amount', 'user_id'}

'''

# GET /api/v1/items/
@app.route('/api/v1/items/', methods=['GET'])
def get_items_api():
    return dumps(get_items())


# GET /api/v1/items/<id>/
@app.route('/api/v1/items/<int:item_id>/', methods=['GET'])
def get_item(item_id):
    for i in get_items():
        if i['id'] == item_id:
            return dumps(i)
    return Response(dumps({'msg': 'This item does not exists'}), status=404)


# GET /api/v1/items/<id>/bids
@app.route('/api/v1/items/<int:item_id>/bids/', methods=['GET'])
def get_item_bids(item_id):
    for i in get_items():
        if i['id'] == item_id:
            return dumps(i['bids'])
    return Response(dumps({'msg': 'This item does not exists'}), status=404)

# POST /api/v1/items/bid/ {'item_id', 'bid_amount', 'user_id'}
@app.route('/api/v1/items/bid/', methods=['POST'])
def add_item_bid():
    item_id = request.json.get('item_id', 0)
    bid_amount = request.json.get('bid_amount', 0)
    user_id = request.json.get('user_id', 0)
    # do something usefull with these data
    items = get_items()
    for i in items:
        if i['id'] == item_id:
            i['bids'].append(
                {
                    'user_id': user_id,
                    'amount': bid_amount,
                    'id': 5
                }
            )
            update_file(items)
            return Response(dumps({'msg': 'Created'}), status=201)
    return Response(dumps({'msg': 'This item does not exists'}), status=404)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8888)
