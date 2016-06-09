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



		'edicion': fields.many2one('edicion.publicidad', string='Edicion'),
		'estilo': fields.many2one('estilo.publicidad', string='Estilo'),
		'seccion': fields.many2one('seccion.publicidad', string='Seccion'),
		'subseccion': fields.many2one('subseccion.publicidad', string='Subseccion'),
		'pagina': fields.many2one('pagina.publicidad', string='Pagina'),
		'tarifa': fields.many2one('tarifa.publicidad', string='Tarifa'),

		'color': fields.many2one('color.publicidad', string='Color'),
		'status': fields.many2one('status.publicidad', string='Status'),
		'dias':fields.integer(string="Días", size=10),
		'ancho':fields.integer(string="Ancho", size=10),
		'alto':fields.integer(string="Alto", size=10),
		'orden_insercion':fields.integer(string="Orden de Inserción", size=20),
		'arte_final':fields.boolean('Arte Final'),

		'centro_costos': fields.many2one('centro', string='Centro de Costos:'),
		'vendedor_agente': fields.many2one('vendedor_agente.publicidad', string='Vendedor/Agente'),
		'tipo': fields.many2one('tipo.publicidad', string='Tipo'),
		'mercado': fields.many2one('mercado.publicidad', string='Mercado'),
		'retener': fields.many2one('retener.publicidad', string='Retener'),
		'contrato': fields.many2one('contrato.publicidad', string='Contrato'),
	}

	class Edicion(models.Model):
	    _name = "edicion.publicidad"
	    _columns = {
	        'name': fields.char('Edición:', size=32),
	    }

	class Estilo(models.Model):
	    _name = "estilo.publicidad"
	    _columns = {
	        'name': fields.char('Estilo:', size=32),
	    }

	class Seccion(models.Model):
	    _name = "seccion.publicidad"
	    _columns = {
	        'name': fields.char('Sección:', size=32),
	    }

	class Subseccion(models.Model):
	    _name = "subseccion.publicidad"
	    _columns = {
	        'name': fields.char('Subsección:', size=32),
	    }

	class Pagina(models.Model):
	    _name = "pagina.publicidad"
	    _columns = {
	        'name': fields.char('Página:', size=32),
	    }

	class Tarifa(models.Model):
	    _name = "tarifa.publicidad"
	    _columns = {
	        'name': fields.char('Tarifa:', size=32),
	    }

	class Color(models.Model):
	    _name = "color.publicidad"
	    _columns = {
	        'name': fields.char('Color:', size=32),
	    }

	class Status(models.Model):
	    _name = "status.publicidad"
	    _columns = {
	        'name': fields.char('Status:', size=32),
	    }

	class CentroCostos(models.Model):
	    _name = "centro_costos.publicidad"
	    _columns = {
	        'name': fields.char('Centro de Costos:', size=32),
	    }

	class VendedorAgente(models.Model):
	    _name = "vendedor_agente.publicidad"
	    _columns = {
	        'name': fields.char('Vendedor:', size=32),
	    }

	class Tipo(models.Model):
	    _name = "tipo.publicidad"
	    _columns = {
	        'name': fields.char('Tipo:', size=32),
	    }

	class Mercado(models.Model):
	    _name = "mercado.publicidad"
	    _columns = {
	        'name': fields.char('Mercado:', size=32),
	    }

	class Retener(models.Model):
	    _name = "retener.publicidad"
	    _columns = {
	        'name': fields.char('Retener:', size=32),
	    }

	class Contrato(models.Model):
	    _name = "contrato.publicidad"
	    _columns = {
	        'name': fields.char('Contrato:', size=32),
	    }
