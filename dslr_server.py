from flask import Flask, Response, redirect, render_template, request,url_for
from capture_settings import CaptureSettings
from ptp_device_prop import PTPDeviceProps
import cv2
app = Flask(__name__)

camera = cv2.VideoCapture(0)

def gen_frames(camera):
    if not camera.isOpened():
        camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        #detector = cv2.CascadeClassifier('libcascades/lbpcascade_frontalface_improved.xml')
        #faces = detector.detectMultiScale(frame, 1.2, 6)   
        #for(x,y,w,h) in faces:
            #frame_path = ''
            #cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),3)
            #face detection saving
            #frame_path = 'static/frame_'+str(time.time())+'.jpg'
            #cv2.imwrite(frame_path,frame)
            #add_snapshot(frame_path)
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()
            yield(b'--frame\r\n'
                  b'Content-Type: iamge/jpeg\r\n\r\n' + frame + b'\r\n')
            
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(camera), mimetype='multipart/x-mixed-replace; boundary=frame') 

@app.route('/')
def index():
    capt_set = CaptureSettings()
    #ptp = PTPDeviceProps()
    return render_template('index.html',data=capt_set)

@app.route('/settings',methods=['POST'])
def change_settings():
    if request.method == 'POST':
        print(request.form)
        return redirect(url_for('index'))
    else:
        print('Method is not post')
        return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(port=80, host='0.0.0.0')