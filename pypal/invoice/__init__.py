from pypal import AppIDResource

class InvoiceResource(AppIDResource):
	resource = 'Invoice'

	def cancel_invoice(self, **kwargs):
		return self.request('CancelInvoice', **kwargs)

	def create_and_send_invoice(self, **kwargs):
		return self.request('CreateAndSendInvoice', **kwargs)

	def create_invoice(self, **kwargs):
		return self.request('CreateInvoice', **kwargs)

	def get_invoice_details(self, **kwargs):
		return self.request('GetInvoiceDetails', **kwargs)

	def mark_invoice_as_paid(self, **kwargs):
		return self.request('MarkInvoiceAsPaid', **kwargs)

	def mark_invoice_as_refunded(self, **kwargs):
		return self.request('MarkInvoiceAsRefunded', **kwargs)

	def mark_invoice_as_unpaid(self, **kwargs):
		return self.request('MarkInvoiceAsUnpaid', **kwargs)

	def search_invoices(self, **kwargs):
		return self.request('SearchInvoices', **kwargs)

	def send_invoice(self, **kwargs):
		return self.request('SendInvoice', **kwargs)

	def update_invoice(self, **kwargs):
		return self.request('UpdateInvoice', **kwargs)