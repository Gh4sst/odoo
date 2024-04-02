from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "el modulo funciona correctamente"

    active=fields.Boolean(string="active",default=True)
    leads_count = fields.Integer(string="Leads Count")
    name = fields.Char(string="Name")
    description = fields.Text(string="Descripcion")
    postcode = fields.Char(string="postcode")
    date_availability = fields.Date(string="Availability Date", default=lambda self: fields.Date.today())
    expected_price = fields.Float(string="Expected Price")
    selling_price = fields.Float(string="Selling Price",readonly=True)
    bedrooms = fields.Integer(string="Bedrooms",default=2)
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string="Garden Orientation")
    state=fields.Selection([
        ('New','Nuevo'),
        ('offer_received','Oferta recibida'),
        ('offer_acepted','Oferta aceptada'),
        ('sold','Vendido'),
        ('cancelled','Cancelado')
    ],string="Estado",required=True,copy=False,default='New')
