# -*- coding: utf-8 -*-
from openerp import models, fields
from openerp import api
import datetime
from datetime import date
import calendar

class EspacioPublicitario(models.Model):
    _name = 'espacio.publicitario'
    name = fields.Char(string='Description', required=False)
    is_done = fields.Boolean(string='Done?')
    active = fields.Boolean(string='Active?', default=True)
    CostPrice = fields.Float('Buy price', readonly=True)
    ShippingCost = fields.Integer('Shipping Cost')
    standard_price = fields.Float('Calculated Field')
    date_field = fields.Text('dates', readonly=True)

    # Campos para el cálculo de precios
    costo_base = fields.Float('Costo Base', readonly=True)
    costo_extras = fields.Float('Extras', readonly=True)
    descuentos = fields.Float('Descuentos', readonly=True)
    costo_comision = fields.Float('Comisión', readonly=True)
    costo_contrato = fields.Float('Contrato', readonly=True)
    costo_impuestos = fields.Float('Impuestos', readonly=True)
    costo_total = fields.Float('Total', readonly=True)
    costo_anuncio = fields.Float('Anuncio', readonly=True)
    costo_impuestos = fields.Float('Impuestos', readonly=True)
    costo_final = fields.Float('Costo Final', readonly=True)

    # Campos del espacio publicitario
    edicion = fields.Many2one('edicion_espacio.publicidad', string='Edición')
    estilo = fields.Many2one('estilo_espacio.publicidad', string='Estilo')
    seccion = fields.Many2one('seccion_espacio.publicidad', string='Sección')
    subseccion = fields.Many2one('subseccion_espacio.publicidad', string='Subsección')
    pagina = fields.Many2one('pagina_espacio.publicidad', string='Página')
    tarifa = fields.Many2one('tarifa_espacio.publicidad', string='Tarifa')
    color = fields.Many2one('color_espacio.publicidad', string='Color')
    status = fields.Many2one('status_espacio.publicidad', string='Status')
    centro_costos = fields.Many2one('centro_costos_espacio.publicidad', string='Centro de Costos')
    vendedor_agente = fields.Many2one('vendedor_agente_espacio.publicidad', string='Vendedor')
    tipo = fields.Many2one('tipo_espacio.publicidad', string='Tipo')
    mercado = fields.Many2one('mercado_espacio.publicidad', string='Mercado')
    retener = fields.Many2one('retener_espacio.publicidad', string='retener')
    contrato = fields.Many2one('contrato_espacio.publicidad', string='Contrato')
    dias = fields.Integer('Días')
    ancho = fields.Float('Ancho')
    alto = fields.Float('Alto')
    orden_insercion = fields.Integer('Orden de Inserción')
    arte_final = fields.Boolean('Arte Final')
    dias_publicidad = fields.Many2many('semana.publicidad', readonly=False)

    #This method will be called when either the field CostPrice or the field ShippingCost changes.
    def on_change_price(self,cr,user,ids,CostPrice,ShippingCost,context=None):
	#Calculate the total
	total = CostPrice + ShippingCost
        res = {
            'value': {
		#This sets the total price on the field standard_price.
                'standard_price': total
	      }
	}
	#Return the values to update it in the view.
	return res

    def _compute_days(self,cr,user,ids,dias,context=None):
        today = date.today()
        num_days = dias
        week_days = ''
        costo_base_week = 3244.56
        for i in range(num_days):
            date_end = today + datetime.timedelta(days=i)
            week_day = calendar.day_name[date_end.weekday()]
            week_days += week_day+":        " + str(costo_base_week) + "\n"
            costo_base_week += 456.88
        res = {
            'value': {
                'date_field': week_days
            }
        }
        return res


class EdicionEspacioPublicidad(models.Model):
    _name = "edicion_espacio.publicidad"
    name = fields.Char(required=True)
    Xtag_inicio = fields.Char('Tag de Inicio')
    Xtaf_fin =  fields.Char('Tag de finalizacion')
    costo = fields.Float('Costo')
    descripcion = fields.Text()

class EstiloEspacioPublicidad(models.Model):
    _name = "estilo_espacio.publicidad"
    name = fields.Char('Estilo')
    Xtag_inicio = fields.Char('Tag de Inicio')
    Xtaf_fin =  fields.Char('Tag de finalizacion')
    costo = fields.Float('Costo')
    descripcion = fields.Text()

