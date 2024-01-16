from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return f'{self.name}'

    
class Contact(models.Model):
    #id primary key é automatico
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)  #blank=True torna opcional
    created_date = models.DateTimeField(default=timezone.now)   #pega a data atual
    description = models.TextField(blank=True)   #ilimitado
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/$Y/%m/') #vai para pasta 'media' e
                                                                  #dentro dela cria a 'pictures'
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    ) #outra opção em vez de SET_NULL: CASCADE  - apagaria todos que tem a categoria junto
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} {self.show}'


#python manage.py shell
#from django.contrib.auth.models import User
#user = User.objects.create_user(username='usuario', password='123')

#user.is_staff = True
#user.save()