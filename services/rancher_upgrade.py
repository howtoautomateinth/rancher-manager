from services.rancher_request import BaseRequest

class RancherUpgrade(BaseRequest):

	def __init__(self,config):
		self.config = config
	
	def get_service_config(self):
		for data in self.config:
			print(data.service_id)
			print(data.environment)
			print(data.name)