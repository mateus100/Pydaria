#Quanto lucra uma padaria por pão feito

def receita():
   print("Pronto para aprender fazer pães? Aperte qualquer tecla: ")
   input("")
   print("A receita para fazer 1 pão é:\n 1 Ovo \n 5 colheres de Açúcar \n 1 colher de sopa de sal \n 1 kg de farinha de trigo \n 2 tabletes de fermento...")

receita()
print("Quantos pães fará hoje? ")
ovo = int(input("Quantos ovos? "))

sugar = int(input("Quantas colheres de açúcar? "))

trigo = int(input("Quantos kg de farinha de trigo? "))

sal = int(input("Quantas colheres de Sal? "))

fermento = int(input("Quantos tabletes de fermento? "))

def fazerpao(ovo, sugar, trigo, sal, fermento):
    if ovo >= 1 and trigo >= 1:
        if sugar >= 5 and sal >= 1 and fermento >= 2:
           print("Ingredientes prontos")
        else:
           print("Veja se o açúcar e sal são o suficientes \n ou o fermento pode está em falta")
    else:
        print("Ingredientes insufissientes")
    
    pao = ovo + sugar + trigo + sal + fermento

    if pao < 9:
        print("O pão saiu ruim, deve está faltando alguma coisa...")
    elif pao >= 10:
        result = pao % 9
        print("O total de pães são %d " %(result) )
       

fazerpao(ovo,sugar,trigo,sal,fermento)
