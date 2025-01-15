from odoo import models, fields

class ProjectAuditYear(models.Model):
    _name = 'project.audit.year'
    _description = 'Año de Auditoría'

    name = fields.Char(string='Nombre', required=True)
    color = fields.Integer(string='Color')

class ProjectAssignmentNumber(models.Model):
    _name = 'project.assignment.number'
    _description = 'Número de Asignación'

    name = fields.Char(string='Nombre', required=True)
    color = fields.Integer(string='Color')

class ProjectReferenceIndex(models.Model):
    _name = 'project.reference.index'
    _description = 'Índice de Referencia'

    name = fields.Char(string='Nombre', required=True)
    color = fields.Integer(string='Color')

class ProjectDepartment(models.Model):
    _name = 'project.department'
    _description = 'Departamento/Dirección/Unidad'

    name = fields.Char(string='Nombre', required=True)
    color = fields.Integer(string='Color')

class ProjectReportNumber(models.Model):
    _name = 'project.report.number'
    _description = 'Número de Informe'

    name = fields.Char(string='Nombre', required=True)
    color = fields.Integer(string='Color')