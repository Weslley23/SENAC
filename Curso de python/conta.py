'''
Faça um algoritmo para ler dois números e imprimir o maior, o menor ou então dizer se são iguais. \n')
'''
continuar = 's'
while continuar.lower() == 's':
    N1 = float(input('Digite o valor desejado para N1: \n'))
    N2 = float(input('Digite o valor desejado para N2: \n'))
    
    if N1 > N2:
        print(f'O maior número é {N1} e o menor é {N2}.')
    elif N1 < N2:
        print(f'O maior número é {N2} e o menor é {N1}.')
    else:
        print(f'Os números {N1} e {N2} são iguais.')
    
    continuar = input('Deseja continuar? (Digite s para sim) ')
