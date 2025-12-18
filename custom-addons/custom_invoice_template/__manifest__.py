{
    "name": "Custom Invoice Template",
    "version": "1.0.0",
    "summary": "Replaces the standard invoice PDF with a custom layout.",
    "description": "Overrides the default account invoice report to match the requested tax invoice layout.",
    "license": "LGPL-3",
    "author": "Sudhan S",
    "depends": ["account"],
    "data": [
        "reports/report_invoice.xml",
        "reports/report_invoice_action.xml",
        "views/account_move_view.xml",
    ],
    "assets": {},
    "installable": True,
    "application": False,
}
