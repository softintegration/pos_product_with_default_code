# -*- coding: utf-8 -*- 


{
    'name': 'Point of sale product with default code ',
    'author': 'Soft-integration',
    'application': False,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1.1',
    'category': 'Sales/Point of Sale',
    'demo': [],
    'depends': ['point_of_sale'],
    'data': [
    ],
    'assets': {
            'web.assets_qweb': [
                'pos_product_with_default_code/static/src/xml/Screens/ProductScreen/ProductItem.xml',
                'pos_product_with_default_code/static/src/xml/Screens/ProductScreen/Orderline.xml',
                'pos_product_with_default_code/static/src/xml/Screens/ReceiptScreen/OrderReceipt.xml',
            ],
            'web.assets_backend': [
                'pos_product_with_default_code/static/src/js/models.js',
            ],
        },
    'license': 'LGPL-3',
}
