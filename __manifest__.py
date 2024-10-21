{
    'name': 'Escuela',
    'version': '2.0',
    'summary': 'Módulo para gestionar inscripciones en un sistema escolar',
    'description': """
        Este módulo permite gestionar alumnos, inscripciones, materias, cursos y profesores
        en una institución educativa.
    """,
    'author': 'Everdev',
    'website': '',
    'category': 'Education',
    'depends': ['base', 'product'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/enrollment_view.xml',
        'views/subject_view.xml',
        'views/course_view.xml',
        'views/teacher_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}