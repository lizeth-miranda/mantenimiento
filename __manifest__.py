# -*- coding: utf-8 -*-
{
    'name': 'Mantenimiento Demsa',
    'version': '13.5',
    'author': 'Demsa',
    'website': '',
    'depends': [
        'maintenance',
    ],
    'data': [
        # security
        'security/groupsRefa.xml',
        'security/equipos_mante.xml',
        'security/ir.model.access.csv',
        # data
        'data/sequence.xml',
        # wizards
        # reports
        'reports/report.xml',
        'reports/Maintenance_report.xml',
        # demo
        # views
        'views/maintenance.xml',
        'views/refacciones.xml',
        'views/product_template.xml',
        'views/equipos_sistemas.xml',
    ],
}
