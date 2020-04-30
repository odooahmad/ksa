# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Saudi Arabia GOSI Contribution',
    'version': '12.0',
    'category': 'Payroll',
    'summary': 'Calculate GOSI Contribution for Saudi Government From Employee and Company',
    'description': "Calculate GOSI Contribution (Employee/Company),Employee Allowances and Deductions",
    'author': 'Ahmad',
    'depends': ['hr', 'hr_payroll'],
    'data': [
        'views/hr_payroll_add_view.xml',
    ],

    'images': ["static/description/icon.png"],
    'license': "AGPL-3",
    'price':'148',
    'currency':'USD',
    'installable': True,
    'auto_install': False,
}