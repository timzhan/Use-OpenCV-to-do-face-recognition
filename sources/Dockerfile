FROM arm32v7/python:3.7-buster

WORKDIR /app

# Install dependencies
RUN apt-get update
RUN apt-get install -y \
    python3 \
    python3-dev \
    python3-pip 

# Install opencv-python
# RUN pip install opencv-python

COPY requirements.txt ./
RUN pip3 install --index-url=https://www.piwheels.org/simple -r requirements.txt

# Copy the face-detect algorithm
COPY haarcascade_frontalface_default.xml ./

# Install other dependencies
RUN apt-get install -y \
    libjpeg62 \
    libsm6 \
    libxrender1 \
    libfontconfig1 \
    libice6 \
    libwebp-dev \
    libtiff-tools \
    libopenjp2-7 \
    libopenexr-dev \
    libhdf5-serial-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libgtk-3-dev \
    liblapack3 \
    libatlas-base-dev

COPY . .

# EXPOSE 8888

CMD [ "python3", "main.py"]