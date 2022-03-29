#import math
from math import sqrt, floor
num = int(input('Digite o numero: '))
#raiz = math.sqrt(num)
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num,floor(raiz)))