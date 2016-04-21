# -*- coding: utf-8 -*-
from openerp import models, fields
import openerp
from openerp import api
from openerp import SUPERUSER_ID
from openerp import tools
from openerp.modules.module import get_module_resource
from openerp.osv import fields, osv
from openerp.tools.translate import _

class AdministrationProduct(models.Model):
	_name = 'admin.product'
	_columns = {
		'edicion': fields.text('Edición'),
		'estilo': fields.text('Estilo'),
		'seccion': fields.text('Sección'),
		'subseccion': fields.text('Subsección'),
		'pagina': fields.text('Página'),
		'tarifa': fields.text('Tarifa'),

		'color': fields.text('Color'),
		'status': fields.text('Status'),
		'dias':fields.text('Días'),
		'ancho':fields.text('Ancho'),
		'alto':fields.text('Alto'),
		'orden_insercion':fields.text('Orden de inserción'),
		'arte_final':fields.text('Arte final'),

		'centro_costos':fields.text('Centro de Costos'),
		'vendedor_agente': fields.text('Vendedor Agente'),
		'tipo': fields.text('Tipo'),
		'mercado': fields.text('Mercado'),
		'retener': fields.text('Retener'),
		'contrato': fields.text('Contrato'),
	}

