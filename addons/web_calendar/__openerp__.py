{
    'name': 'Web Calendar',
    'category': 'Hidden',
    'description':"""
Web Calendar view.
==========================

""",
    'author': 'Nantian',
    'version': '2.0',
    'depends': ['web'],
    'data' : [
        'views/web_calendar.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'auto_install': True
}
