from sqlalchemy.orm import Session
from models import image_data
import json

def store_images_in_db(db: Session, data):
    for idx, row in data.iterrows():
        depth = row['depth']
        image_base64 = row['image_base64']
        image_shape = json.dumps(row['image_shape'])
        db.execute(image_data.insert().values(depth=depth, image_base64=image_base64, image_shape=image_shape))
    db.commit()
