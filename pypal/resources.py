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

class AdaptiveAccountsResource(AppIDResource):
	"""
	Resource for working with Adaptive Accounts
	"""

	resource = 'AdaptiveAccounts'

	def add_bank_account(self, **data):
		return self.request('AddBankAccount', data)

	def add_payment_card(self, **data):
		return self.request('AddPaymentCard', data)

	def create_account(self, **data):
		return self.request('CreateAccount', data)

	def get_user_agreement(self, **data):
		return self.request('GetUserAgreement', data)

	def set_funding_source_confirmed(self, **data):
		return self.request('SetFundingSourceConfirmed', data)

class AdaptivePaymentsResource(AppIDResource):
	"""
	Resource for working with Adaptive Payments
	"""

	resource = 'AdaptivePayments'

	def pay(self, **data):
		return self.request('Pay', data)

	def payment_details(self, **data):
		return self.request('PaymentDetails', data)

	def refund(self, **data):
		return self.request('Refund', data)

	def preapproval(self, **data):
		return self.request('Preapproval', data)

	def preapproval_details(self, **data):
		return self.request('PreapprovalDetails', data)

class InvoiceResource(AppIDResource):
	"""
	Resource for working with Invoicing
	"""

	resource = 'Invoice'

	def cancel_invoice(self, **data):
		return self.request('CancelInvoice', data)

	def create_and_send_invoice(self, **data):
		return self.request('CreateAndSendInvoice', data)

	def create_invoice(self, **data):
		return self.request('CreateInvoice', data)

	def get_invoice_details(self, **data):
		return self.request('GetInvoiceDetails', data)

	def mark_invoice_as_paid(self, **data):
		return self.request('MarkInvoiceAsPaid', data)

	def mark_invoice_as_refunded(self, **data):
		return self.request('MarkInvoiceAsRefunded', data)

	def mark_invoice_as_unpaid(self, **data):
		return self.request('MarkInvoiceAsUnpaid', data)

	def search_invoices(self, **data):
		return self.request('SearchInvoices', data)

	def send_invoice(self, **data):
		return self.request('SendInvoice', data)

	def update_invoice(self, **data):
		return self.request('UpdateInvoice', data)

class PermissionsResource(AppIDResource):
	"""
	Resource for working with Permissions
	"""

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