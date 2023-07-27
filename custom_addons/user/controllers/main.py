from odoo import http
from odoo.http import request


class UserRegistration(http.Controller):
    @http.route('/user/show/',website=True, auth='public')
    def user_registration(self, **kw):
        # return "Hello, user"
        user = request.env['user.registration'].sudo().search([])
        return request.render('user.registration_page',{
            "user":user
        })




    @http.route("/user/submit/", type="http", auth="public", website=True, csrf=False)
    def user_submit(self,**kw):
        # return "Hello, user"
        if request.httprequest.method == 'POST':

            request.env['user.registration'].sudo().create({
                'name': kw.get('name'),
                'email': kw.get('email'),
                'age': kw.get('age'),
                'phone': kw.get('phone')
            })
            return request.render('user.user_form_view',{
                'name': kw.get('name')
            })
        
        return request.render('user.user_form_view')

    