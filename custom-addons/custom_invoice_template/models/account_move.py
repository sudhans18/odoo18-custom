from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def action_print_custom_invoice(self):
        """Return the custom PDF report action for the selected invoices."""
        action = self.env.ref(
            "custom_invoice_template.action_report_invoice_document_custom_full"
        ).with_context(print_with_payments=True)
        return action.report_action(self)
