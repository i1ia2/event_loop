from flask import Flask, jsonify, request, abort
# from models import Advertisement, Session

app = Flask(__name__)

ads_database = {}

@app.route('/ad', methods=['POST'])
def create_ad():
    data = request.json

    ad_id = len(ads_database) + 1

    ads_database[ad_id] = {
        'title': data['title'],
        'description': data['description'],
        'creation_date': data['creation_date'],
        'owner': data['owner']
    }
    return jsonify({'id': ad_id}), 201

@app.route('/ad/<int:ad_id>', methods=['GET'])
def get_ad(ad_id):
    ad = ads_database.get(ad_id)
    if ad is None:
        abort(404)
    return jsonify(ad)

@app.route('/ad/<int:ad_id>', methods=['DELETE'])
def delete_ad(ad_id):
    ad = ads_database.pop(ad_id, None)
    if ad is None:
        abort(404)
    return jsonify({'result': True})

@app.route('/ad/<int:ad_id>', methods=['PUT'])
def update_ad(ad_id):
    if ad_id not in ads_database:
        abort(404)
    data = request.json
    ads_database[ad_id].update({
        'title': data.get('title', ads_database[ad_id]['title']),
        'description': data.get('description', ads_database[ad_id]['description']),
        'creation_date': data.get('creation_date', ads_database[ad_id]['creation_date']),
        'owner': data.get('owner', ads_database[ad_id]['owner'])
    })
    return jsonify(ads_database[ad_id])

if __name__ == '__main__':
    app.run(debug=True)
