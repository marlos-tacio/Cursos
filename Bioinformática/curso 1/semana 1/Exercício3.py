'''

'''
def reverseComplement(pattern):

    dic = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

    return ''.join([dic[i] for i in pattern[::-1]])

'''
    Leitura do arquivo
'''
def readFile(name):

    return open(name, 'r').read()


    
text = readFile('Entrada3.txt')
output = reverseComplement(text)

print(output)
