from odoo import models, fields

class TeamResource(models.Model):
    _inherit = 'resource.resource'  
    _name = 'team.resource'
    _description = 'Team Resource'

    name = fields.Char(string="Name", required=True)
    employee_ids = fields.One2many('hr.employee', 'team_id', string="Employees")
