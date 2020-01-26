# ADN REPLICATION , SEQUENCES , PATTERNS , CLUMPS (marcan cuál puede ser el ori del genoma)

# Vibrio cholerae String / secuencia de bases nitrogenadas de una bacteria
Sequence = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"

# función ver la cantidad de veces que un patrón determinado aparece en una secuencia
def PatternCount(Sequence, Pattern):
    count = 0
    for i in range(len(Sequence)-len(Pattern)+1):
        if Sequence[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 
# TEST : print(PatternCount(Sequence , "ATT"))

# función para encontrar la cantidad de veces que los patrones con determinado largo aparecen
def FrequencyMap(Sequence , k): # k = el largo del patrón
    freq = {}
    n = len(Sequence)
    for i in range(n-k+1):
        Pattern = Sequence[i:i+k]
        freq[Pattern] = 0
        for i in range(n-k+1):
            if Sequence[i:i+k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq
# TEST : print(FrequencyMap(Sequence , 3)) , print(FrequencyMap(Sequence , 1)) (cada letra)

# función para encontrar los patrones con determinada cantidad de letras que aparecen más veces
def FrequentWords(Sequence , k): # k = cantidad de letras
    words = []
    freq = FrequencyMap(Sequence , k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            pattern = key
            words.append(pattern)
    return words
# TEST : print(FrequentWords(Sequence , 7))

# función devolveme todas las posiciones donde determinado patrón empieza a aparecer en una secuencia
def PatternPositions(Sequence , Pattern):
    positions = []
    for i in range(len(Sequence)-len(Pattern)+1):
        if Pattern == Sequence[i:i+len(Pattern)]:
            positions.append(i)
    return positions
# TEST : print(PatternPositions("GATATATGCATATACTT" , "ATAT"))

###################################################################################################################

# función devolveme la secuencia en reversa
def Reverse(Pattern):
  return Pattern[::-1]
# TEST : Reverse("ACTGCATCGT")

# función devolveme la secuencia complementaria
def Complement(Pattern):
    basepairs = {"A":"T", "G":"C", "T":"A", "C":"G"}
    complement = ""
    for base in Pattern:
        complement += basepairs.get(base)
    return complement
# TEST : print(Complement("ACTGCATCGT"))

# función devolveme la secuencia complementaria en reversa
def ComplementReverse(Pattern):
    basepairs = {"A":"T", "G":"C", "T":"A", "C":"G"}
    complement = ""
    for base in Pattern:
        complement += basepairs.get(base)
    return complement[::-1]
# TEST : print(ComplementReverse("ACTGCATCGT"))