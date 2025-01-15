{
    'name': 'Proyectos de Auditoría',
    'version': '16.0.1.0.0',
    'category': 'Project',
    'summary': 'Extensión del módulo de proyectos para auditoría interna',
    'description': """
        Módulo personalizado para gestión de proyectos de auditoría interna.
        - Vistas personalizadas para tareas y proyectos
        - Integración con el módulo de documentos
        - Campos específicos para auditoría
    """,
    'author': 'Custom Development',
    'website': '',
    'depends': ['project', 'documents'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_views.xml',
        'views/task_views.xml',
        'data/project_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}