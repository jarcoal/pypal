import requests, json
from urllib import urlencode


class AppIDResource(object):
	"""
	Base resource for making requests against PayPal's AppID resources:
	- adaptive payments
	- adaptive accounts
	- permissions
	- invoice
	"""

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

	def get_url(self, resource):
		return (self.url if not self.debug else self.url_debug) + resource

	def request(self, resource, data):
		"""
		Makes an authorized POST request to PayPal
		"""
		req = requests.post(self.get_url(resource), data=urlencode(json.dumps(data)), headers=self.headers)
		return req.json()