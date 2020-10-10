from math import log2
from math import inf
from random import randint
from random import choices
from random import seed

'''

'''
def gibbsSampler(dna, k, t, n, pseudocounts = 1):

    seed()
    bestMotifs = motifs = [getMotif(p, k, randint(0, len(dna[0]) - k)) for p in dna]

    for j in range(1, n + 1):

        i = randint(0, t - 1)
        profile = buildProfile(motifs[:i] + motifs[i+1:], pseudocounts)

        probs = []
        for index in range(len(dna[i]) - k + 1):

            pattern = getMotif(dna[i], k, index)
            probs.append(computeProbability(pattern, profile))

        motifs[i] = getMotif(dna[i], k, randomNumber(probs))

        if score2(motifs) < score2(bestMotifs):
            bestMotifs = motifs

    return bestMotifs

'''
    
'''
def randomNumber(probs):

    population = [i for i in range(len(probs))]
    return choices(population, probs)[0]

'''
    
'''
def randomizedMotifSearch(dna, k, t, repeat = 1000, pseudocounts = 1):

    best = []
    for r in range(repeat):

        #bestMotifs = motifs = [getMotif(p, k, randint(0, len(dna[0]) - k)) for p in dna]

        bestMotifs = motifs = ['GTC', 'CCC', 'ATA', 'GCT']
        #while True:

        profile = buildProfile(motifs, pseudocounts)
        motifs = getMotifs(profile, dna)

        print(motifs)

        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs

         #else:
         #   break

        if best == []:
            best = bestMotifs
            
        elif score(bestMotifs) < score(best):
            best = bestMotifs

    return best

'''

'''
def getMotif(pattern, k, i):

    return pattern[i: i + k]


'''
    Função que obtém os k-mers mais prováveis
'''
def getMotifs(profile, dna):

    return [profileMostProbableKmer(p, len(profile['A']), profile) for p in dna]


'''
    Função que utiliza a abordagem de busca greedy
'''
def greedyMotifSearchWithPseudocounts(dna, k, t, pseudocounts = 0):

    bestMotifs = [pattern[0:k] for pattern in dna]

    g_len = len(dna[0])
    for i in range(0, g_len - k + 1):

        motifs = [dna[0][i: i + k]]
        for j in range(1, t):

            profile = buildProfile(motifs, pseudocounts)
            motifs.append(profileMostProbableKmer(dna[j], k, profile))

        if score2(motifs) < score2(bestMotifs):
            bestMotifs = motifs
        
    return bestMotifs

'''
    Função que constrói o profile
'''
def buildProfile(motifs, pseudocounts):

    profile = {'A':[], 'C':[], 'G':[], 'T':[]}
    for i, p in enumerate(transpose(motifs)):

        for nucleotide in ['A', 'C', 'G', 'T']:
            profile[nucleotide].append((p.count(nucleotide) + pseudocounts) / (len(p) + 4 * pseudocounts)) 

    return profile  

'''
    Função que busca pelo k-mer mais provável
'''
def profileMostProbableKmer(genome, k, profile):

    prob = -inf
    k_mer = ''

    g_len = len(genome)
    for i in range(0, g_len - k + 1):

        pattern = genome[i: i + k]
        p = computeProbability(pattern, profile)

        if p > prob:

            prob = p
            k_mer = pattern

    return k_mer


'''
    Função que calcula a probabilidade de um determinado padrão
    dado um perfil
'''
def computeProbability(pattern, profile):

    prob = 1
    for i, p in enumerate(pattern):

        prob *= profile[p][i]

    return prob

'''
    Função que resolve o problema do median string
'''
def medianString(dna, k):

    median = []
    distance = inf

    for pattern in [numberToPattern(p, k) for p in range(0, 4 ** k)]:

        dist = sum([d(pattern, genome) for genome in dna])
            
        if distance > dist:

            distance = dist
            median = [pattern]
            
        elif distance == dist:

            median.append(pattern)
    
    return median

'''
    
'''
def distanceBetweenPatternAndStrings(pattern, dna):

    return sum([d(pattern, genome) for genome in dna])

'''
    Função que calcula o k-mer que minimiza a distância de hamming
'''
def d(pattern, genome):

    g_len = len(genome)
    p_len = len(pattern)

    distance = []
    for i in range(0, g_len - p_len + 1):

        distance.append(hammingDistance(genome[i: i + p_len], pattern))

    return min(distance)

