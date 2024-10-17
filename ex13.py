import os
arq=open(r'saudacao.txt','w')
arq.write('1234567890abcd')
arq.close()

arq = open(r'saudacao.txt')
arq.seek(5)
print(arq.read(1))
arq.close()
