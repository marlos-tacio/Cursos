def betterClumpFinding(genome, k, L, t):

    text = genome[0:L]
    clump = [0] * (4 ** k)
    
    f_array = computingFrequencies(text, k)
    for index, value in enumerate(f_array):

        if(value >= t):
            clump[index] = 1

    g_len = len(genome)
    for i in range(1, g_len - L + 1):

        f_index = i - 1
        firstPattern = genome[f_index: f_index + k]
        index = patternToNumber(firstPattern)
        f_array[index] -= 1

        l_index = i + L
        lastPattern = genome[l_index - k: l_index]
        index = patternToNumber(lastPattern)
        f_array[index] += 1

        if(f_array[index] >= t):
            clump[index] = 1

    f_patterns = []
    for index, value in enumerate(clump):

        if value == 1:
            f_patterns.append(numberToPattern(index, k))

    return f_patterns

def clumpFinding(genome, k, L, t):

    g_len = len(genome)

    clump_set = set()
    for i in range(0, g_len - L + 1):

        text = genome[i:i + L]
        clump_set.update(fasterFrequentWords2(text, k, t))

    return clump_set


'''
    Trasforma um padrão em um número único    
'''
def patternToNumber(pattern):

    total = 0
    dic = {'A':0, 'C':1, 'G':2, 'T':3}
    
    for i, val in enumerate(pattern[::-1]):
        
        total += dic[val] * 4 ** i

    return total

'''
    Trasforma um número em um padrão do genoma
'''
def numberToPattern(number, k):

    dic = {0:'A', 1:'C', 2:'G', 3:'T'}

    div = number // 4
    mod = number %  4

    if(k < 1):
        
        return ''

    return numberToPattern(div, k - 1) + dic[mod]

'''

'''
def fasterFrequentWords2(text, k, t):

    f_array = computingFrequencies(text, k)
    
    f_patterns = []
    for index, value in enumerate(f_array):

        if(value >= t):

            f_patterns.append(numberToPattern(index, k))
            
    return f_patterns

'''

'''
def fasterFrequentWords(text, k):

    f_array = computingFrequencies(text, k)
    max_count = max(f_array)

    f_patterns = []
    for index, value in enumerate(f_array):

        if(value == max_count):

            f_patterns.append(numberToPattern(index, k))
            
    return f_pattern

'''

'''
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

'''
def computingFrequencies(text, k):
    
    t_len = len(text)
    f_array = [0] * (4 ** k)

    for i in range(0, t_len - k + 1):

        pattern = text[i:i + k]
        f_array[patternToNumber(pattern)] += 1

    return f_array

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


def writeFile(name, text):

    f = open(name, "w")
    f.write(text)
    f.close()
    
text = readFile('Opcional2.txt')
output = betterClumpFinding('AAAACGTCGAAAAA', 2, 4, 2)

print(output)

#writeFile('saida.txt', ' '.join(map(str, output)))
