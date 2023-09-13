from flask import Flask, url_for, Response
import cv2

app = Flask(__name__)

video = cv2.VideoCapture(0)

def get_frames():
    while video.isOpened():
        frame = video.read()[1]
        ret, buffer = cv2.imencode('.jpg',frame)
        if not ret:
            break
        frame = buffer.tobytes()
        yield(b'--frame\r\n'
                b'Content-Type: iamge/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/feed')
def feed():
    return Response(get_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)