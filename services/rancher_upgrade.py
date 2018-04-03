from services.rancher_request import BaseRequest

class RancherUpgrade(BaseRequest):
	
	def get_service_config(self):
		print('get service config')