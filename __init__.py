# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import location
from . import production

def register():
    Pool.register(
        location.Location,
        production.Production,
        module='production_output_location', type_='model')
