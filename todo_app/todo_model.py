# -*- coding: utf-8 -*-

from openerp import models, fields
import openerp
from openerp import api
from openerp import SUPERUSER_ID
from openerp import tools
from openerp.modules.module import get_module_resource
from openerp.osv import fields, osv
from openerp.tools.translate import _

class SpecificProduct(models.Model):
	_name = 'specific.product'
	_inherit = 'product.product'
	_columns = {
		'edicion': fields.selection([('imagen', 'Imagen'), ('opcion2', 'Opcion 2'), ('opcion3', 'Opcion 3')], 'Edición'),
		'estilo': fields.selection([('default_desp', 'Default Desp'), ('opcion2', 'Opcion 2'), ('opcion3', 'Opcion 3')], 'Estilo'),
		'seccion': fields.selection([('seccion', 'Capital'), ('opcion2', 'Opcion 2'), ('opcion3', 'Opcion 3')], 'Sección'),
		'subseccion': fields.selection([('indefinida', 'Indefinida'), ('opcion2', 'Opcion 2'), ('opcion3', 'Opcion 3')], 'Subsección'),
		'pagina': fields.selection([('pagina', 'Indefinida'), ('opcion2', 'Opcion 2'), ('opcion3', 'Opcion 3')], 'Página'),
		'tarifa': fields.selection([('tarifa', 'Comercial'), ('opcion2', 'Opcion 2'), ('opcion3', 'Opcion 3')], 'Tarifa'),

		'color': fields.selection([('blanco_negro', 'Blanco y Negro'), ('opcion2', 'Opcion 2'), ('opcion3', 'Opcion 3')], 'Color'),
		'status': fields.selection([('insercion', 'Inserción'), ('opcion2', 'Opcion 2'), ('opcion3', 'Opcion 3')], 'Status'),
		'dias':fields.integer(string="Días", size=10),
		'ancho':fields.integer(string="Ancho", size=10),
		'alto':fields.integer(string="Alto", size=10),
		'orden_insercion':fields.integer(string="Orden de Inserción", size=20),
		'arte_final':fields.boolean('Arte Final'), 

		'centro_costos': fields.selection([('local', 'Local'), ('opcion2', 'Opcion 2'), ('opcion3', 'Opcion 3')], 'Centro de Costos:'),
		'vendedor_agente': fields.selection([('directo', 'Directo'), ('opcion2', 'Opcion 2'), ('opcion3', 'Opcion 3')], 'Vendedor/Agente'),
		'tipo': fields.selection([('normal', 'Normal'), ('opcion2', 'Opcion 2'), ('opcion3', 'Opcion 3')], 'Tipo'),
		'mercado': fields.selection([('general', 'General'), ('opcion2', 'Opcion 2'), ('opcion3', 'Opcion 3')], 'Mercado'),
		'retener': fields.selection([('no_retenido', 'No retenido'), ('opcion2', 'Opcion 2'), ('opcion3', 'Opcion 3')], 'Retener'),
		'contrato': fields.selection([('contrato', ''), ('opcion2', 'Opcion 2'), ('opcion3', 'Opcion 3')], 'Contrato'),
	}

