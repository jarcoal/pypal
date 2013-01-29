import requests


class PayPalSession(requests.Session):
	"""
	A Requests session with PayPal security headers.

	Parameters:

	`user_id` - PayPal security user ID
	`security_password` - PayPal security password
	`security_signature` - PayPal security signature
	`application_id` - PayPal application ID
	"""

	def __init__(self, user_id, security_password, security_signature, application_id):
		"""
		Apply the PayPal security headers
		"""

		super(PayPalSession, self).__init__()

		self.headers.update({
			'X-PAYPAL-SECURITY-USERID': user_id,
			'X-PAYPAL-SECURITY-PASSWORD': security_password,
			'X-PAYPAL-SECURITY-SIGNATURE': security_signature,
			'X-PAYPAL-APPLICATION-ID': application_id,
			'X-PAYPAL-REQUEST-DATA-FORMAT': 'JSON',
			'X-PAYPAL-RESPONSE-DATA-FORMAT': 'JSON',
		})