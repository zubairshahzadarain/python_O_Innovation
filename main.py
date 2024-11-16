
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List  
from contextlib import asynccontextmanager
import pandas as pd
from insert_csv_data_crud import store_images_in_db
from database_session import get_db
from schemas import ImageResponse
from services import resize_and_apply_colormap
from sqlalchemy.sql import text
from fastapi import Query
app = FastAPI()

# Load the CSV data and process it
data = pd.read_csv('img.csv')
data = data.dropna()
data[['image_base64', 'image_shape']] = data.iloc[:, 1:].apply(resize_and_apply_colormap, axis=1, result_type='expand')

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = next(get_db())
    store_images_in_db(db, data)
    print("Images processed and stored in the database.")




@app.get("/api/get_images", response_model=List[ImageResponse])
async def get_images(depth_min: int, depth_max: int, db: Session = Depends(get_db) ,limit: int = Query(100, ge=1),    offset: int = Query(0, ge=0) ):
    try:
        query = text("SELECT depth, image_base64, image_shape FROM image_data WHERE depth BETWEEN :depth_min AND :depth_max LIMIT :limit OFFSET :offset")

        # Execute the query with parameters
        result = db.execute(query, {"depth_min": depth_min, "depth_max": depth_max, "limit": limit,
            "offset": offset }).fetchall()
        images = [{"depth": row[0], "image_base64": row[1], "image_shape": row[2]} for row in result]
        return JSONResponse(content=images)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
