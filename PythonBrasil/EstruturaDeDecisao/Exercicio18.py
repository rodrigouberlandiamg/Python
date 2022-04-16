# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma
# data válida.
while True:
    data = input('Entre com a Data no formato dd/mm/yyyy: ')
    print(len(data))
    if len(data) != 10:
        print('Formato inválido. Entre com o formato DD/MM/YYYY.')
    else:
        dia = data[:2]
        mes = data[3:5]
        ano = data[6:10]
        print(data[2],data[5])
        if data[2] != '/' or data[5] != '/':
            print('Data Inválida.')
        elif dia.isnumeric() and mes.isnumeric() and ano.isnumeric():
            print(f'Dia {dia} mês {mes} ano {ano}')
            if mes in ('01','03','05','07','08','10','12'):
                if int(dia) <= 31 and int(mes) <= 12 and int(ano) <= 9999:
                    print(f'Data {data} esta no formato correto.')
                else:
                    print(f'Data {data} NÃO esta no formato correto.')
            elif mes in ('04','06','09','11'):
                if int(dia) <= 30 and int(mes) <= 12 and int(ano) <= 9999:
                    print(f'Data {data} esta no formato correto.')
                else:
                    print(f'Data {data} NÃO esta no formato correto.')
            elif mes == '02':
                if int(dia) <= 28 and int(mes) <= 12 and int(ano) <= 9999:
                    print(f'Data {data} esta no formato correto.')
                else:
                    print(f'Data {data} NÃO esta no formato correto.')
            break
        else:
            print(f'Data {data} NÃO esta no formato correto.')
print('FIM')
