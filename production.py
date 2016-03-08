# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['Production']


class Production(metaclass=PoolMeta):
    __name__ = 'production'

    def get_rec_name(self, name):
        name = super(Production, self).get_rec_name(name)
        if self.product:
            name = '%s %s' % (name, self.product.rec_name)
        return name

    @classmethod
    def search_rec_name(cls, name, clause):
        domain = super(Production, cls).search_rec_name(name, clause)
        return ['OR',
            domain,
            ('product',) + tuple(clause[1:]),
            ]

    def explode_bom(self):
        super(Production, self).explode_bom()
        if self.warehouse and self.warehouse.production_output_location:
            output_location = self.warehouse.production_output_location
            for move in self.outputs:
                if move.to_location != output_location.id:
                    move.to_location = output_location.id

    def set_moves(self):
        super(Production, self).set_moves()
        Move = Pool().get('stock.move')
        if self.warehouse.production_output_location:
            storage_location = self.warehouse.storage_location
            to_write = []
            for move in self.outputs:
                if move.to_location == storage_location:
                    to_write.append(move)
            if to_write:
                output_location = self.warehouse.production_output_location
                Move.write(to_write, {
                        'to_location': output_location.id,
                         })
