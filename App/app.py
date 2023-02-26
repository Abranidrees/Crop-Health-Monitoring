# importing libaraies
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import Geometry
from shapely.geometry import mapping
from geoalchemy2.shape import to_shape
import psycopg2

# connect to postgresql database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/tech'
app.config['SQLALCHEMY_SCHEMA'] = 'sa'
app.config['SQLALCHEMY_TABLE'] = 'image_meta'
db = SQLAlchemy(app)
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
conn = psycopg2.connect(
    host="localhost",
    database="tech",
    user="postgres",
    password="postgres",
)

# Class to get the specific attributes of the image from the database
class MyTable(db.Model):
    __tablename__ = app.config['SQLALCHEMY_TABLE']
    __table_args__ = {'schema': app.config['SQLALCHEMY_SCHEMA']}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    footprint = db.Column(Geometry('POLYGON', srid=4326), nullable=False)
    date = db.Column(db.TIMESTAMP, nullable=False)
    processing_level = db.Column(db.String)
    cloud_cover_percentage =db.Column(db.Float)
    product_type = db.Column (db.Text)

    
    
    
# Flask route to get the only footprints of the images 

@app.route('/meta', methods=['GET'])
def map_route():
    session = Session()
    my_table = session.query(MyTable).first()
    footprint_geojson = mapping(to_shape(my_table.footprint))
    return render_template('dashboard.html', footprint_geojson=footprint_geojson)

# Flask route to get the footprints  and the metadata of the images 
@app.route('/', methods=['GET'])
def meta_route():
    session = Session()
    my_table = session.query(MyTable).all()
    features = []
    for row in my_table:
        feature = {
            'type': 'Feature',
            'geometry': mapping(to_shape(row.footprint)),
            'properties': {
                'Date': row.date,
                'Processing Level': row.processing_level,
                'Cloud Cover Percentage':row.cloud_cover_percentage,
                 'Product Type':row.product_type 
            }
        }
        features.append(feature)
    geojson = {
        'type': 'FeatureCollection',
        'features': features
    }
    return render_template('dashboard.html', footprint_geojson=geojson)

# Flask route to get the metadata of the images when someone click on the polygon (footprint)
@app.route('/mytable/<int:id>', methods=['GET'])
def mytable_route(id):
    session = Session()
    my_table = session.query(MyTable).get(id)
    if my_table is None:
        return jsonify({'error': 'MyTable with id {} not found'.format(id)})
    else:
        # get all the attributes
        attributes = {}
        for col in MyTable.__table__.columns:
            attributes[col.name] = getattr(my_table, col.name)
        return jsonify(attributes)

# flask route to get all satellite images metadata from the database
@app.route('/metadata', methods=['GET'])
def get_image_meta():
    cur = conn.cursor()
    cur.execute("SELECT * FROM sa.image_meta")
    # Return the HTML table
    return render_template('home.html',rows=cur.fetchall())

# flask route to get all satellite images in RGB 
@app.route('/quicklook_url', methods = ['GET'])    
def get_quicklook_url():
    cur = conn.cursor()
    cur.execute("SELECT quicklook_url FROM sa.image_meta")
    # Return the HTML table
    return render_template('url.html',rows=cur.fetchall())

# flask route to search satellite images metadata from the database
@app.route('/search', methods=['GET'])
def search():
    # Get start and end date from request arguments
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    # Execute SQL query to retrieve data within date range
    cur = conn.cursor()
    cur.execute("SELECT * FROM sa.image_meta WHERE date BETWEEN %s AND %s", (start_date, end_date))
    rows = cur.fetchall()

    # Return the HTML table
    return render_template('home.html', rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
