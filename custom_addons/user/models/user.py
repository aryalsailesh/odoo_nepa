from odoo import models, fields, api

class User(models.Model):
    _name = 'user.registration'
    _description = 'User Registration Form'
    website = fields.Boolean("Visible on the website", default=True)

    name = fields.Char(string='User Name', required=True)
    email = fields.Char(string='User Email', required=True)
    password = fields.Char(string='User Password', required=True)
    age = fields.Integer(string='User Age', required=True)
    phone = fields.Char(string='User Phone', required=True)


    def authenticate(self, email, password):
        user = self.env['user.registration'].sudo().search([('email','=',email),('password','=',password)])
        if user:
            return user
        else:
            return False