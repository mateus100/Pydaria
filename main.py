#Joguinho de ser um padeiro
import configparser
init = configparser.ConfigParser()

init.read_file(open('receita.ini'))

def apresentacao():
    nome = input("Olá qual é o seu nome? ")
    print(f'Como vai {nome}?')
    print(f'Você {nome} agora trabalha para uma padaria\n{nome}Pronto para aprender fazer pães?\nAperte a tecla ENTER: ')
    input("")


def receita():
   receita = init['RECEITA']['bolo']
   return receita

def fazerpao(ovo, sugar, trigo, sal, fermento):
    if ovo >= 1 and trigo >= 1:
        if sugar >= 5 and sal >= 1 and fermento >= 2:
           return "Ingredientes prontos"
        else:
           return "Veja se o açúcar e sal são o suficientes \n ou o fermento pode está em falta"
    else:
        return "Ingredientes insufissientes"

    pao = ovo + sugar + trigo + sal + fermento

    if pao < 9:
        return "O pão saiu ruim, deve está faltando alguma coisa..."
    elif pao >= 10:
        result = pao / 9
        return f'O total de pães são {result}'

apresentacao()

receita()
def make():
  ovo = int(input(f'{init["PERGUNTAS"]["ovo"]} ' ))

  sugar = int(input(f'{init["PERGUNTAS"]["acucar"]} ' ))

  trigo = int(input(f'{init["PERGUNTAS"]["trigo"]} '))

  sal = int(input(f'{init["PERGUNTAS"]["sal"]} ' ))

  fermento = int(input(f'{init["PERGUNTAS"]["fermento"]} '))

  print(fazerpao(ovo,sugar,trigo,sal,fermento))
make()
