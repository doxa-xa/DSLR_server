import os.path as path , os,datetime as dt
import gphoto2 as gp

def capture():
	camera = gp.Camera()
	camera.init()
	print('Capture image')
	file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
	print(f'Camera file path: {file_path.folder}/{file_path.name}')
	target = path.join(f'{path.abspath(path.curdir)}/static',file_path.name)
	print(f'Copying image to {target}')
	now = dt.datetime.now().strftime("%d%m%Y_%H%M%S%p")
	camera_file = camera.file_get(file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
	camera_file.save(target)
	os.rename(target,f'{now}.jpg')
	camera.exit()

#capture()
