import random 
nome = ''
grupos = [[],[],[],[]]
restrição = 1
lista_nomes = [
    [
'Adriel Faustino de Oliveira',
'Amanda Emi Yamasaki',
'Ana Werneck de Souza Dias',
'Felipe de Souza Lourenço',
'Fernanda Mayumi Sakamoto Iizuka',
'Guilherme Vinicius Afonso Dias de Freitas',
'Kim Ju Hyang',
'Leticia Amy Siramidu',
'Marcelo Tamay Honda',
'Maria Dulce Navarro de Britto Matos',
'Mateus Pamio Forcione de Oliveira e Souza',
'Milena da Silva Ramos',
'Paulo Sergio Almeida de Oliveira',
'Theo Borten Radesca Migliano',
'Vitor Tatiama Gouveia'],
    [
'André Menniti Pennini',
'Fernanda Mees Antunes', 
'Gabriel Grub Vidal da Silva',
'Henrique Nogueira Pedro Lindoso']]

while restrição >= 0:
    while len(lista_nomes[restrição]) > 0:
        for i in range(len(grupos)):
            try:
                nome = random.choice(lista_nomes[restrição])
                grupos[i].append(nome)
                lista_nomes[restrição].remove(nome)
            except:
                break
    restrição -= 1

for i in range (len(grupos)):
    print(f'''
Grupo {i+1}: 
''')
    for item in grupos[i]:
        print(f''' {item}''')