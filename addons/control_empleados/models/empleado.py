# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Empleado(models.Model):
    _name = 'control.empleado'
    _description = 'Control de Empleados'
    _order = 'nombre asc'

    nombre = fields.Char(
        string='Nombre completo',
        required=True,
    )
    puesto = fields.Char(
        string='Puesto de trabajo',
    )
    departamento = fields.Selection([
        ('rrhh', 'Recursos Humanos'),
        ('it', 'Informática / IT'),
        ('ventas', 'Ventas'),
        ('administracion', 'Administración'),
        ('produccion', 'Producción'),
        ('logistica', 'Logística'),
        ('otro', 'Otro'),
    ], string='Departamento', default='otro')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    fecha_alta = fields.Date(
        string='Fecha de alta',
        default=fields.Date.today,
    )
    estado = fields.Selection([
        ('activo', 'Activo'),
        ('baja', 'Baja'),
        ('vacaciones', 'Vacaciones'),
    ], string='Estado', default='activo', required=True)
    notas = fields.Text(string='Notas')
