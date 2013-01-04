from pypal.resources import AppIDResource

class AdaptiveAccountsResource(AppIDResource):
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