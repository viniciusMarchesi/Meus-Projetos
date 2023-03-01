print('Seja Bem vindo ao Quiz!')
answer_user = input('Quer começar o Quiz? (s/n): ')

if answer_user != 's':
    quit()

score = 0

print('Começando...')   

#1
print('1- Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Ubisoft \n (B) Rockstar Games \n (C) Activision \n (D) EA \n') 
answer_1= input('Resposta: ')

if answer_1 == 'B' :
    print('Acertou!')
    score = score + 1
else :
    print ('Errou!')

#2
print('2- De quem é a famosa frase “Penso, logo existo? \n (A) Platão \n (B) Galileu Galilei \n (C) Descartes \n (D) Sócrates \n') 
answer_2= input('Resposta: ')

if answer_2 == 'C' :
    print('Acertou!')
    score = score + 1
else :
    print ('Errou!')

#3
print('3- De onde é a invenção do chuveiro elétrico? \n (A) França \n (B) Inglaterra \n (C) Austrália  \n (D) Brasil \n') 
answer_3= input('Resposta: ')

if answer_3 == 'D' :
    print('Acertou!')
    score = score + 1
else :
    print ('Errou!')

#4
print('4- Quais o menor e o maior país do mundo? \n (A) Vaticano e Rússia  \n (B) Mônaco e Canadá \n (C) Malta e Estados Unidos \n (D) Nauru e China \n') 
answer_4= input('Resposta: ')

if answer_4 == 'A' :
    print('Acertou!')
    score = score + 1
else :
    print ('Errou!')

#5
print('5- Qual o nome do presidente do Brasil que ficou conhecido como Jango? \n (A) Jânio Quadros \n (B) João Goulart \n (C) Getúlio Vargas \n (D) João Figueiredo \n') 
answer_5= input('Resposta: ')

if answer_5 == 'B' :
    print('Acertou!')
    score = score + 1
else :
    print ('Errou!') 

#6
print('6- Quantas casas decimais tem o número pi? \n (A) Centenas \n (B) Milhares \n (C) Infinitas \n (D) Vinte \n') 
answer_6= input('Resposta: ')

if answer_6 == 'C' :
    print('Acertou!')
    score = score + 1
else :
    print ('Errou!')

#7
print('7- Atualmente, quantos elementos químicos a tabela periódica possui? \n (A) a) 113 \n (B) 109 \n (C) 108 \n (D) 118 \n') 
answer_7= input('Resposta: ')

if answer_7 == 'D' :
    print('Acertou!')
    score = score + 1
else :
    print ('Errou!')

#8
print('8- Quais as duas datas que são comemoradas em novembro? \n (A) Independência do Brasil e Dia da Bandeira \n (B) Proclamação da República e Dia Nacional da Consciência Negra \n (C) Dia de Finados e Dia Nacional do Livro \n (D) Black Friday e Dia da Árvore \n') 
answer_8= input('Resposta: ')

if answer_8 == 'B' :
    print('Acertou!')
    score = score + 1
else :
    print ('Errou!')

#9
print('9- Quanto tempo a luz do Sol demora para chegar à Terra? \n (A) 12 minutos \n (B) 1 dia \n (C) 12 horas \n (D) 8 minutos \n') 
answer_9= input('Resposta: ')

if answer_9 == 'D' :
    print('Acertou!')
    score = score + 1
else :
    print ('Errou!') 

#10
print('10- O que a palavra legend significa em português? \n (A) Legenda \n (B) Conto \n (C) Lenda \n (D) Legendário \n') 
answer_10= input('Resposta: ')

if answer_10 == 'C' :
    print('Acertou!')
    score = score + 1
else :
    print ('Errou!')

print(f'O Quiz Acabou! Pontuação: {score}/10')    
