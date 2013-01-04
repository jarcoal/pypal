from pypal.resources import AppIDResource

class PermissionsResource(AppIDResource):
	resource = 'Permissions'

	def cancel_permissions(self, **data):
		return self.request('CancelPermissions', data)

	def get_access_token(self, **data):
		return self.request('GetAccessToken', data)

	def get_advanced_personal_data(self, **data):
		return self.request('GetAdvancedPersonalData', data)

	def get_basic_personal_data(self, **data):
		return self.request('GetBasicPersonalData', data)

	def get_permissions(self, **data):
		return self.request('GetPermissions', data)

	def request_permissions(self, **data):
		return self.request('RequestPermissions', data)