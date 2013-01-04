from pypal.resources import AppIDResource

class InvoiceResource(AppIDResource):
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