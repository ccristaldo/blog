from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'myblog',
        'USER' : 'sa',
        'PASSWORD' : '<Anaeva01>',
        'HOST': '127.0.0.1',
    	'PORT': '1433',

        'OPTIONS':{
        	'driver':'/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.6.so.1.1',
        	'extra_params': "Persist Security Info=False;server=127.0.0.1"
        }
    },
}
