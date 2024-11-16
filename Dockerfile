# Use the official Python image from the Docker Hub
FROM python:3.8.18

WORKDIR /app


COPY requirements.txt .
COPY img.csv .
RUN apt-get update && apt-get install -y libglib2.0-0
RUN apt-get update && apt-get install -y libgl1-mesa-glx
# Install the dependencies specified in the requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
RUN  pip install opencv-python
RUN pip install fastapi[all] sqlalchemy aiomysql pydantic mysql-connector-python  pandas

COPY . .

# Expose the port FastAPI will run on
EXPOSE 5000

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
