# This file is part of Tryton.  The COPYRIGHT file at the top level of this
# repository contains the full copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Project', 'Asset']


class Project(ModelSQL, ModelView):
    'Asset Project'
    __name__ = 'account.asset.project'

    name = fields.Char('Name')
    description = fields.Text('Description')


class Asset(metaclass=PoolMeta):
    'Asset'
    __name__ = 'account.asset'
    project = fields.Many2One('account.asset.project', 'Project')

    @classmethod
    def __setup__(cls):
        super().__setup__()
        cls.account_journal.context = {'company': Eval('company', -1)}
        cls.account_journal.depends.add('company')
