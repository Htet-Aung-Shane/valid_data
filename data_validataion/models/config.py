from odoo import models, fields, api, _


class Config(models.Model):
    _name = "config.data"

    name = fields.Char(string="Name")
    field = fields.Selection([('integer','Integer'),('string','String'),('datetime','Date Time'),('transfer','Transfered'),('null','Null')],string="Field", default='string')
    is_nuallable = fields.Boolean(string="Is Nullable")
    is_unique = fields.Boolean(string="Is Unique")
    allow_formula = fields.Boolean(string="Allow Formula")
    