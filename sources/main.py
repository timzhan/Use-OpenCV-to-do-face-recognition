import cv2
from flask import Flask, render_template, Response

class cameraCapture(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0) 
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        ret, image = self.video.read()
        
        image_tagged = self.tag_faces(image)

        # Convert to jpg format
        ret, jpeg = cv2.imencode('.jpg', image_tagged)
        
        return jpeg.tobytes()

    def tag_faces(self, image):
        # Get user supplied values
        face_detect_path = './haarcascade_frontalface_default.xml'

        # Create the haar cascade objects - facee
        faces = cv2.CascadeClassifier(face_detect_path)

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        face = faces.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

        # Draw a rectangle around the faces
        for (x, y, w, h) in face:
            cv2.rectangle(image, (x, y), (x + w, y + h), color = (0, 255, 0), thickness = 2)

        # cv2.imshow('Faces detected', image)

        return image

    
app = Flask(__name__)

@app.route('/') 
def index():
    # jinja2 template，stored in templates/index.html
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        # if cv2.waitKey(5) & 0xff == ord('q'):
        #     break
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
   

@app.route('/video_feed') 
def video_feed():
    return Response(gen(cameraCapture()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')   


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
