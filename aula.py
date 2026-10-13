print("-"*50)
print("Bem vindo ao Quiz sobre conhecimentos gerais. Nesse Quiz, temos 10 questões que vão valer 1,0 para cada. Porém, cada questão que vai passando fica mais difícil. Então tome cuidado quando for responder. Lembrando que o seu resultado final irá definir o seu Qi. Como: (1 a 4: Qi Baixo.), (5 a 7: Qi médio.), (8 a 9: Qi alto) e (10: Qi superior).")
print("-"*50)
print("Antes de Começar, cadastre o seu nome e a sua idade.")
print("-"*50)
list=[]
while True:
    nome=input("Nome do Usuário: ")
    list.append(nome)
    idade=input("Idade: ")
    list.append(idade)
    print(list)
    print("Está correto? Digite (S) para Sim e (N) para (Não).")
    ps=input(": ")
    if ps=="S" or ps=="s":
        print("Cadastrado. Iremos começa em: ")
        break
    elif ps=="N" or ps=="n":
        del list[0]
        del list[0]
        print("-"*50)
        print("O seu cadastro foi apagado. Insira normalmente.")
        print("-"*50)
from time import sleep
for cont in range(3, -1, -1):
    print(cont)
    sleep(1)
print("-"*50)
print("-"*50)
acerto=0
erro=0
a=[]
e=[]
while True:
    print("-"*50)
    print("Pergunta 1. Qual a Capital dos Estados Unidos.")
    print("a) Brasília.")
    print("b) Carlifórnia.")
    print("c) Flórida.")
    print("d) Washington.")
    print("e) Texas.")
    print("-"*50)
    p1=input("Resposta: ")
    if p1=="D" or p1=="d":
        acerto+=1
        a.append("1")
        break
    elif p1=="A" or p1=="a" or p1=="B" or p1=="b" or p1=="C" or p1=="c" or p1=="E" or p1=="e":
        erro+=1
        e.append(" 1")
        break
    else:
        print("-"*50)
        print("Resposta não conhecida, tente normalmente.")
        print("-"*50)
while True:
    print("-"*50)
    print("Pergunta 2. Qual o Oceano banha o Brasil?")
    print("a) Oceano Atlantido.")
    print("b) Oceano Pacífico. ")
    print("c) Oceano Índico. ")
    print("d) Oceano Ártico. ")
    print("e) Oceano Antártico. ")
    print("-"*50)
    p2=input("Resposta: ")
    if p2=="A" or p2=="a":
        acerto+=1
        a.append(" 2")
        break
    elif p2=="B" or p2=="b" or p2=="C" or p2=="c" or p2=="D" or p2=="d" or p2=="E" or p2=="e":
        erro+=1
        e.append(" 2")
        break
    else:
        print("-"*50)
        print("Resposta não conhecida, tente normalmente.")
        print("-"*50)
while True:
    print("-"*50)
    print("Pergunta 3. Onde fica o templo de kiyomizu-dera, um dos monumentos mais famosos do japão?")
    print("a) Tokyo/tóquio.")
    print("b) Osaka. ")
    print("c) Yokohama. ")
    print("d) Quioto. ")
    print("e) Nagoia. ")
    print("-"*50)
    p3=input("Resposta: ")
    if p3=="D" or p3=="d":
        acerto+=1
        a.append(" 3")
        break
    elif p3=="A" or p3=="a" or p3=="B" or p3=="b" or p3=="C" or p3=="c" or p3=="E" or p3=="e":
        erro+=1
        e.append(" 3")
        break
    else:
        print("-"*50)
        print("Resposta não conhecida, tente normalmente.")
        print("-"*50)
while True:
    print("-"*50)
    print("Pergunta 4. Qual o nome completo do autor de Dom Casmurro?")
    print("a) José de Anchieta.")
    print("b) Gregório de Matos. ")
    print("c) Gonçalves Dias. ")
    print("d) José de Alencar. ")
    print("e) Machado de Assis. ")
    print("-"*50)
    p4=input("Resposta: ")
    if p4=="E" or p4=="e":
        acerto+=1
        a.append(" 4")
        break
    elif p4=="A" or p4=="a" or p4=="B" or p4=="b" or p4=="C" or p4=="c" or p4=="D" or p4=="d":
        erro+=1
        e.append(" 4")
        break
    else:
        print("-"*50)
        print("Resposta não conhecida, tente normalmente.")
        print("-"*50)
