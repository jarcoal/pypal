import requests, json
from pypal import API_BASE_URL, API_BASE_URL_DEBUG


class AppIDResource(object):
	"""
	Base resource for making requests against PayPal's AppID resources:
	- adaptive payments
	- adaptive accounts
	- permissions
	- invoice
	"""

	resource = None

	def __init__(self, user_id, security_password, security_signature, application_id, debug=False):
		self.debug = debug

		self.headers = {
			'X-PAYPAL-SECURITY-USERID': user_id,
			'X-PAYPAL-SECURITY-PASSWORD': security_password,
			'X-PAYPAL-SECURITY-SIGNATURE': security_signature,
			'X-PAYPAL-APPLICATION-ID': application_id,
			'X-PAYPAL-REQUEST-DATA-FORMAT': 'JSON',
			'X-PAYPAL-RESPONSE-DATA-FORMAT': 'JSON',
		}

	def get_url(self, action):
		return '/'.join([API_BASE_URL_DEBUG if self.debug else API_BASE_URL, self.resource, action])

	def request(self, action, data):
		"""
		Makes an authorized POST request to PayPal
		"""

		if 'request_envelope' not in data:
			data['request_envelope'] = { 'requestEnvelope': { 'errorLanguage': 'en_US' } };

		req = requests.post(self.get_url(action), data=json.dumps(data), headers=self.headers)
		return req.json()