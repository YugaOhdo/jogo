#Indicar que é um package
from .contact_views import *
from .contact_forms import *
from .user_forms import *
#com isso estamos enganando o django, fazendo pensar que a pasta views é o arquivo views.py
#pois o init é a primeira coisa a ser importada, e estão importando tudo de contact_views,
#que tinha o conteudo de views

#podemos por mais importações e vai funcionar como se fosse views