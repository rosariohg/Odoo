# -*- coding: utf-8 -*-
{
    'name': "convalidaciones",

    'summary': """
        Permite Gestionar las convalidaciones en un Instituto""",

    'description': """
        Este módulo permite gestionar las convalidaciones de un Centro Educativo
    """,

    'author': "Rosario Huanca",
    'website': "http://www.rosariohg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/alumnos.xml',
        'views/modulos.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
     #   'demo/demo.xml',
    #],
}