'''
    Função que obtém os motifs
'''
def motifEnumeration(genome_list, k, d):

    patterns = set()
    for genome in genome_list:

        g_len = len(genome)
        for i in range(0, g_len - k + 1):
            for neighbor in neighbors(genome[i: i + k], d):
                for line in genome_list:

                    if approximatePatternCount(line, neighbor, d) < 1:
                        break
                else:
                    patterns.add(neighbor)

    return list(patterns)

'''
    Função que calcula a entropia de um motif
'''
def score(motifs):

    scores = []
    for i, value in enumerate(transpose(motifs)):

        entrophy = 0
        for nucleotide in ['A', 'C', 'G', 'T']:

            prob = value.count(nucleotide) / len(value)
            entrophy += prob * log2(prob) if prob > 0 else 0

        scores.append(-entrophy)

    return sum(scores)

'''
    Função que calcula o score de um motif
'''
def score2(motifs):

    scores = []
    for i, value in enumerate(transpose(motifs)):

        sub_scores = []
        for nucleotide in ['A', 'C', 'G', 'T']:

            sub_scores.append(value.count(nucleotide))
            
        scores.append(len(value) - max(sub_scores))

    return sum(scores)


'''
    Função que obtém a transposta de um motif
'''
def transpose(motifs):

    t_motifs = [''] * len(motifs[0]) 
    for j in range(len(motifs[0])):

        for i in range(len(motifs)):

            t_motifs[j] += motifs[i][j]

    return t_motifs
    

'''
    Função que obtém os valores míninos do skew em um genoma
'''
def minSkew(genome):

    skew_list = skew(genome)
    min_skew = min(skew_list)

    min_list = []
    for i, val in enumerate(skew_list):

        if(val == min_skew):
            min_list.append(i)

    return min_list

'''
    Função que calcula a diferença entre as bases C e G
'''
def skew(genome):

    current = 0
    total   = [0] * (len(genome) + 1)
    dic = {'A': 0, 'T': 0, 'C': -1, 'G': +1}
    
    for i, val in enumerate(genome):

        current += dic[val]
        total[i+1] = current

    return total

'''
    Função que verifica um padrão aproximado em um genoma
'''
def approximatePatternMatching(genome, pattern, d):
    positions = []

    g_len = len(genome)
    p_len = len(pattern)
    
    for i in range(0, g_len - p_len + 1):

        if hammingDistance(genome[i: i + p_len], pattern) <= d:

            positions.append(i)
    
    return positions

'''
    Função que conta a quantidade de vezes que um
    determinado padrão aparece no genoma. Utiliza
    a distância de Hamming para verificar padrões
    aproximados.
'''
def approximatePatternCount(genome, pattern, d):

    return len(approximatePatternMatching(genome, pattern, d))

'''
    Função que obtém os padrões mais frequentes.
    Utiliza a distância de Hamming para obter padrões aproximados
'''
def frequentWordsWithMismatches(genome, k, d):

    dic = {}
    patterns = [numberToPattern(p, k) for p in range(0, 4 ** k)]

    for p in patterns:

        dic[p] = approximatePatternCount(genome, p, d)

    max_count = max(dic.values())
    
    f_patterns = []
    for pattern, count in dic.items():

        if(count == max_count):

            f_patterns.append(pattern)
            
    return f_patterns

'''
    Função que obtém os padrões mais frequentes.
    Utiliza os padrões complementares.
    Utiliza a distância de Hamming para obter padrões aproximados.
'''
def frequentWordsWithMismatchesAndReverseComplements(genome, k, d):

    dic = {}
    patterns = [numberToPattern(p, k) for p in range(0, 4 ** k)]
    c_patterns = [reverseComplement(p) for p in patterns]
    
    for p, cp in zip(patterns, c_patterns):

        dic[p] = approximatePatternCount(genome, p, d) + approximatePatternCount(genome, cp, d)

    max_count = max(dic.values())
    
    f_patterns = []
    for pattern, count in dic.items():

        if(count == max_count):

            f_patterns.append(pattern)
            
    return f_patterns

'''
    Função que obtém os vizinhos imediatos de um padrão
'''
def neighbors(pattern, d):

    if d == 0: return [pattern]

    if len(pattern) == 1: return ['A', 'T', 'C', 'G']

    neighborhood = []
    sulfix = pattern[1:]

    for n in neighbors(sulfix, d):

        if(hammingDistance(sulfix, n) < d):
            for x in ['A', 'T', 'C', 'G']:
                neighborhood.append(x + n)
                
        else:
            neighborhood.append(pattern[0] + n)

    return neighborhood

