from odoo import models, fields

class HREmployeeInherit(models.Model):
    _inherit = 'hr.employee'

    team_id = fields.Many2one('team.resource', string="Team")

