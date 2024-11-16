# Python Engineer Technical Challenge

## Overview

This repository contains the solution for the Python Engineer technical challenge at Open Innovation AI. The challenge focuses on processing image data, resizing it, applying a color map, and storing the results in a MySQL database. Additionally, an API is provided to retrieve image data based on specific depth ranges. The solution is implemented using Python, FastAPI, SQLAlchemy, and MySQL, with Docker orchestration for easy deployment.

## Project Features

- **Image Resizing**: Resize image width from 200 to 150 pixels using bilinear interpolation.
- **Color Mapping**: Apply a custom color map (`COLORMAP_JET`) to the resized images.
- **API**: An endpoint to retrieve image frames based on depth ranges (`depth_min`, `depth_max`).
- **Database**: Store image data as Base64-encoded strings in a MySQL database.
- **Dockerized**: The solution is containerized using Docker and Docker Compose, simplifying deployment.

## Technologies Used

- **Python 3.8.18+**
- **FastAPI**: For building the web API.
- **SQLAlchemy**: ORM for MySQL database interaction.
- **MySQL**: Relational database for storing image data.
- **OpenCV**: For image processing and color map application.
- **Docker**: For containerization of the application and database.
- **Pandas**: For CSV data manipulation.

## Setup & Installation

### Prerequisites

- Docker 24.0.5+ installed on your system.
- Python 3.8.18+ and the required Python packages.

### Steps to Run the Project Locally

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/zubairshahzadarain/python_O_Innovation.git
   move project directory 
   sudo docker-compose build
    sudo docker-compose up
    once  start  application will start on port 5000 
   http://localhost:5000/docs#/default/get_images_api_get_images_get
