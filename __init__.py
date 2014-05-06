# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .asset import *


def register():
    Pool.register(
        Project,
        Asset,
        module='account_asset_project', type_='model')
