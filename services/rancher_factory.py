from services.rancher_upgrade import RancherUpgrade

class RancherFactory(object):
	def __init__(self, command_type):
		self.command_type = command_type

	def factory(self):
		if self.command_type == "UPGRADE": return RancherUpgrade()
		raise ValueError('Command type not defined')