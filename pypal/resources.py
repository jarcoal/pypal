import json
from http import PayPalSession
from pypal import API_BASE_URL, API_BASE_URL_SANDBOX


class AppIDResource(PayPalSession):
	"""
	Base resource for making requests against PayPal's AppID resources:
	- adaptive payments
	- adaptive accounts
	- permissions
	- invoice
	"""

	resource = None

	def __init__(self, *args, **kwargs):
		self.sandbox = kwargs.pop('sandbox', False)
		self.base_url = API_BASE_URL_SANDBOX if self.sandbox else API_BASE_URL

		super(AppIDResource, self).__init__(*args, **kwargs)

	def get_url(self, action):
		"""
		Builds a URL for a PayPal resource.
		"""
		return '/'.join([self.base_url, self.resource, action])

	def request(self, action, data, **kwargs):
		"""
		Execute a request to a PayPal AppID API.
		"""

		if 'requestEnvelope' not in data:
			data['requestEnvelope'] = { 'errorLanguage': 'en_US' }

		return super(AppIDResource, self).request('POST', self.get_url(action), data=json.dumps(data), **kwargs).json()