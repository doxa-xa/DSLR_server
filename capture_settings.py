class CaptureSettings:
	movie_resolution = '1920x1080; 30p'
	def set_movie_resolution(self,quality):
		self.movie_resolution = quality
	
	movie_quality = 'High'
	def set_movie_quality(self,quality):
		self.movie_quality = quality
	
	exp_program = 'M'
	def set_exposure_program(self,exp):
		self.exp_program = exp
	
	min_shutter_speed = 'Auto'
	def set_min_shutter_speed(self,speed):
		self.min_shutter_speed = speed
	
	shooting_speed = '5 fps'
	def set_shooting_speed(self,sh_sp):
		self.shooting_speed = sp
	
	iso_auto_hi_lim = 6400
	def set_iso_auto_hi_limit(self,ahl):
		self.iso_auto_hi_lim = ahl
	
	focus_metering = 'Single Area'
	def set_focus_metering(self,fm):
		self.focus_metering = fm
	
	d_lighting = 'Auto'
	def set_d_lighing(self,d_light):
		self.d_lighing = d_light
	
	high_iso_noise_reduct = 'High'
	def set_high_iso_noise_reduct(self,hisonr):
		self.high_iso_noise_reduct = hisonr
		
	raw_compression = 'Lossless'
	def set_raw_compression(self,raw_comp):
		self.raw_compression = raw_comp
	
	flash_shutter_speed = '1/60s'
	def set_flash_shutter_speed(self,flash_shut_speed):
		self.flash_shutter_speed = flash_shut_speed
	
	live_view_size = 'VGA'
	def set_live_view_size(self,lvs):
		self.live_view_size = lvs
