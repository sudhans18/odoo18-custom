# -*- coding: utf-8 -*-
{
    'name': "College Details Management",

    'summary': "Manage student details with PDF reports and sales integration",

    'description': """
This module allows you to:
- Add student details from quotation pages
- Generate professional PDF reports for student information
- Link student records to sales quotations
- Manage comprehensive student data including personal and academic information
    """,

    'author': "Your Company",
    'website': "https://www.yourcompany.com",

    'category': 'Education',
    'version': '1.0',
    'installable': True,
    'application': False,

    'depends': ['base', 'sale_management'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/sale_order_inherit.xml',
        'reports/student_details_report.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
