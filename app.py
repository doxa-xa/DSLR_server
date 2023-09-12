from flask import Flask, request, Response, url_for, redirect, render_template
from utils import get_status, get_device_info, get_vitals
import os, cv2, time, json 
try:
	import gphoto2 as gp
except ImportError as err:
	print('Working on windows.. no GPhoto2')
from motion_detection import motion_detection
from snap import capture

app = Flask(__name__)

web_cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

@app.route('/')
def index():
	try:
		camera = gp.Camera()
		camera.init()
		device_info = get_device_info(camera)
		vitals = get_vitals(camera)
		result = {"vitals":vitals, "device_info":device_info}
	except ImportError:
		device_info = None
		vitals = None
		return redirect(url_for('404'))
	return render_template('index.html', device=result)
	
@app.route('/request/capture/settings/<int:setting>')
def get_request(setting):

	try:
		from controls import CaptureSettings
		capt_set = CaptureSettings(setting)
		return json.dumps(capt_set.get_value_info())
	except gp.GPhoto2Error as err:
		return json.dumps({"error" : str(err), "message" : "an error has occured"})
		
@app.route('/videofeed')
def video_feed():
	return Response(motion_detection(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/photos')
def photos():
	return render_template('photos.html')

@app.route('/currentsettings')
def current_settings():
	try:
		camera = gp.Camera()
		camera.init()
		result = get_status(camera)
	except ImportError:
		result = {"error": "You cannot use GPhoto2 under windows"}
	return render_template('currentsettings.html',settings = result)

@app.route('/status/<req>')
def get_status(req):
	try:
		camera = gp.Camera()
    #camera.init()
		if req == 'vitals':
			return json.dumps(get_vitals(camera))
		elif req == 'info':
			return json.dumps(get_device_info(camera))
		else:
			return 'Wrong request parameters: Correct ways to address the API in this request are: <b>/status/vitals</b> or <b>/status/info</b>'	
	except gp.GPhoto2Error as err:
		return json.dumps({"error" : str(err), "message" : "an error has occured"})
		
@app.route('/capturephoto')
def capture_photo():
  capture()

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
		return json.dumps({"error" : str(err), "message" : "an error has occured"})
	
@app.route('/404')
def end_404():
	return render_template('404.html')	
		
if __name__ == '__main__':
	app.run(debug=True)
