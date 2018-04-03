class BaseRequest(object):

	# THIS KEY DEPEND ON YOUR RANCHER API KEY
	RC_ACCESS_KEY = 'XXX'
	RC_SECRET_KEY = 'XXX'

	def get_request(self):
		print('THIS IS GET REQUEST')

	def post_request(self):
		print('THIS IS POST REQUEST')