while True:
    print("-"*50)
    print("Pergunta 5. Qual o maior país da América Latina em extensão territorial?")
    print("a) Brasil.")
    print("b) Agentina. ")
    print("c) Colômbia. ")
    print("d) Peru. ")
    print("e) Uruguai. ")
    print("-"*50)
    p5=input("Resposta: ")
    if p5=="A" or p5=="a":
        acerto+=1
        a.append(" 5")
        break
    elif p5=="B" or p5=="b" or p5=="C" or p5=="c" or p5=="D" or p5=="d" or p5=="E" or p5=="e":
        erro+=1
        e.append(" 5")
        break
    else:
        print("-"*50)
        print("Resposta não conhecida, tente normalmente.")
        print("-"*50)
while True:
    print("-"*50)
    print("Pergunta 6. Em que ano o Brasil foi descoberta por Pedro Álvares Cabral?")
    print("a) 1510.")
    print("b) 1512. ")
    print("c) 1509. ")
    print("d) 1500. ")
    print("e) 1503. ")
    print("-"*50)
    p6=input("Resposta: ")
    if p6=="D" or p6=="d":
        acerto+=1
        a.append(" 6")
        break
    elif p6=="A" or p6=="a" or p6=="B" or p6=="b" or p6=="C" or p6=="c" or p6=="E" or p6=="e":
        erro+=1
        e.append(" 6")
        break
    else:
        print("-"*50)
        print("Resposta não conhecida, tente normalmente.")
        print("-"*50)
while True:
    print("-"*50)
    print("Pergunta 7. Qual o maior cordilheira do mundo?")
    print("a) Cordilheira Australiana.")
    print("b) Cordilheira dos Atlas. ")
    print("c) Cordilheira do Cáusaso. ")
    print("d) cordilheira Elbruz. ")
    print("e) Cordilheira do Andes. ")
    print("-"*50)
    p7=input("Resposta: ")
    if p7=="E" or p7=="e":
        acerto+=1
        a.append(" 7")
        break
    elif p7=="A" or p7=="a" or p7=="B" or p7=="b" or p7=="C" or p7=="c" or p7=="D" or p7=="d":
        erro+=1
        e.append(" 7")
        break
    else:
        print("-"*50)
        print("Resposta não conhecida, tente normalmente.")
        print("-"*50)
while True:
    print("-"*50)
    print("Pergunta 8. Qual País que tem mais ilhas do Mundo?")
    print("a) Indonésia.")
    print("b) Suécia. ")
    print("c) Estados Unidos. ")
    print("d) Austrália. ")
    print("e) Filipinas. ")
    print("-"*50)
    p8=input("Resposta: ")
    if p8=="B" or p8=="b":
        acerto+=1
        a.append(" 8")
        break
    elif p8=="A" or p8=="a" or p8=="C" or p8=="c" or p8=="D" or p8=="d" or p8=="E" or p8=="e":
        erro+=1
        e.append(" 8")
        break
    else:
        print("-"*50)
        print("Resposta não conhecida, tente normalmente.")
        print("-"*50)
while True:
    print("-"*50)
    print("Pergunta 9. Qual o país de origem da marca de automoveis Audi?")
    print("a) Itália.")
    print("b) Japão. ")
    print("c) Estados Unidos. ")
    print("d) Alemanha. ")
    print("e) Orlanda. ")
    print("-"*50)
    p9=input("Resposta: ")
    if p9=="D" or p9=="d":
        acerto+=1
        a.append(" 9")
        break
    elif p9=="A" or p9=="a" or p9=="B" or p9=="b" or p9=="C" or p9=="c" or p9=="E" or p9=="e":
        erro+=1
        e.append(" 9")
        break
    else:
        print("-"*50)
        print("Resposta não conhecida, tente normalmente.")
        print("-"*50)
while True:
    print("-"*50)
    print("Pergunta 10. Qual é a rocha mais abundante da crosta terrestre?")
    print("a) Ferro.")
    print("b) Hidrogênio. ")
    print("c) Magmáticas. ")
    print("d) Oxigenio. ")
    print("e) Feldspato. ")
    print("-"*50)
    p10=input("Resposta: ")
    if p10=="E" or p10=="e":
        acerto+=1
        a.append(" 10")
        break
    elif p10=="A" or p10=="a" or p10=="B" or p10=="b" or p10=="C" or p10=="c" or p10=="D" or p10=="d":
        erro+=1
        e.append("10")
        break
    else:
        print("-"*50)
        print("Resposta não conhecida, tente normalmente.")
        print("-"*50)
print("Resultado saindo em:")
from time import sleep
for cont in range(5, -1, -1):
    print(cont)
    sleep(1)
