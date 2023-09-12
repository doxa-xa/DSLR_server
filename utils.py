
#file is used by the server to fetch the current DSLR and it vitals
try:
	import gphoto2 as gp
except ImportError as err:
	print('Working on windows ... no Gphoto2')

camera = gp.Camera()

#get all DSLR current settings
def get_status(camera):
	context = gp.Context()
	config_major = camera.get_config(context)
	status = config_major.get_child(2)
	status_items = status.count_children()
	result = {}
	for i in range(status_items):
		result.update( { status.get_child(i).get_name() : status.get_child(i).get_value(), "readonly": status.get_child(i).get_readonly() } )
	return result

#print(get_status(camera))

def get_device_info(camera):
	context = gp.Context()
	config_major = camera.get_config(context)
	status = config_major.get_child(2)
	serial_number = status.get_child(0).get_value()
	brand = status.get_child(1).get_value()
	model = status.get_child(2).get_value()
	version = status.get_child(3).get_value()

	result = {
		"brand":brand,
		"model":model,
		"serial number":serial_number,
		"version":version
	}
	return result

#print(get_device_info(camera))

def get_vitals(camera):
	context = gp.Context()
	config_major = camera.get_config(context)
	status = config_major.get_child(2)
	ac_power = status.get_child(5).get_value()
	battery_lvl = status.get_child(7).get_value()
	storage = status.get_child(14).get_value()
	
	return { "charging" : ac_power, "battery" : battery_lvl, "remainigstorage" : storage}

#print(get_vitals(camera))

class CapturePhotoResponse:
	def __init__(self,filename,filepath,fullpath):
		self.filename = filename
		self.filepath = filepath
		self.fullpath = fullpath
