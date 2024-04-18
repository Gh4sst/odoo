from odoo import fields, models, api

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Propiedad Inmobiliaria"
    _order = 'id desc'

    state = fields.Selection([
        ('draft', 'Borrador'),
        ('sold', 'Vendido'),
        ('cancelled', 'Cancelado')
    ], string="Estado", default='draft')
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    seller_id = fields.Many2one('res.users', string='Seller', default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')
    total_area = fields.Float(string='Total Area', compute='_compute_total_area')
    best_price = fields.Float(string="Best Price", compute="_compute_best_price")
    type_id = fields.Many2one("estate.property.type", string="Tipo de Propiedad")
    sequence = fields.Integer(string="Sequence")
    active = fields.Boolean(string="Active", default=True)
    leads_count = fields.Integer(string="Leads Count")
    name = fields.Char(string="Name")
    description = fields.Text(string="Descripción")
    postcode = fields.Char(string="Código Postal")
    date_availability = fields.Date(string="Fecha de Disponibilidad", default=lambda self: fields.Date.today())
    expected_price = fields.Float(string="Precio Esperado")
    selling_price = fields.Float(string="Precio de Venta", readonly=True)
    bedrooms = fields.Integer(string="Dormitorios", default=2)
    living_area = fields.Integer(string="Superficie Habitacional")
    facades = fields.Integer(string="Fachadas")
    garage = fields.Boolean(string="Garaje")
    garden = fields.Boolean(string="Jardín")
    garden_area = fields.Integer(string="Superficie de Jardín")
    garden_orientation = fields.Selection([
        ('north', 'Norte'),
        ('south', 'Sur'),
        ('east', 'Este'),
        ('west', 'Oeste')
    ], string="Orientación del Jardín")

    _sql_constraints = [
        ('check_expected_price_positive', 'CHECK(expected_price > 0)', 'El precio esperado debe ser estrictamente positivo.')
    ]

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for property in self:
            property.total_area = property.living_area + property.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for property in self:
            property.best_price = max(property.offer_ids.mapped('price')) if property.offer_ids else 0.0

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10.0
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0.0
            self.garden_orientation = False

    def action_cancel(self):
        self.filtered(lambda prop: prop.state == 'draft').write({'state': 'cancelled'})

    def action_set_sold(self):
        self.filtered(lambda prop: prop.state == 'draft').write({'state': 'sold'})

    def _check_property_deletion(self):
        self.filtered(lambda prop: prop.state not in ('new', 'cancelled')).raise_user_error("No se puede eliminar una propiedad si su estado no es 'nuevo' o 'cancelado'")

