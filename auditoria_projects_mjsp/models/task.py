from odoo import models, fields, api

class Task(models.Model):
    _inherit = 'project.task'

    x_process_by = fields.Char(
        string='Proceso realizado por',
        default='Dirección ministerial de Auditoria interna',
        readonly=True
    )
    x_assigned_users = fields.Many2many(
        'res.users',
        'task_assigned_users_rel',  # Tabla intermedia específica
        'task_id',
        'user_id',
        string='Asignados',
        tracking=True
    )
    x_reference_index = fields.Many2many(
        'project.reference.index',
        'task_reference_index_rel',  # Tabla intermedia específica
        'task_id',
        'reference_id',
        string='Índice de referencia',
        tracking=True
    )
    x_department = fields.Many2many(
        'project.department',
        'task_department_rel',  # Tabla intermedia específica
        'task_id',
        'department_id',
        string='Departamento/Dirección/Unidad',
        tracking=True
    )
    x_assignment_number = fields.Many2many(
        'project.assignment.number',
        'task_assignment_number_rel',  # Tabla intermedia específica
        'task_id',
        'assignment_id',
        string='Asignación No.',
        tracking=True
    )
    x_until = fields.Many2one(
        'res.users',
        string='Hasta',
        tracking=True
    )
    image = fields.Binary(
        string='Imagen',
        attachment=True
    )