class SeccionEspacioPublicidad(models.Model):
    _name = "seccion_espacio.publicidad"
    name = fields.Char('Sección')
    Xtag_inicio = fields.Char('Tag de Inicio')
    Xtaf_fin =  fields.Char('Tag de finalizacion')
    costo = fields.Float('Costo')
    descripcion = fields.Text()


class SubseccionEspacioPublicidad(models.Model):
    _name = "subseccion_espacio.publicidad"
    name = fields.Char('Subsección')
    Xtag_inicio = fields.Char('Tag de Inicio')
    Xtaf_fin =  fields.Char('Tag de finalizacion')
    costo = fields.Float('Costo')
    descripcion = fields.Text()

class PaginaEspacioPublicidad(models.Model):
    _name = "pagina_espacio.publicidad"
    name = fields.Char('Página')
    Xtag_inicio = fields.Char('Tag de Inicio')
    Xtaf_fin =  fields.Char('Tag de finalizacion')
    costo = fields.Float('Costo')
    descripcion = fields.Text()

class TarifaEspacioPublicidad(models.Model):
    _name = "tarifa_espacio.publicidad"
    name = fields.Char('Tarifa')
    Xtag_inicio = fields.Char('Tag de Inicio')
    Xtaf_fin =  fields.Char('Tag de finalizacion')
    costo = fields.Float('Costo')
    descripcion = fields.Text()

class ColorEspacioPublicidad(models.Model):
    _name = "color_espacio.publicidad"
    name = fields.Char('Color')
    Xtag_inicio = fields.Char('Tag de Inicio')
    Xtaf_fin =  fields.Char('Tag de finalizacion')
    costo = fields.Float('Costo')
    descripcion = fields.Text()

class StatusEspacioPublicidad(models.Model):
    _name = "status_espacio.publicidad"
    name = fields.Char('Status')
    Xtag_inicio = fields.Char('Tag de Inicio')
    Xtaf_fin =  fields.Char('Tag de finalizacion')
    costo = fields.Float('Costo')
    descripcion = fields.Text()


class CentroCostosEspacioPublicidad(models.Model):
    _name = "centro_costos_espacio.publicidad"
    name = fields.Char('Centro de Costos')
    Xtag_inicio = fields.Char('Tag de Inicio')
    Xtaf_fin =  fields.Char('Tag de finalizacion')
    costo = fields.Float('Costo')
    descripcion = fields.Text()


class VendedorAgenteEspacioPublicidad(models.Model):
    _name = "vendedor_agente_espacio.publicidad"
    name = fields.Char('Vendedor Agente')
    Xtag_inicio = fields.Char('Tag de Inicio')
    Xtaf_fin =  fields.Char('Tag de finalizacion')
    costo = fields.Float('Costo')
    descripcion = fields.Text()

class TipoEspacioPublicidad(models.Model):
    _name = "tipo_espacio.publicidad"
    name = fields.Char('Tipo')
    Xtag_inicio = fields.Char('Tag de Inicio')
    Xtaf_fin =  fields.Char('Tag de finalizacion')
    costo = fields.Float('Costo')
    descripcion = fields.Text()


class MercadoEspacioPublicidad(models.Model):
    _name = "mercado_espacio.publicidad"
    name = fields.Char('Mercado')
    Xtag_inicio = fields.Char('Tag de Inicio')
    Xtaf_fin =  fields.Char('Tag de finalizacion')
    costo = fields.Float('Costo')
    descripcion = fields.Text()


class RetenerEspacioPublicidad(models.Model):
    _name = "retener_espacio.publicidad"
    name = fields.Char('Retener')
    Xtag_inicio = fields.Char('Tag de Inicio')
    Xtaf_fin =  fields.Char('Tag de finalizacion')
    costo = fields.Float('Costo')
    descripcion = fields.Text()


class ContratoEspacioPublicidad(models.Model):
    _name = "contrato_espacio.publicidad"
    name = fields.Char('Contrato')
    Xtag_inicio = fields.Char('Tag de Inicio')
    Xtaf_fin =  fields.Char('Tag de finalizacion')
    costo = fields.Float('Costo')
    descripcion = fields.Text()

class DiasPublicidad(models.Model):
    _name = "semana.publicidad"
    fecha = fields.Char('Fechas')
    costo_base = fields.Float('Costo base')