if acerto==1 or acerto==2 or acerto==3 or acerto==4:
    print("-"*50)
    print("Seu Qi é Baixo, precisa melhorar mais :-( . Você acertou( "+str(acerto)+" ) nas questões, "+str(a)+" e errou, ("+str(erro)+") nas questões, "+str(e)+". Mas não fique desanimado, pelo menos você tentou. Com os nossos erros, aprendemos mais coisas que você imagina, é assim que Deus nos faz para o nosso melhor, ele mostra o seu erro e você corrige com ajuda dele. Se quiser tentar de novo, estremos muito feliz <-). Muito Obrigado por Jogar.")
    print("-"*50)
    while True:
        print("Quer ver o Gabarito? Digite (S) para disser Sim e (N) para disser (Não).")
        print("-"*50)
        gabarito=input(": ")
        if gabarito=="S":
            print("-"*50)
            print("GABARITO")
            print("-"*50)
            print("Q1 = d")
            print("Waskington D.C")
            print("-"*50)
            print("Q2 = a")
            print("Oceano Atlântico")
            print("-"*50)
            print("Q3 = d")
            print("Quioto")
            print("-"*50)
            print("Q4 = e")
            print("Machado de Assis")
            print("-"*50)
            print("Q5 = a")
            print("Brasil")
            print("-"*50)
            print("Q6 = d")
            print("1500")
            print("-"*50)
            print("Q7 = e")
            print("Cordilheira da Andes")
            print("-"*50)
            print("Q8 = b")
            print("Suésia")
            print("-"*50)
            print("Q9 = d")
            print("Alemanha")
            print("-"*50)
            print("Q10 = e")
            print("Feldspato")
            print("-"*50)
            print("-"*50)
            print("Sua Resposta.")
            print("-"*50)
            print("Q1 = "+(p1))
            print("-"*50)
            print("Q2 = "+(p2))
            print("-"*50)
            print("Q3 = "+(p3))
            print("-"*50)
            print("Q4 = "+(p4))
            print("-"*50)
            print("Q5 = "+(p5))
            print("-"*50)
            print("Q6 = "+(p6))
            print("-"*50)
            print("Q7 = "+(p7))
            print("-"*50)
            print("Q8 = "+(p8))
            print("-"*50)
            print("Q9 = "+(p9))
            print("-"*50)
            print("Q10 = "+(p10))
            print("-"*50)
            break
        elif gabarito=="N":
            break
        else:
            print("-"*50)
            print("Erro, resposta não indentificada. Tente Normalmente.")
            print("-"*50)
elif acerto==5 or acerto==6 or acerto==7:
    print("-"*50)
    print("Seu Qi está na média,:-| . Você acertou( "+str(acerto)+" ) nas questões, "+str(a)+" e errou, ("+str(erro)+") nas questões, "+str(e)+". Não está ruim e não está bom, mas é um resultado interessante, mas não esqueça que quanto mais treinar, melhor você fica. Deus Abençoe você sempre e muito obrigado por jogar <-).")
    print("-"*50)
    while True:
        print("Quer ver o Gabarito? Digite (S) para disser Sim e (N) para disser (Não).")
        print("-"*50)
        gabarito=input(": ")
        if gabarito=="S" or gabarito=="s":
            print("-"*50)
            print("GABARITO")
            print("-"*50)
            print("Q1 = d")
            print("Waskington D.C")
            print("-"*50)
            print("Q2 = a")
            print("Oceano Atlântico")
            print("-"*50)
            print("Q3 = d")
            print("Quioto")
            print("-"*50)
            print("Q4 = e")
            print("Machado de Assis")
            print("-"*50)
            print("Q5 = a")
            print("Brasil")
            print("-"*50)
            print("Q6 = d")
            print("1500")
            print("-"*50)
            print("Q7 = e")
            print("Cordilheira da Andes")
            print("-"*50)
            print("Q8 = b")
            print("Suésia")
            print("-"*50)
            print("Q9 = d")
            print("Alemanha")
            print("-"*50)
            print("Q10 = e")
            print("Feldspato")
            print("-"*50)
            print("-"*50)
            print("Sua Resposta.")
            print("-"*50)
            print("Q1 = "+(p1))
            print("-"*50)
            print("Q2 = "+(p2))
            print("-"*50)
            print("Q3 = "+(p3))
            print("-"*50)
            print("Q4 = "+(p4))
            print("-"*50)
            print("Q5 = "+(p5))
            print("-"*50)
            print("Q6 = "+(p6))
            print("-"*50)
            print("Q7 = "+(p7))
            print("-"*50)
            print("Q8 = "+(p8))
            print("-"*50)
            print("Q9 = "+(p9))
            print("-"*50)
            print("Q10 = "+(p10))
            print("-"*50)
            break
        elif gabarito=="N" or gabarito=="n":
            break
        else:
            print("-"*50)
            print("Erro, resposta não indentificada. Tente Normalmente.")
            print("-"*50)
