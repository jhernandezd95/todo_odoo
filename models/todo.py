from odoo import models,fields


class Todo(models.Model):
    _name = "todo"

    name = fields.Char("Nombre")
    status = fields.Selection(selection=[
        ("finalization", "Finalization"),
        ("Pendent", "Pendent"),
        ("on_process", "On process")
    ])
