#Indicar que é um package

from django.shortcuts import render, redirect
import random
from ..model import Player
from ..forms import PlayerForm
from django.urls import reverse
from ..villains import villain1
from ..forms import BotaoForm
from django.shortcuts import render, redirect, get_object_or_404



def index(request):
    form = PlayerForm(request.POST, request.FILES)

    if request.method == "POST":
        context = {
            'form': form, 
        }
        if form.is_valid():
            Player.objects.all().delete()

            player = form.save(commit=False)
            player.save()
            return redirect('contact:history')
        
    context = {
        'form': form,
    }
    return render(
        request, 
        'contact/index.html',
        context,
    )

def showdeck(request):
    player = get_object_or_404(Player, name='Yuji')
    cardlist = Player.objects.get(name='Yuji').cardlist
    

    context = {
        'cardlist': cardlist
    }
    return render(
        request, 
        'contact/showdeck.html',
        context,
    )

def batalha1(request):
    player = get_object_or_404(Player, name='Yuji')
    if 'tutorial' in request.GET:
        lifes = player.heart_point
        energy = player.energy_point
        # atk = int(player.atk_atual)
        strike_left = player.villain_strike_left
        lifes = player.heart_point
        context = {
            'image': player.carta_atual,
            'controle': player.controle1,
            'drawPerformed': player.drawperformed,
            'lifes': list(range(lifes)),
            'energy': energy,
            'atk': player.atk_atual,
            'villain_card': player.carta_do_vilao,
            'villain_card_atk': player.atk_do_vilao,
            'strike_left': list(range(strike_left)),
            'verification': player.verification,
            'strike': player.villain_strike_left,
            'fase_atual': player.fase_atual,
            'strike_left': list(range(strike_left)),
            'verification': player.verification,
            'tutorial': True

            }
        return render(request, 'contact/batalha1.html', context)  
    player.controle1 = 0
    player.save()
    if 'recomecar' in request.GET:
        player.cardlist = []
        player.energy_point = 200
        player.heart_point = 3
        player.villain_strike_left = 3
        player.carta_atual = ''
        player.atk_atual = 0      
        player.carta_do_vilao = ''
        player.atk_do_vilao = 0
        player.verification = False
        player.atributo_atual = ''
        player.life_round2 = 0
        player.enemy_life_round2 = 4000
        player.energy_pointFase1 = 0
        player.life_round2savepoint = 0
        player.controle1 = 1
        player.save()

    lifes = player.heart_point   
    energy = player.energy_point
    strike_left = player.villain_strike_left
    player.verification = False


    if request.method == 'POST':
        player = Player.objects.get(name='Yuji')
        
        
        if 'draw' in request.GET:
            player.verification = True
            undrawn_cards = [card for card in player.cardlist if card['drawn'] is False]

            if not undrawn_cards:
                print("No more cards to draw.")
                return render(request, 'contact/batalha1.html', {'drawPerformed': False})

            
            if 'destinydraw' in request.GET and player.energy_point >70:
                drawn_card = player.cardlist[19]
                player.energy_point -= 70
                player.save()
            else:
                drawn_card = random.choice(undrawn_cards)

            drawn_card['drawn'] = True
            player.carta_atual = drawn_card['img']
            player.atk_atual = int(drawn_card['ATK'])
            player.atributo_atual = drawn_card['attribute']
            
            
            villain_draw = random.choice(range(0, 19))
            player.carta_do_vilao = villain1[villain_draw]['img']
            player.atk_do_vilao = villain1[villain_draw]['ATK']
            
            player.save()
            
        if 'recover_lp' in request.GET:
            if player.energy_point > 50 and player.heart_point !=3:
                player.energy_point -= 50
                player.heart_point += 1
                player.save()
        
        if 'power_up' in request.GET:
            if player.energy_point >= 20:
                player.atk_atual = player.atk_atual + int((20/100 * player.atk_atual))
                player.energy_point -= 20
                player.save()
        if 'dark_energy' in request.GET:
            if player.energy_point >= 10:
                if player.atributo_atual == 'dark':
                    player.atk_atual += 200
                    player.energy_point -= 10
                    player.save()
                else:
                    player.atk_atual -= 200
                    player.energy_point -= 10
                    player.save()   
        if 'fire_power' in request.GET:
            if player.energy_point >= 10:
                if player.atributo_atual == 'fire':
                    player.atk_atual += 200
                    player.energy_point -= 10
                    player.save()
                else:
                    player.atk_atual -= 200
                    player.energy_point -= 10
                    player.save()    
        if 'water_impulse' in request.GET:
            if player.energy_point >= 10: 
                if player.atributo_atual == 'water':
                    player.atk_atual += 200
                    player.energy_point -= 10
                    player.save()
                else:
                    player.atk_atual -= 200
                    player.energy_point -= 10
                    player.save()    
        if 'compare' in request.GET and player.villain_strike_left != 0:
            player.verification = False
            if player.atk_atual > int(player.atk_do_vilao):
                player.villain_strike_left -= 1
                player.save()
            elif player.atk_atual < int(player.atk_do_vilao):
                player.heart_point -= 1
                player.save()
            if player.heart_point == 0:
                return redirect('contact:resultado')
        elif player.villain_strike_left == 0:
                player.energy_point += 30
                player.save()
                if player.heart_point == 1:
                    player.life_round2 = 1000
                    player.save()
                elif player.heart_point == 2:
                    player.life_round2 = 1500
                    player.save()
                elif player.heart_point == 3:
                    player.life_round2 = 2000
                    player.save()
                if player.energy_point > 200:
                    player.energy_point=200
                    player.save()
                player.life_round2savepoint = player.life_round2
                player.energy_pointFase1 = player.energy_point
                player.save()
                return redirect('contact:history2')
                
        image = player.carta_atual
        energy = player.energy_point
        # atk = int(player.atk_atual)
        strike_left = player.villain_strike_left
        lifes = player.heart_point
        
        player.fase_atual = 1
        player.save()
        player.drawperformed = True
        context = {
            'image': image,
            'controle': player.controle1,
            'drawPerformed': True,
            'lifes': list(range(lifes)),
            'energy': energy,
            'atk': player.atk_atual,
            'villain_card': player.carta_do_vilao,
            'villain_card_atk': player.atk_do_vilao,
            'strike_left': list(range(strike_left)),
            'verification': player.verification,
            'strike': player.villain_strike_left

            }

        return render(request, 'contact/batalha1.html', context)
    player.drawperformed = 'draw' in request.GET
    context = {
            'drawPerformed': player.drawperformed,
            'controle': 0,
            'lifes': list(range(lifes)),
            'energy': energy,
            'strike_left': list(range(strike_left)),
            'villain_card': player.carta_do_vilao,
            'image': player.carta_atual,
            'verification': player.verification,
            'strike': player.villain_strike_left,
            'fase_atual': player.fase_atual,  
        }
    
    return render(request, 'contact/batalha1.html', context)

