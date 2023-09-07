from flask import Flask, request, Response, url_for, redirect
from utils import get_status, get_device_info, get_vitals
import os, cv2, time, json, gphoto2 as gp
from webcam import gen_frames

app = Flask(__name__)

web_cam = cv2.VideoCapture(0)

@app.route('/')
def index():
	return "Server is alive"
	
@app.route('/request/capture/settings/<int:setting>')
def get_request(setting):

	try:
		from controls import CaptureSettings
		capt_set = CaptureSettings(setting)
		return json.dumps(capt_set.get_value_info())
	except gp.GPhoto2Error as err:
		return json.dumps({"error" : err, "message" : "an error has occured"})
		
@app.route('/videofeed')
def video_feed():
	return Response(gen_frames(web_cam), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/status/<req>')
def get_status(req):
	try:
		camera = gp.Camera()
		if req == 'vitals':
			return json.dumps(get_vitals(camera))
		elif req == 'info':
			return json.dumps(get_device_info(camera))
		else:
			return 'Wrong request parameters: Correct ways to address the API in this request are: <b>/status/vitals</b> or <b>/status/info</b>'	
	except gp.GPhoto2Error as err:
		return json.dumps({"error" : err, "message" : "an error has occured"})
		
@app.route('/capturephoto')
def capture_photo():
	try:
		camera = gp.Camera()
		photo = camera.capture(gp.GP_CAPTURE_IMAGE)
		dirpath = '/home/doxa/Documents/Python'
		pic_path = os.path.join(dirpath,photo.name)
		camera_file = camera.file_get(photo.folder,photo.name, gp.GP_FILE_TYPE_NORMAL)
		camera_file.save(pic_path)
		camera.exit()
		file_name = f'{time.time()}.jpg'
		new_path = os.path.join(dirpath, file_name)
		os.rename(pic_path, new_path)
		return json.dumps({"filename" : file_name, "filepath" : dirpath, "fullpath" : new_path})
		
	except gp.GPhoto2Error as err:
		return json.dumps({"error" : err, "message" : "an error has occured"})

@app.route('/set/<int:item>/<string:value>')
def change_settings(item,value):
	try:
		from controls import CaptureSettings
		if item and value:
			capt_set = CaptureSettings(item)
			result = capt_set.set_value(value)
			return json.dumps(result)
		else:
			return 'incorect url parameters'
	except gp.GPhoto2Error as err:
		return json.dumps({"error" : err, "message" : "an error has occured"})
		
if __name__ == '__main__':
	app.run(debug=True)
