{
    'name': "Fleet: Regcheck",
    'summary': "A module to access vehicle information using registration number",
    'description': "This module allows you to access vehicle information using registration number",
    'author': "Your Name",
    'category': 'Fleet',
    'version': '14.0.1',
    'depends': ['base', 'website', 'fleet_reg_common'],
    'data': [
       'security/ir.model.access.csv',
    
    #    'views/snippets/register.xml',
         'views/templates.xml',
         'views/vehicle_information.xml',
         'views/res_config_settings_view.xml',
        #  'static/src/img/plate_number.png',
         #'views/snippets/snippets.xml',
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