def batalha2(request):
    player = get_object_or_404(Player, name='Yuji')
    resto_turno = player.turno % 2    
    player.venceu_fase2 == False
    player.save()
    if 'tutorial' in request.GET:
        context = {
        'tutorial': True,
        'energy': player.energy_point,
        'life': player.life_round2,
        'elife': player.enemy_life_round2,
        'feiticos_img': player.imagens_feiticos,
        'dark_energy_blast' : player.dark_energy_blast,
        'dark_energy_shield': player.dark_energy_shield,
        'turno': player.turno,
        'resto_turno': resto_turno,
        'dark_energy': player.dark_energy,
        'rising_energy' : player.rising_energy,
        'acceleration': player.acceleration,
        'angelwing': player.angel_wing,
        'calculo_player': int(player.calculo_dano_player),
        'calculo_inimigo': int(player.calculo_dano_inimigo),
        'contagem': player.contagem,
        'expandir': player.limite,
        'thousandknives': player.thounsand_knives,
        'millenniumshield': player.millennium_shield,
        
        }
        return render(
            request, 
            'contact/batalha2.html',
            context,
        )
    
    
    player.fase_atual = 2
    player.save()
    
    if 'recomecar' in request.GET:
        player.energy_point = player.energy_pointFase1
        player.life_round2 = player.life_round2savepoint
        player.enemy_life_round2 = 4000
        player.rising_energy = False
        player.thounsand_knives = False
        player.millennium_shield = False
        player.angel_wing = False
        player.acceleration = False
        player.calculo_dano_player = 0
        player.calculo_dano_inimigo = 0
        player.dark_energy = 200
        player.dark_energy_shield = False
        player.dark_energy_blast = False
        player.dark_aura = False
        player.defesa_acumulada_inimigo = 0
        player.defesa_acumulada = 0
        player.turno= 0
        player.contagem = 0
        player.stand_by = False
        player.feiticos = []
        player.imagens_feiticos = []
        player.limite==3
        player.save()

        
    # if request.method == 'POST':
    if player.contagem == 0:
        if player.turno % 2 == 0:
            player.dark_energy_shield=True
            player.save()
        else:
            player.dark_energy_blast = True
            player.save()
            
        
    if 'faseDeBatalha' in request.GET:
        
        if player.turno % 2 == 0:
        
            player.turno += 1
            player.dark_energy_shield=False
            poder = random.choice([10,11,12,13,14,15,16,17,18,19,20])
            player.dark_energy -= poder
            player.calculo_dano_inimigo += poder * 80 
            player.save()
        else:
            player.turno += 1
            player.dark_energy_blast = False
            poder = random.choice([10,11,12,13,14,15,16,17,18,19,20])
            player.dark_energy -= poder
            player.calculo_dano_player -= poder * 80
            player.save()   
            
        for n in player.feiticos:
            if n == 1:
                player.energy_point -= 5
                player.life_round2 += 300
                player.save()
            if n == 2:
                player.energy_point -= 5
                player.calculo_dano_inimigo -= 500
                player.save()
            if n == 3:    
                player.energy_point -= 12
                player.calculo_dano_player = 0
                player.save()
            if n == 5:
                player.energy_point -= 7
                player.calculo_dano_player += 500
                player.save()
            if n == 7:
                player.energy_point -= 10
                player.enemy_life_round2 -= 1200
                player.save()
            if n == 9:
                player.energy_point -= 8
                player.calculo_dano_player += 1000
                player.save()
            if n == 10:
                player.energy_point -= 3
                player.calculo_dano_inimigo -= 300
                player.save()
       
        if 6 in player.feiticos:
            player.energy_point -= 15
            player.calculo_dano_inimigo *= 150/100
            player.calculo_dano_player = (player.calculo_dano_player * 10)/100
            player.save()
        
        if 8 in player.feiticos:
            player.energy_point -= 10
            player.calculo_dano_player += 700
            player.save()
            
        if player.turno % 2 == 0:
            if player.calculo_dano_inimigo == 0:
                player.dark_energy += poder
            player.save()
        

        
        if player.calculo_dano_player < 0:
            player.life_round2 += player.calculo_dano_player
            player.calculo_dano_player = 0
            # player.contagem += 1
            player.save()
        if player.calculo_dano_inimigo < 0:
            player.enemy_life_round2 += player.calculo_dano_inimigo
            player.calculo_dano_inimigo = 0
            # player.contagem += 1
            player.save()
        player.contagem = 0
        if player.limite != 3:
            player.limite = 3
            player.save()
        if 8 in player.feiticos:
                player.limite += 1                
                player.save()
        if 4 in player.feiticos:
            player.energy_point -= 10
            player.limite += 2
            player.save()
        if player.contagem == 0:
            player.feiticos.clear()
            player.imagens_feiticos.clear()
            player.save()
        player.save()
    if 'bluemedicine' in request.GET and player.contagem < player.limite:
        player.feiticos.append(1)
        player.imagens_feiticos.append('blue_medicine.jpg')
        player.contagem += 1
        player.save()
    if 'hinotama' in request.GET and player.contagem < player.limite :
        player.feiticos.append(2)
        player.imagens_feiticos.append('hinotama.jpg')
        player.contagem += 1
        player.save()

    if 'evasion' in request.GET and player.contagem < player.limite:
        player.contagem += 1
        player.feiticos.append(3)
        player.imagens_feiticos.append('evasion.jpg')

        player.save()

    if 'acceleration' in request.GET and player.contagem < player.limite:
        player.contagem += 1
        player.feiticos.append(4)
        player.imagens_feiticos.append('acceleration.png')
        player.acceleration = True
        player.save()
    
    if 'ringofdefense' in request.GET and player.contagem < player.limite:
        player.contagem += 1
        player.feiticos.append(5)
        player.imagens_feiticos.append('ringofdefense.jpg')
        player.save()
          
    if 'risingenergy' in request.GET and player.contagem < player.limite:
        player.contagem += 1
        player.feiticos.append(6)
        player.imagens_feiticos.append('RisingEnergy.webp')
        player.rising_energy = True
        player.save()

           
    if 'thousandknives' in request.GET and player.contagem < player.limite:
            player.contagem += 1
            player.thounsand_knives = True
            player.feiticos.append(7)
            player.imagens_feiticos.append('thousandknives.png')
            player.save()
           
    if 'angelwing' in request.GET and player.contagem < player.limite:
        player.contagem += 1
        player.feiticos.append(8)
        player.imagens_feiticos.append('angelwing.jpg')
        player.angel_wing = True
        player.save()
        
    if 'millenniumshield' in request.GET and player.contagem < player.limite:
        player.contagem += 1
        player.feiticos.append(9)
        player.millennium_shield = True
        player.imagens_feiticos.append('millenniumshield.jpg')
        player.save()
        
    if 'gun' in request.GET  and player.contagem < player.limite:
        player.contagem += 1
        player.imagens_feiticos.append('gun.jpg')
        player.feiticos.append(10)
        player.save()
    if 'nothing' in request.GET  and player.contagem < player.limite:
        player.contagem = 3
        player.save()
    
    resto_turno = player.turno % 2    
    
    if player.enemy_life_round2 <= 0 or player.dark_energy <= 0:
        player.venceu_fase2 == True
        player.save()
        return redirect('contact:history3')

    if player.life_round2 <= 0 or player.energy_point <=0:
        return redirect('contact:resultado')

    
    context = {
        'energy': player.energy_point,
        'life': player.life_round2,
        'elife': player.enemy_life_round2,
        'feiticos_img': player.imagens_feiticos,
        'dark_energy_blast' : player.dark_energy_blast,
        'dark_energy_shield': player.dark_energy_shield,
        'turno': player.turno,
        'resto_turno': resto_turno,
        'dark_energy': player.dark_energy,
        'rising_energy' : player.rising_energy,
        'acceleration': player.acceleration,
        'angelwing': player.angel_wing,
        'calculo_player': int(player.calculo_dano_player),
        'calculo_inimigo': int(player.calculo_dano_inimigo),
        'contagem': player.contagem,
        'expandir': player.limite,
        'thousandknives': player.thounsand_knives,
        'millenniumshield': player.millennium_shield,
        
    }
    return render(
        request, 
        'contact/batalha2.html',
        context,
    )

