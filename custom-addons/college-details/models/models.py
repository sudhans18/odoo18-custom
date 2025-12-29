# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StudentDetails(models.Model):
    _name = 'student.details'
    _description = 'Student Details'
    _order = 'create_date desc'

    name = fields.Char(string='Student Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone Number')
    course = fields.Char(string='Course', required=True)
    address = fields.Text(string='Address')
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    quotation_id = fields.Many2one('sale.order', string='Quotation Reference')
    notes = fields.Text(string='Additional Notes')

    def action_generate_pdf(self):
        """Generate PDF report for student details"""
        return self.env.ref('college-details.action_report_student_details').report_action(self)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_create_student_details(self):
        """Open student details form with current quotation pre-filled"""
        action = {
            'name': 'Create Student Details',
            'type': 'ir.actions.act_window',
            'res_model': 'student.details',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_quotation_id': self.id,
            }
        }
        return action
