'''

'''
def patternMatching(pattern, genome):

    index = []
    g_len = len(genome)
    p_len = len(pattern)

    for i in range(0, g_len - p_len + 1):

        if(genome[i:i + p_len] == pattern):

           index.append(i)

    return ' '.join(map(str, index))

'''
    Leitura do arquivo
'''
def readFile(name):

    return open(name, 'r').read()


    
genome = readFile('Opcional1.txt')
output = patternMatching('CTTGATCAT', genome)

print(output)
