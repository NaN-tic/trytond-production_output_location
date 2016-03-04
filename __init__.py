# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .location import *
from .production import *

def register():
    Pool.register(
        Location,
        Production,
        module='production_output_location', type_='model')
