# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de
# modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros,
# isto é, quantos quilômetros cada um desses carros faz com um litro de combustível.
# Calcule e mostre:
#
#     O modelo do carro mais econômico;
#     Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma
#     distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina
#     custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve
#     ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução
#     do programa.
#
# Comparativo de Consumo de Combustível
#
# Veículo 1
# Nome: fusca
# Km por litro: 7
# Veículo 2
# Nome: gol
# Km por litro: 10
# Veículo 3
# Nome: uno
# Km por litro: 12.5
# Veículo 4
# Nome: Vectra
# Km por litro: 9
# Veículo 5
# Nome: Peugeout
# Km por litro: 14.5
#
# Relatório Final
#  1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
#  2 - gol             -   10.0 -  100.0 litros - R$ 225.00
#  3 - uno             -   12.5 -   80.0 litros - R$ 180.00
#  4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
#  5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
# O menor consumo é do peugeout.

carros = {}
for x in range(5):
    carros[f'modelo_{x}'] = str(input(f'Entre com o modelo do veiculo: '))
    carros[f'consumo_{x}'] = float(input(f'Entre com o consumo do veiculo {carros[f"modelo_{x}"]}: '))
#print(carros)
count = 0
print(f'Relatorio FINAL:')
for x in carros:
    if 'modelo' in x:
        count += 1
        print(f'{count} - {carros[x]}',end='    -     ')
    elif 'consumo' in x:
        print(f'{carros[x]}', end='    -     ')
        print(f'{1000/carros[x]:.2f}', end='    -     ')
        print(f'R${(1000/carros[x])*2.25:.2f}')