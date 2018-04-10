import yaml
import requests
from services.rancher_request import BaseRequest

class YamlGenerator(BaseRequest):

	def __init__(self, path):
		stream =  open(path, 'r')
		self.configuration = yaml.load(stream)
		self.object_to_yaml = {'apilist' : []}

	def gathering(self):
		apilist = []

		for index in range(len(self.configuration['service_list'])):
			service_id = self.configuration['service_list'][index]['service_id']
			environment = self.configuration['service_list'][index]['environment']
			name = self.configuration['service_list'][index]['name']
			list_instance_id = self.__get_service_instance_id(environment,service_id)

			for index in range(len(list_instance_id)):
				temp_dict = {'id' : list_instance_id[index] , 'machine' : environment, 'system' : "{0}_{1}".format(name,index+1) }
				apilist.append(temp_dict)

		self.object_to_yaml['apilist'] = apilist

	def generate(self):
		with open('./output/config.yaml', 'w') as yaml_file:
			yaml_file.write(yaml.dump(self.object_to_yaml,default_flow_style=False))

	def __get_service_instance_id(self,environment,service_id):

		r = requests.get('{0}:{1}/{2}/projects/{3}/services/{4}'.format(
				BaseRequest.RC_HOST, BaseRequest.RC_PORT,BaseRequest.RC_API_VERSION, 
				environment, service_id),
				auth=(BaseRequest.RC_ACCESS_KEY,BaseRequest.RC_SECRET_KEY))

		return r.json()['instanceIds']
