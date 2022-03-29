from random import randint
texto = 'este'
if texto[0] in 'aeiou':
    print('Tem vogal')

while True:
    print('Vai')
    break
i = 0
for c in range(0, 10, 3):
    print('c: ',c)
    #i+=3
    #print(i)

x = randint(10,100)
print(x)
#resp = str(input('Digite uma letra: ')).strip().upper()[0]
resp = str(input('Digite uma letra: ')).upper().strip()[1]
print(resp)