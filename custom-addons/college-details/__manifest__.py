# -*- coding: utf-8 -*-
{
    'name': "College Details Management",

    'summary': "Manage student details with PDF reports and sales integration",

    'description': """
This module allows you to:
- Add student details from dedicated app interface
- Generate professional PDF reports for student information
- Link student records to sales quotations
- Manage comprehensive student data including personal and academic information
    """,

    'author': "Your Company",
    'website': "https://www.yourcompany.com",

    'category': 'Education',
    'version': '1.0',
    'installable': True,
    'application': True,

    'depends': ['base', 'sale_management'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'reports/student_details_report.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