def batalha3(request):
    player = get_object_or_404(Player, name='Yuji')
    if player.venceu_fase2 == False:
        return redirect('contact:batalha2')
    if 'tutorial' in request.GET:
        context = {
        'andamento': player.batalha_em_andamento,
        'superou': player.superou,
        'sequencia': player.batalha3lista,
        'flip': player.flip,
        'comecou': player.comecou,
        'vida_sobrando': player.vida_sobrando,
        'poder_somado': player.poder_somado,
        'boss_inimigo': player.boss_escolhido,
        'boss_Inimigo_atk': int(player.boss_escolhido_atk),
        'poder_somado': player.poder_somado,
        'contador_batalha': 7 - player.contador_batalha3,
        'fim': player.fim,
        'lista_aliados': player.monstros_fase3,
        'batalhar': player.batalhar,
        'tutorial': True,
        
    }
        print(context)
        return render(
                request, 
                'contact/batalha3.html',
                context,
            )
        
        
    if 'recomecar' in request.GET:
        player.boss_escolhido = ''
        player.boss_escolhido_atk = 0 
        player.contador_batalha3 = 0
        player.par_linha_coluna.clear()
        player.fim = False
        player.monstros_fase3.clear()
        player.poder_somado = 0
        player.batalhar = False
        player.save()
            
    player.batalha_em_andamento = False
    lista = player.batalha3lista
    player.comecou = False
    player.flip = False
    form = BotaoForm(request.POST or None)
    par_linha_coluna = player.par_linha_coluna

    player.fase_atual = 3
    player.save()

    

    for n in range(len(lista)):
        for i in range(5):
            lista[n][i]['i'] = 'global/img/sleeve.jpg'

    if request.method == 'POST':
        
        if 'comecar' in request.GET:
            player.boss_escolhido = ''
            player.boss_escolhido_atk = 0 
            player.contador_batalha3 = 0
            player.par_linha_coluna.clear()
            player.fim = False
            player.monstros_fase3.clear()
            player.poder_somado = 0
            player.save()
            
            player.resultado = 'l'
            player.batalha_em_andamento = True
            player.comecou = True
            player.fim = False
            player.monstros_fase3.clear()
            boss = random.randint(0,4)
            player.boss_escolhido = player.lista_boss[boss]['img']
            player.boss_escolhido_atk = player.lista_boss[boss]['atk']
            
            player.save()
            
            for n in range(len(lista)):
                for i in range(5):
                    lista[n][i]['v']= 'global/img/sleeveUsed.png'
                    lista[n][i]['t'] = 0
                    
            for imagem in player.lista_imagem:
                
                while True:
                    linha_monstro = random.randint(0, 3)
                    coluna_monstro = random.randint(0, 4)
                    if f'{linha_monstro}{coluna_monstro}' not in par_linha_coluna:
                        par_linha_coluna.append(f'{linha_monstro}{coluna_monstro}')
                        print(f'no if {par_linha_coluna}')
                        break
                    continue
                    
                lista[linha_monstro][coluna_monstro]['v'] = imagem['img']
                lista[linha_monstro][coluna_monstro]['atk'] = imagem['atk']

            player.par_linha_coluna.clear()
            player.poder_somado = 0
            player.vida_sobrando = 1
            player.contador_batalha3 = 0
            player.save()
            
        if 'batalhar' in request.GET :
            player.batalhar = True
            player.batalha_em_andamento = False
            boss_escolhido = player.boss_escolhido
            boss_escolhido_atk = int(player.boss_escolhido_atk)
            poder_somado = player.poder_somado
            if poder_somado > boss_escolhido_atk:
                player.resultado = 'w'
                player.save()
            else:
                player.resultado = 'l'
            player.save()
            context = {
            'sequencia': lista,
            'andamento': player.batalha_em_andamento,
            'flip': player.flip,
            'comecou': player.comecou,
            'boss_inimigo': boss_escolhido,
            'boss_Inimigo_atk': boss_escolhido_atk,
            'poder_somado': poder_somado,
            'fim': player.fim,
            'lista_aliados': player.monstros_fase3,
            'batalhar': player.batalhar
        }
            return render(
                request, 
                'contact/batalha3.html',
                context,
            )
            
        
        if 'flip' in request.GET:
            if form.is_valid():
                botao_id = form.cleaned_data['botao_id']
                linha, coluna = botao_id.split('-')
                linha = int(linha) - 1
                coluna = int(coluna) - 1
                lista[linha][coluna]['t'] = 1
                if lista[linha][coluna]['v'] != 'global/img/sleeveUsed.png' and lista[linha][coluna]['v'] not in player.monstros_fase3:
                    player.monstros_fase3.append(lista[linha][coluna]['v'])
                    player.poder_somado += lista[linha][coluna]['atk']
                lista[linha][coluna]['atk'] = 0
                player.flip = True
                player.comecou = True
                
                player.contador_batalha3 += 1
                player.boss_escolhido_atk += 10 * player.boss_escolhido_atk/100
                
                player.batalha_em_andamento = True
                player.save()

            else: 
                print('nao valido')
    
    
    boss_escolhido = player.boss_escolhido
    boss_escolhido_atk = int(player.boss_escolhido_atk)
    poder_somado = player.poder_somado
    vida_sobrando = player.vida_sobrando
    death_counter = 7 - player.contador_batalha3
    player.batalhar = False
    
    player.superou = player.poder_somado - player.boss_escolhido_atk
    
    context = {
        'andamento': player.batalha_em_andamento,
        'superou': player.superou,
        'sequencia': lista,
        'flip': player.flip,
        'comecou': player.comecou,
        'vida_sobrando': player.vida_sobrando,
        'poder_somado': player.poder_somado,
        'boss_inimigo': boss_escolhido,
        'boss_Inimigo_atk': boss_escolhido_atk,
        'poder_somado': poder_somado,
        'vida_sobrando':vida_sobrando,
        'contador_batalha': death_counter,
        'fim': player.fim,
        'lista_aliados': player.monstros_fase3,
        'batalhar': player.batalhar
    }
    return render(
        request, 
        'contact/batalha3.html',
        context,
    )



