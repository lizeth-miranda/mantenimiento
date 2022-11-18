# -*- coding: utf-8 -*-
{
    'name': 'Mantenimiento Demsa',
    'version': '13.6',
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
        #'reports/Maintenance_report.xml',
        'reports/maintenance_reportv2.xml',
        'reports/report_equipment.xml',
        'reports/maintenance_equip.xml',
        # demo
        # views
        'views/maintenance.xml',
        'views/refacciones.xml',
        'views/product_template.xml',
        'views/equipos_sistemas.xml',
        #'views/maintenance_equipment.xml',
        
    ],
}
