import re
# padrao = '[0-9][a-z][0-9]'
# texto = '123 1a2 1cc aa1'
# resposta = re.search(padrao,texto)
# print(resposta.group())
#
# padrao_email = '\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}'
# texto_email = 'djlaifjilds fjsjfois 1334243 rodrigoo@tribanco.com.br djwkldjlksd 234234 kwdfpj5345rpp'
# resposta_email = re.search(padrao_email,texto_email)
# print(resposta_email.group())

padrao_telefone = '[0-9]{2}[0-9]{4,5}[0-9]{4}'
texto_telefone = '1246 a dfsddf sdf f406f 4s04f 0s65f40 3432357364  da da da  dad 34992825843 ada dade4333'
resposta_telefone = re.search(padrao_telefone,texto_telefone)
print(resposta_telefone.group())