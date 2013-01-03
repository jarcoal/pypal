from pypal import AppIDResource

class AdaptiveAccountsResource(AppIDResource):
	resource = 'AdaptiveAccounts'

	def add_bank_account(self, **kwargs):
		return self.request('AddBankAccount', **kwargs)

	def add_payment_card(self, **kwargs):
		return self.request('AddPaymentCard', **kwargs)

	def create_account(self, **kwargs):
		return self.request('CreateAccount', **kwargs)

	def get_user_agreement(self, **kwargs):
		return self.request('GetUserAgreement', **kwargs)

	def set_funding_source_confirmed(self, **kwargs):
		return self.request('SetFundingSourceConfirmed', **kwargs)