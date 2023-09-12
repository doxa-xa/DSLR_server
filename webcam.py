import cv2, numpy as np, datetime as time, csv
#from controls_1 import capture_image
from flask import Flask, Response
from snap import capture


app = Flask(__name__)

dt = time.datetime.now()
now = dt.strftime("%d%m%Y_%H%M%S")

def mse(imgA,imgB):
    height,width = imgA.shape
    differance = cv2.subtract(imgA,imgB)
    error = np.sum(differance**2)
    mean_sq_err = error/(float(height*width))
    return mean_sq_err

def capture_image():
    err, camera = cv2.VideoCapture(0)
    if not err:
        ret,frame = camera.read()
        while camera.isOpened():
            cv2.imwrite(f'static/{now}.jpg',frame)

def zoom(frame):
    height, width, channels = frame.shape
    centerX,centerY = int(height/2), int(width/2)
    radiusX,radiusY = int(100*height/100),int(100*width/100)
    minX,maxX = centerX-radiusX,centerX+radiusX
    minY,maxY = centerY-radiusY,centerY+radiusY
    cropped = frame[minX:maxX, minY:maxY]
    resized_cropped = cv2.resize(cropped, (width,height))
    return resized_cropped

def gen_frames(sensitivity):
    camera = cv2.VideoCapture(0)
    prev_err = 0.0
    err_csv_lst = []
    while camera.isOpened():
        suc, pframe = camera.read()
        previous_frame = pframe[:]
        success, frame = camera.read()
        pframe_zoom = zoom(previous_frame)
        frame_zoom = zoom(frame)
        if not success:
            break
        else:
            previous = cv2.cvtColor(pframe_zoom,cv2.COLOR_BGR2GRAY)
            current = cv2.cvtColor(frame_zoom,cv2.COLOR_BGR2GRAY)
            error = mse(current,previous)
            curr_err = error
            print(curr_err - prev_err)
            err_csv_lst.append(curr_err-prev_err)
            if curr_err is not None and curr_err - prev_err > sensitivity:
                    print(f'time: {time.datetime.now()} object detected')
                    capture()
                    continue
            ret, buffer = cv2.imencode('.jpg',frame_zoom)
            frame = buffer.tobytes()
            prev_err = error
            yield(b'--frame\r\n'
                  b'Content-Type: iamge/jpeg\r\n\r\n' + frame + b'\r\n')
            
@app.route('/<float:sens>')
def webcam(sens):
    return Response(gen_frames(sens),mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
            
