from pypal import AppIDResource

class PermissionsResource(AppIDResource):
	url = 'https://svcs.paypal.com/Permissions/'
	url_debug = 'https://svcs.sandbox.paypal.com/Permissions/'

	def cancel_permissions(self, **kwargs):
		return self.request('CancelPermissions', **kwargs)

	def get_access_token(self, **kwargs):
		return self.request('GetAccessToken', **kwargs)

	def get_advanced_personal_data(self, **kwargs):
		return self.request('GetAdvancedPersonalData', **kwargs)

	def get_basic_personal_data(self, **kwargs):
		return self.request('GetBasicPersonalData', **kwargs)

	def get_permissions(self, **kwargs):
		return self.request('GetPermissions', **kwargs)

	def request_permissions(self, **kwargs):
		return self.request('RequestPermissions', **kwargs)