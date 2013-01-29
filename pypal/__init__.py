#
# Base URLs for PayPal AppID APIs
#

API_BASE_URL = 'https://svcs.paypal.com'
API_BASE_URL_SANDBOX = 'https://svcs.sandbox.paypal.com'

from adaptive_accounts.resources import AdaptiveAccountsResource
from adaptive_payments.resources import AdaptivePaymentsResource
from invoice.resources import InvoiceResource
from permissions.resources import PermissionsResource