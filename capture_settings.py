class CaptureSettings:
	f_number = 'f/9'
	f_num_range = ["f/5.6","f/6.3","f/7.1","f/8","f/9","f/10","f/11","f/13","f/14","f/16","f/18","f/20","f/22","f/25"]
	
	def get_f_number(self):
		return self.f_number
	
	def set_f_number(self,fnum):
		for num in self.f_num_range:
			if fnum == num:
				self.f_number = fnum
	
	iso_speed = '160'
	iso_speed_range = ["100","125","160","200","250","320","400","500","640","800","1000","1250","1600","2000","2500","3200","4000","5000","6400"]

	def get_iso_speed(self):
		return self.iso_speed
	
	def set_iso_speed(self,iso_sp):
		for num in self.iso_speed_range:
			if num == iso_sp:
				self.iso_speed = iso_sp
	
	exp_compensation = "0"
	exp_comp_range = ["-5","-4.666","-4.333","-4","-3.666","-3.333","-3","-2.666","-2.333","-2","-1.666","-1.333","-1","-0.666","-0.333","0","0.333","0.666","1","1.333","1.666","2","2.333","2.666","3","3.333","3.666","4","4.333","4.666","5"]

	def get_exp_compensation(self):
		return self.exp_compensation
	
	def set_exp_compensation(self,exp_comp):
		for num in self.exp_comp_range:
			if num == exp_comp:
				self.exp_compensation = exp_comp
	
	shutter_speed = '0.0062s'
	shutter_speed_range = [
      "Bad Speed",
      "0.0001s",
      "0.0002s",
      "0.0003s",
      "0.0004s",
      "0.0005s",
      "0.0006s",
      "0.0008s",
      "0.0010s",
      "0.0012s",
      "0.0015s",
      "0.0020s",
      "0.0025s",
      "0.0031s",
      "0.0040s",
      "0.0050s",
      "0.0062s",
      "0.0080s",
      "0.0100s",
      "0.0125s",
      "0.0166s",
      "0.0200s",
      "0.0250s",
      "0.0333s",
      "0.0400s",
      "0.0500s",
      "0.0666s"
     ]
	
	def get_shutter_speed(self):
		return self.shutter_speed
	
	def set_shutter_speed(self,shut_sp):
		for num in self.shutter_speed_range:
			if num == shut_sp:
				self.shutter_speed = shut_sp

	fraction_shutter_speed = '1/160'
	fract_shut_sp_range = [
        "Bad Speed",
        "1/6400",
        "1/4000",
        "1/3200",
        "1/2500",
        "1/2000",
        "1/1600",
        "1/1250",
        "1/1000",
        "1/800",
        "1/640",
        "1/500",
        "1/400",
        "1/320",
        "1/250",
        "1/200",
        "1/160",
        "1/125",
        "1/100",
        "1/80",
        "1/60",
        "1/50",
        "1/40",
        "1/30",
        "1/25",
        "1/20",
        "1/15"
        ]
	
	def get_fraction_shutter_speed(self):
		return self.fraction_shutter_speed
	
	def set_fraction_shutter_speed(self,fr_shut_sp):
		for num in self.fract_shut_sp_range:
			if num == fr_shut_sp:
				self.fraction_shutter_speed = fr_shut_sp

	auto_iso = 'On'

	def get_auto_iso(self):
		return self.auto_iso
	
	def set_auto_iso(self,autoiso):
		self.auto_iso = autoiso
	
	iso_auto_hi_limit = '6400'
	iso_auto_hi_lim_range = [
      "400",
      "800",
      "1600",
      "3200",
      "6400",
      "Hi 1"
     ]
	
	def get_iso_auto_hi_limit(self):
		return self.iso_auto_hi_limit
	
	def set_iso_auto_hi_limit(self,iso_ahlim):
		for num in self.iso_auto_hi_lim_range:
			if num == iso_ahlim:
				self.iso_auto_hi_limit = iso_ahlim

	white_balance = 'Automatic'
	white_balance_range = [
            "Automatic", 
            "Daylight", 
            "Fluorescent", 
            "Tungsten", 
            "Tungsten",
            "Flash",
            "Cloudy",
            "Shade",
            "Color Temperature",
            "Preset"
        ]
	battery_level = '80'
	
	def get_battery_level(self):
		return self.battery_level
	
	storage = {
		'free':'1543Mb',
		'capacity':'32Gb'
	}
	
	def get_storage(self):
		return self.storage

	def get_white_balance(self):
		return self.white_balance
	
	def set_white_balance(self,wb):
		for num in self.white_balance_range:
			if num == wb:
				self.white_balance = wb

	def get_white_balance_range(self):
		return self.white_balance_range
	
	def get_iso_auto_hi_range(self):
		return self.iso_auto_hi_lim_range
	
	def get_fraction_shutter_speed_range(self):
		return self.fract_shut_sp_range
	
	def get_shutter_speed_range(self):
		return self.shutter_speed_range
	
	def get_exposure_compensation_range(self):
		return self.exp_comp_range
	
	def get_iso_speed_range(self):
		return self.iso_speed_range
	
	def get_f_number_range(self):
		return self.f_num_range