from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import registry

metadata = MetaData()
mapper_registry = registry()

# Define the image_data table model
image_data = Table('image_data', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('depth', Integer, nullable=False),
                   Column('image_base64', String(9000), nullable=False),
                   Column('image_shape', String(50), nullable=False)
                   )
