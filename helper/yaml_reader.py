import yaml
from model.rancher_server_config import RancherServerConfig

class YamlReader(object):
	
	def __init__(self, path):
		stream =  open(path, 'r')
		self.configuration = yaml.load(stream)
		self.server_object = self.__convert_to_obejct()

	def __convert_to_obejct(self):
		serverLits = []
		for index in range(len(self.configuration['service_list'])):
			server = RancherServerConfig()
			server.service_id = self.configuration['service_list'][index]['service_id']
			server.environment = self.configuration['service_list'][index]['environment']
			server.name = self.configuration['service_list'][index]['name']
			serverLits.append(server)
		return serverLits

	@property
	def server_object(self):
		return self.__server_object

	@server_object.setter
	def server_object(self, server_object):
		self.__server_object = server_object