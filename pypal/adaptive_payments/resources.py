from pypal.resources import AppIDResource

class AdaptivePaymentsResource(AppIDResource):
	resource = 'AdaptivePayments'

	def pay(self, **kwargs):
		return self.request('Pay', **kwargs)

	def payment_details(self, **kwargs):
		return self.request('PaymentDetails', **kwargs)

	def refund(self, **kwargs):
		return self.request('Refund', **kwargs)

	def preapproval(self, **kwargs):
		return self.request('Preapproval', **kwargs)

	def preapproval_details(self, **kwargs):
		return self.request('PreapprovalDetails', **kwargs)