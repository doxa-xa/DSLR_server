import cv2, numpy as np, datetime as time
from controls import capture_image

def mse(imgA,imgB):
    height,width = imgA.shape
    differance = cv2.subtract(imgA,imgB)
    error = np.sum(differance**2)
    mean_sq_err = error/(float(height*width))
    return mean_sq_err

def gen_frames(camera,sensitivity):
    ret, pframe = camera.read()
    curr_err = []
    curr_err.append(0.0)
    if not sensitivity:
         sensitivity = 3 
    if not camera.isOpened():
        camera = cv2.VideoCapture(0)
    while True:
        previous_frame = pframe[:]
        success, frame = camera.read()
        if not success:
            break
        else:
            current = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            previous = cv2.cvtColor(previous_frame,cv2.COLOR_BGR2GRAY)
            error = mse(current,previous)
            curr_err.append(error)
            if curr_err is not None and curr_err[-2] - error > sensitivity:
                    print(f'time: {time.datetime.now()} object detected')
                    capture_image()
            ret, buffer = cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()
            yield(b'--frame\r\n'
                  b'Content-Type: iamge/jpeg\r\n\r\n' + frame + b'\r\n')
            