'''
    Função que calcula a distância de Hamming
'''
def hammingDistance(p, q):

    dist = 0
    for i in range(len(p)):

        if(p[i] != q[i]):
            dist +=1

    return dist

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
    Função que obtém o complemento de uma cadeia de DNA
'''
def reverseComplement(pattern):

    dic = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

    return ''.join([dic[i] for i in pattern[::-1]])


'''
    Função para efetuar leitura de um arquivo
'''
def readFile(name):

    return open(name, 'r').read()


'''
    Função para efetuar a escrita em um arquivo
'''
def writeFile(name, text):

    f = open(name, "w")
    f.write(text)
    f.close()

'''
    Função que transforma um array em uma string
'''
def toString(array):

    return '\n'.join(map(str, array))

'''
    Testando as funções
'''

# Exercise: 1.3
#print(toString(skew('GAGCCACCGCGATA')))

#genome = readFile('dataset_7_6.txt').split('\n')[0]
#print(toString(minSkew(genome)))

# Exercise: 1.4
#g1, g2 = readFile('dataset_9_3.txt').split('\n')[:2]
#print(hammingDistance(g1, g2))

#pattern, genome, d = readFile('dataset_9_4.txt').split('\n')[:3]
#print(toString(approximatePatternMatching(genome, pattern, int(d))))

#pattern, genome, d = readFile('dataset_9_6.txt').split('\n')[:3]
#print(approximatePatternCount(genome, pattern, int(d)))

#genome, k, d = readFile('dataset_9_7.txt').split()[:3]
#print(frequentWordsWithMismatches(genome, int(k), int(d)))

#genome, k, d = readFile('dataset_9_8.txt').split()[:3]
#print(frequentWordsWithMismatchesAndReverseComplements(genome, int(k), int(d)))

# Optional Exercise
#genome = ''.join(readFile('Salmonella_enterica.txt').split())

#min_skew = minSkew(genome)[0]
#genome = genome[min_skew - 200: min_skew + 200]
#print(frequentWordsWithMismatchesAndReverseComplements(genome, 9, 1))

# Exercise 1.8 Week 2
# genome, d = readFile('dataset_3014_4.txt').split()[:2]
# print(toString(neighbors(genome, int(d))))

# Exercise 1.2 Week 3
#f_list = readFile('dataset_156_8.txt').split()
#k, d = f_list[:2]
#genome_list = f_list[2:]
#print(toString(motifEnumeration(genome_list, int(k), int(d))))

# Exercise 1.4 Week 3
#f_list = readFile('dataset_158_9.txt').split()
#k = f_list[0]
#genome_list = f_list[1:]
#print(medianString(genome_list, int(k)))

# Exercise 1.5 Week 3
#f_list = readFile('dataset_159_3.txt').split('\n')
#genome, k = f_list[0], int(f_list[1])
#
#profile = {}
#for index, value in enumerate(['A', 'C', 'G', 'T']):  
#    profile[value] = list(map(float, f_list[index + 2].split()))
#
#print(profileMostProbableKmer(genome, k, profile))

# Exercise 1.5 Week 3
#f_list = readFile('dataset_159_5.txt').split()
#k = int(f_list[0])
#t = int(f_list[1])
#dna = f_list[2:]

#print(toString(greedyMotifSearch(dna, k, t)))


# Exercise 1.6 Week 3
#f_list = readFile('dataset_160_9.txt').split()
#k = int(f_list[0])
#t = int(f_list[1])
#dna = f_list[2:]

#print(toString(greedyMotifSearch(dna, k, t)))

# Exercise 1.7 Week 3
#f_list = readFile('dataset_5164_1.txt').split()
#pattern = f_list[0]
#dna = f_list[1:]

#print(distanceBetweenPatternAndStrings(pattern, dna))

# Exercise 1.7 Week 3
#f_list = readFile('dataset_163_4.txt').split()
#k = int(f_list[0])
#t = int(f_list[1])
#n = int(f_list[2])
#dna = f_list[3:]

#R = 20
#seed()

#BestMotifs = gibbsSampler(dna, k, t, n)
#for i in range(R):
#    m = gibbsSampler(dna, k, t, n)
#    if score2(m) < score2(BestMotifs):
#        BestMotifs = m
#
#print(toString(BestMotifs))

dna = ['ATGAGGTC', 'GCCCTAGA', 'AAATAGAT', 'TTGTGCTA']
randomizedMotifSearch(dna, 3, 4, 1)
