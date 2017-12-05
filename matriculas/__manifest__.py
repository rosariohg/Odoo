# -*- coding: utf-8 -*-
{
    'name': "matriculas",

    'summary': """
        Permite realizar las matrículas en una Institucíón
        """,

    'description': """
        Este módulo permite realizar matrículas en una Institución.
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
        'views/areas.xml',
        'views/cursos.xml',
        'views/profesores.xml',
        'views/matriculas.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}