import json
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
#from sqlalchemy.schema import UniqueConstraint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
# app.config['SQLAlchemy_DATABASE_URI'] = 'mysql://root:root@db/main'
CORS(app)
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

    def as_dict(self):
        obj_d = {
            'id': self.id,
            'title': self.title,
            'image': self.image,
        }
        return obj_d
    
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    
    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/api/products')
def index():
    products = Product.query.all()    
    results = [product.as_dict() for product in products]

    for u in db.session.query(Product).all():
        print(u._asdict())

    return "to_array(data)"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
