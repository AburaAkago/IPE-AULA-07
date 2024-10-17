import os
diretorio = os.getcwd()
print(f'vc esta no diretorio {diretorio}')
texto = '''boa pa nois fml
vc ta preparado para uma imersão em python?
python foi criado por Power Guido Van Rossum
a comunidade python é muito legal'''

arq = open('saudacao.txt', 'w', encoding='utf-8')
arq.write(texto)
arq.close()