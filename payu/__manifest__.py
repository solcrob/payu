# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'PayU',
    'category': 'Payment Acquirer',
    'summary': 'Payment Acquirer: PayU Implementation',
    'description': """
    PayU for Europe.

    PayU payment gateway supports in CZK currency.
    """,
    'depends': ['payment'],
    'data': [
        'views/payment_views.xml',
        'views/payment_payumoney_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
    'post_init_hook': 'create_missing_journal_for_acquirers',
}
