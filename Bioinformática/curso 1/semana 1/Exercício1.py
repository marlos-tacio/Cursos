'''
    Contagem de um padrão em um texto
'''
def patternCount(text, pattern):
    count = 0
    t_len = len(text)
    p_len = len(pattern)

    for i in range(0, t_len - p_len + 1):

        if(text[i:i + p_len] == pattern):

           count += 1

    return count


'''
    Leitura do arquivo
'''
def readFile(name):

    return open(name, 'r').read()


    
text, pattern = readFile('Entrada1.txt').split('\n')[:2]
output = patternCount(text, pattern)

print(output)
