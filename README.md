#pypal
###PayPal API bindings for Python

----

pypal is a set of resources that make it easy to work with PayPal's "AppID" APIs, which are the following:

* [Adaptive Payments](https://www.x.com/developers/paypal/products/adaptive-payments)
* [Adaptive Accounts](https://www.x.com/developers/paypal/products/adaptive-accounts)
* [Permissions](https://www.x.com/developers/paypal/products/permissions)
* [Invoicing](https://www.x.com/developers/paypal/products/invoicing)

If you peek at the source you'll find this is just a bunch of classes that inherit from python-requests [Session](http://docs.python-requests.org/en/latest/user/advanced/#session-objects) ([source](https://github.com/kennethreitz/requests/blob/master/requests/sessions.py#LC142)), and provide some convenience methods for calling PayPal URLs.

##Install

----

```python
pip install pypal
```

##Use

----

###pypal.AdaptiveAccountsResource(user_id, security_password, security_signature, application_id, sandbox=False)

####.add_bank_account(**parameters)
####.add_payment_card(**parameters)
####.create_account(**parameters)
####.get_user_agreement(**parameters)
####.set_funding_source_confirmed(**parameters)


###pypal.AdaptivePaymentsResource(user_id, security_password, security_signature, application_id, sandbox=False)

####.pay(**parameters)
####.payment_details(**parameters)
####.refund(**parameters)
####.preapproval(**parameters)
####.preapproval_details(**parameters)


###pypal.InvoiceResource(user_id, security_password, security_signature, application_id, sandbox=False)

####.cancel_invoice(**parameters)
####.create_and_send_invoice(**parameters)
####.create_invoice(**parameters)
####.get_invoice_details(**parameters)
####.mark_invoice_as_paid(**parameters)
####.mark_invoice_as_refunded(**parameters)
####.mark_invoice_as_unpaid(**parameters)
####.search_invoices(**parameters)
####.send_invoice(**parameters)
####.update_invoice(**parameters)


###pypal.PermissionsResource(user_id, security_password, security_signature, application_id, sandbox=False)

####.cancel_permissions(**parameters)
####.get_access_token(**parameters)
####.get_advanced_personal_data(**parameters)
####.get_basic_personal_data(**parameters)
####.get_permissions(**parameters)
####.request_permissions(**parameters)


###pypal.http.PayPalSession(user_id, security_password, security_signature, application_id)

You probably won't need to use this on it's own, but all resources inherit from it, so they also require the above parameters.  All requests made with instances of PayPalSession will be sent with the appropriate [PayPal authorization headers](https://www.x.com/developers/paypal/documentation-tools/quick-start-guides/paypal-apis-getting-started-guide#headers).


###pypal.resources.AppIDResource(user_id, security_password, security_signature, application_id, sandbox=False)

Base resource class.  You also won't use this directly.