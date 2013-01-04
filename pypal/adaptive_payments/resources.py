from pypal.resources import AppIDResource

class AdaptivePaymentsResource(AppIDResource):
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