# -*- coding: utf-8 -*-
{
    'name': "dimensions_in_sale_order_line",
    'summary': "Dimensions in Sale Order Linee",
    'description': """
        This module adds dimensions fields in sale order lines.
    """,
    'author': "Edoardo Soloperto",
    'license': 'AGPL-3',
    'category': 'Sales',
    'version': '0.1',
    'depends': ['sale'],
    'data': [
        'views/sale_order_view.xml',
        # 'report/sale_order_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}