elif acerto==8 or acerto==9:
    print("-"*50)
    print("Seu Qi é alto, :-) . Você acertou( "+str(acerto)+" ) nas questões, "+str(a)+" e errou, ("+str(erro)+") nas questões, "+str(e)+". Muito bem, sensacional o seu desenpenho, foi uma bela pontuação, continue se esforçado e nunca perca a sua esperança que Deus deu para você. Muito obrigado por jogar <-).")
    print("-"*50)
    while True:
        print("Quer ver o Gabarito? Digite (S) para disser Sim e (N) para disser (Não).")
        print("-"*50)
        gabarito=input(": ")
        if gabarito=="S" or gabarito=="s":
            print("-"*50)
            print("GABARITO")
            print("-"*50)
            print("Q1 = d")
            print("Waskington D.C")
            print("-"*50)
            print("Q2 = a")
            print("Oceano Atlântico")
            print("-"*50)
            print("Q3 = d")
            print("Quioto")
            print("-"*50)
            print("Q4 = e")
            print("Machado de Assis")
            print("-"*50)
            print("Q5 = a")
            print("Brasil")
            print("-"*50)
            print("Q6 = d")
            print("1500")
            print("-"*50)
            print("Q7 = e")
            print("Cordilheira da Andes")
            print("-"*50)
            print("Q8 = b")
            print("Suésia")
            print("-"*50)
            print("Q9 = d")
            print("Alemanha")
            print("-"*50)
            print("Q10 = e")
            print("Feldspato")
            print("-"*50)
            print("-"*50)
            print("Sua Resposta.")
            print("-"*50)
            print("Q1 = "+(p1))
            print("-"*50)
            print("Q2 = "+(p2))
            print("-"*50)
            print("Q3 = "+(p3))
            print("-"*50)
            print("Q4 = "+(p4))
            print("-"*50)
            print("Q5 = "+(p5))
            print("-"*50)
            print("Q6 = "+(p6))
            print("-"*50)
            print("Q7 = "+(p7))
            print("-"*50)
            print("Q8 = "+(p8))
            print("-"*50)
            print("Q9 = "+(p9))
            print("-"*50)
            print("Q10 = "+(p10))
            print("-"*50)
            break
        elif gabarito=="N" or gabarito=="n":
            break
        else:
            print("-"*50)
            print("Erro, resposta não indentificada. Tente Normalmente.")
            print("-"*50)
elif acerto==10:
    print("-"*50)
    print("Fantastico!! Você tem um Qi Superior :-D. Você acertou( "+str(acerto)+" pontos ) nas questões, "+str(a)+" e errou nenhuma. Parabéns, você conseguiu acertar tudo sem errar nenhuma. Isso é fantastico, continua sendo essa tipo de pessoa, esforse para conquistar os seus objetivos e nunca deixe para atrás naquilo que Deus deu paa você. Muito obrigado por jogar <-).")
    print("-"*50)
    while True:
        print("Quer ver o Gabarito? Digite (S) para Sim e (N) para (Não).")
        print("-"*50)
        gabarito=input(": ")
        if gabarito=="S" or gabarito=="s":
            print("-"*50)
            print("GABARITO")
            print("-"*50)
            print("Q1 = d")
            print("Waskington D.C")
            print("-"*50)
            print("Q2 = a")
            print("Oceano Atlântico")
            print("-"*50)
            print("Q3 = d")
            print("Quioto")
            print("-"*50)
            print("Q4 = e")
            print("Machado de Assis")
            print("-"*50)
            print("Q5 = a")
            print("Brasil")
            print("-"*50)
            print("Q6 = d")
            print("1500")
            print("-"*50)
            print("Q7 = e")
            print("Cordilheira da Andes")
            print("-"*50)
            print("Q8 = b")
            print("Suésia")
            print("-"*50)
            print("Q9 = d")
            print("Alemanha")
            print("-"*50)
            print("Q10 = e")
            print("Feldspato")
            print("-"*50)
            print("-"*50)
            print("Sua Resposta.")
            print("-"*50)
            print("Q1 = "+(p1))
            print("-"*50)
            print("Q2 = "+(p2))
            print("-"*50)
            print("Q3 = "+(p3))
            print("-"*50)
            print("Q4 = "+(p4))
            print("-"*50)
            print("Q5 = "+(p5))
            print("-"*50)
            print("Q6 = "+(p6))
            print("-"*50)
            print("Q7 = "+(p7))
            print("-"*50)
            print("Q8 = "+(p8))
            print("-"*50)
            print("Q9 = "+(p9))
            print("-"*50)
            print("Q10 = "+(p10))
            print("-"*50)
            break
        elif gabarito=="N" or gabarito=="n":
            break
        else:
            print("-"*50)
            print("Erro, resposta não indentificada. Tente Normalmente.")
            print("-"*50)
print("Se queira fazer de novo, é só pressionar o botão com a seta para cima para fazer de novo no começo.")
