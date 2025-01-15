from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

    x_year_audit = fields.Many2many(
        'project.audit.year', 
        'project_year_audit_rel',  # Tabla intermedia específica
        'project_id',
        'year_id',
        string='Año de Auditoría',
        tracking=True
    )
    x_assignment_number = fields.Many2many(
        'project.assignment.number', 
        'project_assignment_number_rel',  # Tabla intermedia específica
        'project_id',
        'assignment_id',
        string='Asignación No.',
        tracking=True
    )
    x_process_by = fields.Char(
        string='Proceso realizado por',
        default='Dirección ministerial de Auditoria interna',
        readonly=True
    )
    x_project_manager_ids = fields.Many2many(
        'res.users',
        'project_manager_users_rel',  # Tabla intermedia específica
        'project_id',
        'user_id',
        string='Gerente de proyecto',
        tracking=True
    )
    x_report_number = fields.Many2many(
        'project.report.number',
        'project_report_number_rel',  # Tabla intermedia específica
        'project_id',
        'report_id',
        string='Informe No.',
        tracking=True
    )
    x_parent_project_id = fields.Many2one(
        'project.project',
        string='Proyecto Padre'
    )

    def action_duplicate_project(self):
        self.ensure_one()
        new_project = self.copy()
        parent_project_id = new_project.x_parent_project_id.id

        if parent_project_id:
            parent_project = self.env['project.project'].browse(parent_project_id)
            
            if parent_project:
                stage_map = {}
                stages = self.env['project.task.type'].search([('project_ids', '=', parent_project.id)])
                
                for stage in stages:
                    existing_stage = self.env['project.task.type'].search([
                        ('name', '=', stage.name),
                        ('project_ids', 'in', new_project.id)
                    ], limit=1)
                    
                    if existing_stage:
                        stage_map[stage.id] = existing_stage.id
                    else:
                        stage.write({'project_ids': [(4, new_project.id)]})
                        stage_map[stage.id] = stage.id

                task_map = {}
                tasks = self.env['project.task'].search([('project_id', '=', parent_project.id)])
                for task in tasks:
                    new_task = task.copy({
                        'project_id': new_project.id,
                        'stage_id': stage_map.get(task.stage_id.id, task.stage_id.id),
                        'name': task.name,
                    })
                    task_map[task.id] = new_task.id

                    attachments = self.env['ir.attachment'].search([
                        ('res_model', '=', 'project.task'),
                        ('res_id', '=', task.id)
                    ])
                    for attachment in attachments:
                        existing_attachment = self.env['ir.attachment'].search([
                            ('res_model', '=', 'project.task'),
                            ('res_id', '=', new_task.id),
                            ('name', '=', attachment.name),
                            ('datas', '=', attachment.datas)
                        ], limit=1)
                        
                        if not existing_attachment:
                            attachment.copy({
                                'res_id': new_task.id,
                            })

                documents = self.env['documents.document'].search([
                    ('folder_id', '=', parent_project.id)
                ])
                for document in documents:
                    existing_document = self.env['documents.document'].search([
                        ('name', '=', document.name),
                        ('folder_id', '=', new_project.id)
                    ], limit=1)
                    
                    if not existing_document:
                        document.copy({'folder_id': new_project.id})

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'project.project',
            'res_id': new_project.id,
            'view_mode': 'form',
            'target': 'current',
        }