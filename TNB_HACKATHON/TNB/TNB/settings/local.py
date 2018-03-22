from .settings import *

DATABASES = {
    'default': {
    	'ENGINE': 'django.db.backends.mysql',
    	'NAME': 'TNB_USER',
		'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    	'USER': 'root',
    	'PASSWORD': 'root',
    	'HOST': 'localhost',
    	'PORT': '3306',
    },
}
