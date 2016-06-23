# -*- coding: UTF-8 -*-
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
    #_inherit = 'product.product'

    # edicion = fields.many2one('edicion.publicidad', string='Edicion')
    # estilo = fields.many2one('estilo.publicidad', string='Estilo')
    # seccion = fields.many2one('seccion.publicidad', string='Seccion')
    # subseccion = fields.many2one('subseccion.publicidad', string='Subseccion')
    # pagina = fields.many2one('pagina.publicidad', string='Pagina')
    # tarifa = fields.many2one('tarifa.publicidad', string='Tarifa')
    # color = fields.many2one('color.publicidad', string='Color')
    # status = fields.many2one('status.publicidad', string='Status')
    # dias = fields.integer(string="Días", size=10)
    # ancho = fields.integer(string="Ancho", size=10)
    # alto = fields.integer(string="Alto", size=10)
    # orden_insercion = fields.integer(string="Orden de Inserción", size=20)
    # arte_final = fields.boolean('Arte Final')
    # centro_costos = fields.many2one('centro', string='Centro de Costos:')
    # vendedor_agente = fields.many2one('vendedor_agente.publicidad', string='Vendedor/Agente')
    # tipo = fields.many2one('tipo.publicidad', string='Tipo')
    # mercado = fields.many2one('mercado.publicidad', string='Mercado')
    # retener = fields.many2one('retener.publicidad', string='Retener')
    # contrato = fields.many2one('contrato.publicidad', string='Contrato2')
    # hola = fields.text(string='hola')
    _columns = {


		'name': fields.char(string='Nombre'),
        'edicion': fields.many2one('edicion.publicidad', string='Edicion'),
        'estilo': fields.many2one('estilo.publicidad', string='Estilo'),
        'seccion': fields.many2one('seccion.publicidad', string='Seccion'),
        'subseccion': fields.many2one('subseccion.publicidad', string='Subseccion'),
        'pagina': fields.many2one('pagina.publicidad', string='Pagina'),
        'tarifa': fields.many2one('tarifa.publicidad', string='Tarifa'),

        'color': fields.many2one('color.publicidad', string='Color'),
        'status': fields.many2one('status.publicidad', string='Status'),
        'dias': fields.integer(string="Días", size=10),
        'ancho': fields.integer(string="Ancho", size=10),
        'alto': fields.integer(string="Alto", size=10),
        'orden_insercion': fields.integer(string="Orden de Inserción", size=20),
        'arte_final': fields.boolean('Arte Final'),

        'centro_costos': fields.many2one('centro_costos.publicidad', string='Centro de Costos:'),
        'vendedor_agente': fields.many2one('vendedor_agente.publicidad', string='Vendedor/Agente'),
        'tipo': fields.many2one('tipo.publicidad', string='Tipo'),
        'mercado': fields.many2one('mercado.publicidad', string='Mercado'),
        'retener': fields.many2one('retener.publicidad', string='Retener'),
        'contrato': fields.many2one('contrato.publicidad', string='Contrato2'),

    }
    




    class Edicion(models.Model):
        _name = "edicion.publicidad"
        _columns = {
            'name': fields.char('Edición:', size=32),
            # Xtag Etiquetas que indican el inicio y el fin del parametro
            'Xtag_inicio': fields.char('TAG INICIO'),
            'Xtag_fin': fields.char('TAG FIN'),
        }
        # Metodo que permite obtener y mostrar en la interfaz el nombre de la
        # edición, es un toString en Python

        def get_name(self, cr, uid, ids, context=None):
            if context is None:
                context = {}
                if isinstance(ids, (int, long)):
                    ids = [ids]

                    res = []
                    for record in self.browse(cr, uid, ids, context=context):
                        name = record.name
                    return name

    class Estilo(models.Model):
        _name = "estilo.publicidad"
        _columns = {
            'name': fields.char('Estilo:', size=32),
            # Xtag Etiquetas que indican el inicio y el fin del parametro
            'Xtag_inicio': fields.char('TAG INICIO'),
            'Xtag_fin': fields.char('TAG FIN'),
        }
        # Metodo que permite obtener y mostrar en la interfaz el nombre de la
        # edición, es un toString en Python

        def get_name(self, cr, uid, ids, context=None):
            if context is None:
                context = {}
                if isinstance(ids, (int, long)):
                    ids = [ids]

                    res = []
                    for record in self.browse(cr, uid, ids, context=context):
                        name = record.name
                    return name

    class Seccion(models.Model):
        _name = "seccion.publicidad"
        _columns = {
            'name': fields.char('Sección:', size=32),
            # Xtag Etiquetas que indican el inicio y el fin del parametro
            'Xtag_inicio': fields.char('TAG INICIO'),
            'Xtag_fin': fields.char('TAG FIN'),
        }
        # Metodo que permite obtener y mostrar en la interfaz el nombre de la
        # edición, es un toString en Python

        def get_name(self, cr, uid, ids, context=None):
            if context is None:
                context = {}
                if isinstance(ids, (int, long)):
                    ids = [ids]

                    res = []
                    for record in self.browse(cr, uid, ids, context=context):
                        name = record.name
                    return name

    class Subseccion(models.Model):
        _name = "subseccion.publicidad"
        _columns = {
            'name': fields.char('Subsección:', size=32),
            # Xtag Etiquetas que indican el inicio y el fin del parametro
            'Xtag_inicio': fields.char('TAG INICIO'),
            'Xtag_fin': fields.char('TAG FIN'),
        }
        # Metodo que permite obtener y mostrar en la interfaz el nombre de la
        # edición, es un toString en Python

        def get_name(self, cr, uid, ids, context=None):
            if context is None:
                context = {}
                if isinstance(ids, (int, long)):
                    ids = [ids]

                    res = []
                    for record in self.browse(cr, uid, ids, context=context):
                        name = record.name
                    return name

    class Pagina(models.Model):
        _name = "pagina.publicidad"
        _columns = {
            'name': fields.char('Página:', size=32),
            # Xtag Etiquetas que indican el inicio y el fin del parametro
            'Xtag_inicio': fields.char('TAG INICIO'),
            'Xtag_fin': fields.char('TAG FIN'),
        }
        # Metodo que permite obtener y mostrar en la interfaz el nombre de la
        # edición, es un toString en Python

        def get_name(self, cr, uid, ids, context=None):
            if context is None:
                context = {}
                if isinstance(ids, (int, long)):
                    ids = [ids]

                    res = []
                    for record in self.browse(cr, uid, ids, context=context):
                        name = record.name
                    return name

    class Tarifa(models.Model):
        _name = "tarifa.publicidad"
        _columns = {
            'name': fields.char('Tarifa:', size=32),
            # Xtag Etiquetas que indican el inicio y el fin del parametro
            'Xtag_inicio': fields.char('TAG INICIO'),
            'Xtag_fin': fields.char('TAG FIN'),
        }
        # Metodo que permite obtener y mostrar en la interfaz el nombre de la
        # edición, es un toString en Python

        def get_name(self, cr, uid, ids, context=None):
            if context is None:
                context = {}
                if isinstance(ids, (int, long)):
                    ids = [ids]

                    res = []
                    for record in self.browse(cr, uid, ids, context=context):
                        name = record.name
                    return name

    class Color(models.Model):
        _name = "color.publicidad"
        _columns = {
            'name': fields.char('Color:', size=32),
            # Xtag Etiquetas que indican el inicio y el fin del parametro
            'Xtag_inicio': fields.char('TAG INICIO'),
            'Xtag_fin': fields.char('TAG FIN'),
        }
        # Metodo que permite obtener y mostrar en la interfaz el nombre de la
        # edición, es un toString en Python

        def get_name(self, cr, uid, ids, context=None):
            if context is None:
                context = {}
                if isinstance(ids, (int, long)):
                    ids = [ids]

                    res = []
                    for record in self.browse(cr, uid, ids, context=context):
                        name = record.name
                    return name

    class Status(models.Model):
        _name = "status.publicidad"
        _columns = {
            'name': fields.char('Status:', size=32),
            # Xtag Etiquetas que indican el inicio y el fin del parametro
            'Xtag_inicio': fields.char('TAG INICIO'),
            'Xtag_fin': fields.char('TAG FIN'),
        }
        # Metodo que permite obtener y mostrar en la interfaz el nombre de la
        # edición, es un toString en Python

        def get_name(self, cr, uid, ids, context=None):
            if context is None:
                context = {}
                if isinstance(ids, (int, long)):
                    ids = [ids]

                    res = []
                    for record in self.browse(cr, uid, ids, context=context):
                        name = record.name
                    return name

    class CentroCostos(models.Model):
        _name = "centro_costos.publicidad"
        _columns = {
            'name': fields.char('Centro de Costos:', size=32),
            # Xtag Etiquetas que indican el inicio y el fin del parametro
            'Xtag_inicio': fields.char('TAG INICIO'),
            'Xtag_fin': fields.char('TAG FIN'),
        }
        # Metodo que permite obtener y mostrar en la interfaz el nombre de la
        # edición, es un toString en Python

        def get_name(self, cr, uid, ids, context=None):
            if context is None:
                context = {}
                if isinstance(ids, (int, long)):
                    ids = [ids]

                    res = []
                    for record in self.browse(cr, uid, ids, context=context):
                        name = record.name
                    return name

    class VendedorAgente(models.Model):
        _name = "vendedor_agente.publicidad"
        _columns = {
            'name': fields.char('Vendedor:', size=32),
            # Xtag Etiquetas que indican el inicio y el fin del parametro
            'Xtag_inicio': fields.char('TAG INICIO'),
            'Xtag_fin': fields.char('TAG FIN'),
        }
        # Metodo que permite obtener y mostrar en la interfaz el nombre de la
        # edición, es un toString en Python

        def get_name(self, cr, uid, ids, context=None):
            if context is None:
                context = {}
                if isinstance(ids, (int, long)):
                    ids = [ids]

                    res = []
                    for record in self.browse(cr, uid, ids, context=context):
                        name = record.name
                    return name

    class Tipo(models.Model):
        _name = "tipo.publicidad"
        _columns = {
            'name': fields.char('Tipo:', size=32),
            # Xtag Etiquetas que indican el inicio y el fin del parametro
            'Xtag_inicio': fields.char('TAG INICIO'),
            'Xtag_fin': fields.char('TAG FIN'),
        }
        # Metodo que permite obtener y mostrar en la interfaz el nombre de la
        # edición, es un toString en Python

        def get_name(self, cr, uid, ids, context=None):
            if context is None:
                context = {}
                if isinstance(ids, (int, long)):
                    ids = [ids]

                    res = []
                    for record in self.browse(cr, uid, ids, context=context):
                        name = record.name
                    return name

    class Mercado(models.Model):
        _name = "mercado.publicidad"
        _columns = {
            'name': fields.char('Mercado:', size=32),
            # Xtag Etiquetas que indican el inicio y el fin del parametro
            'Xtag_inicio': fields.char('TAG INICIO'),
            'Xtag_fin': fields.char('TAG FIN'),
        }
        # Metodo que permite obtener y mostrar en la interfaz el nombre de la
        # edición, es un toString en Python

        def get_name(self, cr, uid, ids, context=None):
            if context is None:
                context = {}
                if isinstance(ids, (int, long)):
                    ids = [ids]

                    res = []
                    for record in self.browse(cr, uid, ids, context=context):
                        name = record.name
                    return name

    class Retener(models.Model):
        _name = "retener.publicidad"
        _columns = {
            'name': fields.char('Retener:', size=32),
            # Xtag Etiquetas que indican el inicio y el fin del parametro
            'Xtag_inicio': fields.char('TAG INICIO'),
            'Xtag_fin': fields.char('TAG FIN'),
        }
        # Metodo que permite obtener y mostrar en la interfaz el nombre de la
        # edición, es un toString en Python

        def get_name(self, cr, uid, ids, context=None):
            if context is None:
                context = {}
                if isinstance(ids, (int, long)):
                    ids = [ids]

                    res = []
                    for record in self.browse(cr, uid, ids, context=context):
                        name = record.name
                    return name

    class Contrato(models.Model):
        _name = "contrato.publicidad"
        _columns = {
            'name': fields.char('Contrato:', size=32),
            # Xtag Etiquetas que indican el inicio y el fin del parametro
            'Xtag_inicio': fields.char('TAG INICIO'),
            'Xtag_fin': fields.char('TAG FIN'),
        }
        # Metodo que permite obtener y mostrar en la interfaz el nombre de la
        # edición, es un toString en Python

        def get_name(self, cr, uid, ids, context=None):
            if context is None:
                context = {}
                if isinstance(ids, (int, long)):
                    ids = [ids]

                    res = []
                    for record in self.browse(cr, uid, ids, context=context):
                        name = record.name
                    return name
