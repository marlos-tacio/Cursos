'''
    Função que encontra os motifs
'''
def motifEnumeration(dna, k, d):

    patterns = set()

    

'''
    Função que obtém os vizinhos imediatos de um padrão
'''
def neighbors(pattern, d):

    if d == 0: return pattern

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
