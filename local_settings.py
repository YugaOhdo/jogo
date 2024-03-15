'''
python -c "import string as s; from secrets import SystemRandom as SR; print (''.join
(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))"

gera senha, k é o numero de caracteres
'''

SECRET_KEY = '0$i?dKvc"&9Bf_AoJlp~}zR.lqt:|S<:G};f2_qu!f{k5$`RIV%Nfn(,(M,0~+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['35.180.100.66'] #ip do servidor

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'projeto_agenda',
        'USER': 'usuario_agenda',
        'PASSWORD': 'senha_usuario_agenda',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