def resultado(request):
    player = get_object_or_404(Player, name='Yuji')
    resultado = player.resultado        
    life = player.life_round2savepoint
    energy = player.energy_pointFase1
    fase_atual = player.fase_atual
    context = {
        'resultado': resultado,
        'fase_atual': fase_atual,
        'vidafase2': life,
        'energia': energy
    }
    
    if resultado == 'w':
        player.delete()
        
    return render(
        request,
        'contact/resultado.html',
        context
    )

def history(request):
    player = get_object_or_404(Player, name='Yuji')

    if 'primeiro' in request.GET:
        player.historiaVariavel = 1
        player.save()
        return render(
        request,
        'contact/history.html',
        context={'variavel': player.historiaVariavel}
    )
    if 'segundo' in request.GET:
        player.historiaVariavel = 2
        player.save()
        return render(
        request,
        'contact/history.html',
        context={'variavel': player.historiaVariavel}
    )
    if 'terceiro' in request.GET:
        player.historiaVariavel = 3
        player.save()
        return render(
        request,
        'contact/history.html',
        context={'variavel': player.historiaVariavel}
    )
    if 'quarto' in request.GET:
        player.historiaVariavel = 4
        player.save()
        return render(
        request,
        'contact/history.html',
        context={'variavel': player.historiaVariavel}
    )
    if 'quinto' in request.GET:
        return redirect('contact:showdeck')

    player.historiaVariavel = 1
    player.save()
    context = {
        'variavel': player.historiaVariavel
    }
    
    return render(
        request,
        'contact/history.html',
        context
    )
    

def history2(request):
    player = get_object_or_404(Player, name='Yuji')

    if 'primeiro' in request.GET:
        player.historiaVariavel2 = 1
        player.save()
        return render(
        request,
        'contact/history2.html',
        context={'variavel': player.historiaVariavel2}
    )
    if 'segundo' in request.GET:
        url = reverse('contact:batalha2') + '?recomecar=True'
        return redirect(url)
    player.historiaVariavel2 = 1
    player.save()
    context = {
        'variavel': player.historiaVariavel2
    }
    
    return render(
        request,
        'contact/history2.html',
        context
    )
    
def history3(request):
    player = get_object_or_404(Player, name='Yuji')

    if 'primeiro' in request.GET:
        player.historiaVariavel3 = 1
        player.save()
        return render(
        request,
        'contact/history3.html',
        context={'variavel': player.historiaVariavel3}
    )
    if 'segundo' in request.GET:
        return redirect('contact:batalha3')

    player.historiaVariavel3 = 1
    player.save()
    context = {
        'variavel': player.historiaVariavel3
    }
    
    return render(
        request,
        'contact/history3.html',
        context
    )