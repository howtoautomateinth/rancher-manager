class BaseRequest(object):

	# THIS KEY DEPEND ON YOUR RANCHER API KEY
	RC_ACCESS_KEY = 'XXX'
	RC_SECRET_KEY = 'XXX'
	HEADERS = {'content-type':'application/json'}
	RC_HOST = 'http://XXX'
	RC_PORT = '8080'
	RC_API_VERSION = 'v2-beta'

	def get_request(self):
		print('THIS IS GET REQUEST')

	def post_request(self):
		print('THIS IS POST REQUEST')