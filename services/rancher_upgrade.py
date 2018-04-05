from services.rancher_request import BaseRequest
import requests
import time
import json

class RancherUpgrade(BaseRequest):

	def __init__(self,config):
		self.config = config
		self.launchConfig = None

	def upgrade(self):
		self.__get_service_config()

	def __get_service_config(self):
		print('Getting service configuration')
		for data in self.config:
			r = requests.get('{0}:{1}/{2}/projects/{3}/services/{4}'.format(
					self.RC_HOST, self.RC_PORT,self.RC_API_VERSION, 
					data.environment, data.service_id),
					auth=(self.RC_ACCESS_KEY,self.RC_SECRET_KEY))
			self.launchConfig = r.json()['launchConfig']
			self.__upgrade_services(data.environment, data.service_id)

	def __upgrade_services(self,environment,service_id):
		print('Upgrading service configuration')
		payload = {
			'inServiceStrategy': {
				'batchSize': 1,
				'intervalMillis': 2000,
				'startFirst': False,
				'launchConfig': self.launchConfig
			}
		}
		r = requests.post('{0}:{1}/{2}/projects/{3}/services/{4}/?action=upgrade'.format(
				self.RC_HOST, self.RC_PORT,self.RC_API_VERSION, 
				environment,service_id),
				data = json.dumps(payload), headers = self.HEADERS,
				auth=(self.RC_ACCESS_KEY,self.RC_SECRET_KEY))
		self.__check_state(environment,service_id)

	def __check_state(self,environment,service_id):
		print('Check service state')
		state = 'upgrading'
		retry = 10
		sleep = 30

		while (state != 'upgraded'):
			time.sleep(sleep)
			r = requests.get('{0}:{1}/{2}/projects/{3}/services/{4}'.format(
					self.RC_HOST, self.RC_PORT,self.RC_API_VERSION, 
					environment, service_id),
					auth=(self.RC_ACCESS_KEY,self.RC_SECRET_KEY))
			state = r.json()['state']
			retry -= 1
			print('Current State "{}" and retry count "{}"'.format(state,retry))
			if (retry <= 0): break

		print('Posting "finishupgrade" to Rancher Server')
		r = requests.post('{0}:{1}/{2}/projects/{3}/services/{4}/?action=finishupgrade'.format(
				self.RC_HOST, self.RC_PORT,self.RC_API_VERSION, 
				environment,service_id),
				auth=(self.RC_ACCESS_KEY,self.RC_SECRET_KEY))

