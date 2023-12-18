from flask import Flask, jsonify, request, abort
from models import Advertisement, Session

app = Flask(__name__)

ads_database = {}

@app.route('/ad', methods=['POST'])
def create_ad():
    data = request.json

    new_ad = Advertisement(
        title=data['title'],
        description=data['description'],
        creation_date=data['creation_date'],
        owner=data['owner']
    )

    session = Session()
    session.add(new_ad)
    session.commit()

    return jsonify({'id': new_ad.id}), 201

@app.route('/ad/<int:ad_id>', methods=['GET'])
def get_ad(ad_id):
    session = Session()
    ad = session.query(Advertisement).filter_by(id=ad_id).first()
    session.close()

    if ad is None:
        abort(404)

    return jsonify({
        'id': ad.id,
        'title': ad.title,
        'description': ad.description,
        'creation_date': ad.creation_date,
        'owner': ad.owner
    })

@app.route('/ad/<int:ad_id>', methods=['DELETE'])
def delete_ad(ad_id):
    session = Session()
    ad = session.query(Advertisement).filter_by(id=ad_id).first()

    if ad is None:
        session.close()
        abort(404)

    session.delete(ad)
    session.commit()
    session.close()

    return jsonify({'result': True})

@app.route('/ad/<int:ad_id>', methods=['PUT'])
def update_ad(ad_id):
    session = Session()
    ad = session.query(Advertisement).filter_by(id=ad_id).first()

    if ad is None:
        session.close()
        abort(404)

    data = request.json
    ad.title = data.get('title', ad.title)
    ad.description = data.get('description', ad.description)
    ad.creation_date = data.get('creation_date', ad.creation_date)
    ad.owner = data.get('owner', ad.owner)

    session.commit()
    session.close()

    return jsonify({
        'id': ad.id,
        'title': ad.title,
        'description': ad.description,
        'creation_date': ad.creation_date,
        'owner': ad.owner
    })

if __name__ == '__main__':
    app.run(debug=True)
