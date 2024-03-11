from django.db import models
    
class Player(models.Model):
    username = models.CharField(max_length=255, default='')
    name = models.CharField(max_length=255, default='Yuji') 
    energy_point = models.IntegerField(default=200)  
    heart_point = models.IntegerField(default=3)
    villain_strike_left = models.IntegerField(default=3)
    carta_atual = models.CharField(max_length=255, default='')
    atk_atual = models.IntegerField(default=0)
    drawperformed = models.FloatField(default=False)
    carta_do_vilao = models.CharField(max_length=255, default='')
    atk_do_vilao = models.IntegerField(default=0)
    # carta_atual = models.ForeignKey('Card', null=True, blank=True, on_delete=models.SET_NULL)
    verification = models.FloatField(default=False)
    atributo_atual = models.CharField(max_length=255, default='')
    life_round2 = models.IntegerField(default=0)
    controle1 = models.IntegerField(default=0)
    
    #fase 2
    enemy_life_round2 = models.IntegerField(default=4000)
    energy_pointFase1 = models.IntegerField(default=0)
    life_round2savepoint = models.IntegerField(default=0)
    
    rising_energy = models.BooleanField(default=False)
    thounsand_knives = models.BooleanField(default=False)
    millennium_shield = models.BooleanField(default=False)
    angel_wing = models.BooleanField(default=False)
    acceleration = models.BooleanField(default=False)
    calculo_dano_player = models.IntegerField(default=0)
    calculo_dano_inimigo = models.IntegerField(default=0)
    
    dark_energy = models.IntegerField(default=200)
    dark_energy_shield = models.BooleanField(default=False)
    dark_energy_blast = models.BooleanField(default=False)
    dark_aura = models.BooleanField(default=False)
    
    defesa_acumulada_inimigo = models.IntegerField(default=0)
    defesa_acumulada = models.IntegerField(default=0)

    
    turno= models.IntegerField(default=0)
    contagem = models.IntegerField(default=0)
    stand_by = models.BooleanField(default=False)
    feiticos = []
    imagens_feiticos = []
    
    limite= models.IntegerField(default=3)
    
    #fase 3
    par_linha_coluna = []
    
    poder_somado = models.IntegerField(default=0)
    
    contador_batalha3 = models.IntegerField(default=0)
    
    vida_sobrando = models.IntegerField(default=1)
    
    fim = models.BooleanField(default=False)
    
    flip = models.BooleanField(default=False)
    comecou = models.BooleanField(default=False)
    superou = models.IntegerField(default=0)
    batalhar = models.BooleanField(default=False)
    
    
    monstros_fase3 = []
    
    fase_atual = models.IntegerField(default=1)
    
    resultado = models.CharField(max_length=255, default="l")
    
    historiaVariavel = models.IntegerField(default=1)
    historiaVariavel2 = models.IntegerField(default=1)
    historiaVariavel3 = models.IntegerField(default=1)
    
    batalha_em_andamento = models.BooleanField(default=False)

    venceu_fase2 = models.BooleanField(default=False)
    
    lista_boss = [ 
        {'id': 1, 'img':'global/img/armedragon.webp', 'atk': 2800},
        {'id': 2, 'img':'global/img/cosmoqueen.webp', 'atk': 2900},
        {'id': 3, 'img':'global/img/metalarmoredbug.webp', 'atk': 2800},          
        {'id': 4, 'img':'global/img/tri-horned-dragon.webp', 'atk': 2850},
        {'id': 5, 'img':'global/img/wingweaver.webp', 'atk': 2750},
        
    ]
    boss_escolhido = models.CharField(max_length=255, default='')
    boss_escolhido_atk = models.IntegerField(default=0)

    
    lista_imagem = [
        {'id': 1, 'img':'global/img/red-eyes-black-dragon-en002.webp', 'atk': 2400},
        {'id': 2, 'img':'global/img/swordstalker.jpg', 'atk': 2000},
        {'id': 3, 'img':'global/img/flamecerebrus.jpg', 'atk': 2100},
        {'id': 4, 'img':'global/img/anotherversedragon.jpg', 'atk': 2500},
        {'id': 5, 'img':'global/img/warwolf.jpg', 'atk': 2000},
        {'id': 6, 'img':'global/img/boarder.jpg', 'atk': 2000},
        {'id': 7, 'img':'global/img/vorseraider.webp', 'atk': 1900}, 
    ]
    
    batalha3lista = [
[{'i':'1', 'v':'', 't': 0, 'atk': 0}, {'i':'2', 'v':'', 't': 0, 'atk': 0}, {'i':'3', 'v':'', 't': 0, 'atk': 0}, {'i':'4', 'v':'', 't': 0, 'atk': 0},{'i':'5', 'v':'', 't': 0, 'atk': 0}],
[{'i':'6', 'v':'', 't': 0, 'atk': 0}, {'i':'7', 'v':'', 't': 0, 'atk': 0}, {'i':'8', 'v':'', 't': 0, 'atk': 0}, {'i':'9', 'v':'', 't': 0, 'atk': 0},{'i':'10', 'v':'', 't': 0, 'atk': 0}],
[{'i':'11', 'v':'', 't': 0, 'atk': 0}, {'i':'12', 'v':'', 't': 0, 'atk': 0}, {'i':'13', 'v':'', 't': 0, 'atk': 0}, {'i':'14', 'v':'', 't': 0, 'atk': 0},{'i':'15', 'v':'', 't': 0, 'atk': 0}],
[{'i':'16', 'v':'', 't': 0, 'atk': 0}, {'i':'17', 'v':'', 't': 0, 'atk': 0}, {'i':'18', 'v':'', 't': 0, 'atk': 0}, {'i':'19', 'v':'', 't': 0, 'atk': 0},{'i':'20', 'v':'', 't': 0, 'atk': 0}]
             ]

    
    cardlist = [
        {'id': 1, 'name': 'Alexandrite dragon', 'ATK': 2000, 'img': 'global/img/alexandrite dragon.jpg', 'drawn': False, 'attribute': 'light'},
        {'id': 2, 'name': 'Alexandrite dragon', 'ATK': 2000, 'img': 'global/img/alexandrite dragon.jpg', 'drawn': False, 'attribute': 'light'},
        {'id': 3, 'name': 'Alexandrite dragon', 'ATK': 2000, 'img': 'global/img/alexandrite dragon.jpg', 'drawn': False, 'attribute': 'light'},
        {'id': 4, 'name': 'Blazing Inpachi', 'ATK': 1850, 'img': 'global/img/blazing inpachi.jpg', 'drawn': False, 'attribute': 'fire'},
        {'id': 5, 'name': 'Blazing Inpachi', 'ATK': 1850, 'img': 'global/img/blazing inpachi.jpg', 'drawn': False,'attribute': 'fire'},
        {'id': 6, 'name': 'Blazing Inpachi', 'ATK': 1850, 'img': 'global/img/blazing inpachi.jpg', 'drawn': False, 'attribute': 'fire'},
        {'id': 7, 'name': 'Kairyu-shin', 'ATK': 1800, 'img': 'global/img/kairyu-shin.jpg', 'drawn': False, 'attribute': 'water'},
        {'id': 8, 'name': 'Kairyu-shin', 'ATK': 1800, 'img': 'global/img/kairyu-shin.jpg', 'drawn': False, 'attribute': 'water'},
        {'id': 9, 'name': 'Mad Dog of Darkness', 'ATK': 1900, 'img': 'global/img/mad-dog-of-darkness-yskr-en009-common.jpg', 'drawn': False, 'attribute': 'dark'},
        {'id': 10, 'name': 'Mad Dog of Darkness', 'ATK': 1900, 'img': 'global/img/mad-dog-of-darkness-yskr-en009-common.jpg', 'drawn': False, 'attribute': 'dark'},
        {'id': 11, 'name': 'Mad Dog of Darkness', 'ATK': 1900, 'img': 'global/img/mad-dog-of-darkness-yskr-en009-common.jpg', 'drawn': False, 'attribute': 'dark'},
        {'id': 12, 'name': 'Ruder Kaiser', 'ATK': 1800, 'img': 'global/img/ruderkaiser.jpg', 'drawn': False, 'attribute': 'earth'},
        {'id': 13, 'name': 'Ruder Kaiser', 'ATK': 1800, 'img': 'global/img/ruderkaiser.jpg', 'drawn': False, 'attribute': 'earth'},
        {'id': 14, 'name': 'Sky Scout', 'ATK': 1800, 'img': 'global/img/SkyScout.webp', 'drawn': False , 'attribute': 'wind'},
        {'id': 15, 'name': 'Sky Scout', 'ATK': 1800, 'img': 'global/img/SkyScout.webp', 'drawn': False , 'attribute': 'wind'},
        {'id': 16, 'name': 'Sky Scout', 'ATK': 1800, 'img': 'global/img/SkyScout.webp', 'drawn': False, 'attribute': 'wind'},
        {'id': 17, 'name': 'Ryu-Kishin Powered', 'ATK': 1600, 'img': 'global/img/ryu-kishin.webp', 'drawn': False, 'attribute': 'dark'},
        {'id': 18, 'name': 'Ryu-Kishin Powered', 'ATK': 1600, 'img': 'global/img/ryu-kishin.webp', 'drawn': False, 'attribute': 'dark'},
        {'id': 19, 'name': 'Ryu-Kishin Powered', 'ATK': 1600, 'img': 'global/img/ryu-kishin.webp', 'drawn': False, 'attribute': 'dark'},
        {'id': 20, 'name': 'Red-Eyes Black Dragon', 'ATK': 2400, 'img': 'global/img/red-eyes-black-dragon-en002.webp', 'drawn': False, 'attribute': 'dark'},
    ]

# class Card(models.Model):
#     name = models.CharField(max_length=255)
#     ATK = models.IntegerField()
#     img = models.CharField(max_length=255)
#     drawn = models.BooleanField(default=False)
    