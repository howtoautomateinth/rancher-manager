from services.rancher_upgrade import RancherUpgrade

class RancherFactory(object):
	
	def __init__(self, command_type, config):
		self.command_type = command_type
		self.config = config

	def factory(self):
		if self.command_type == "UPGRADE": return RancherUpgrade(self.config)
		raise ValueError('Command type not defined')