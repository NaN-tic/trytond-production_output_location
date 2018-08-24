# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Location']


class Location(metaclass=PoolMeta):
    __name__ = 'stock.location'
    production_output_location = fields.Many2One('stock.location',
        'Production Output',
        states={
            'invisible': Eval('type') != 'warehouse',
            'readonly': ~Eval('active'),
            },
        domain=[
            ('type', '=', 'storage'),
            ('parent', 'child_of', [Eval('id')]),
            ],
        depends=['type', 'active', 'id'])
