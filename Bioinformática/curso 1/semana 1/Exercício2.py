def frequentWords(text, k):

    patterns = {}
    t_len = len(text)
    
    for i in range(0, t_len - k + 1):

        pattern = text[i:i + k]
        count = patternCount(text, pattern)

        patterns[pattern] = count

    max_count = max(patterns.values())

    f_patterns = []
    for pattern, count in patterns.items():

        if(count == max_count):

            f_patterns.append(pattern)
            
    return f_patterns


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


    
text, pattern = readFile('Entrada2.txt').split('\n')[:2]
output = frequentWords(text, int(pattern))

print(output)
