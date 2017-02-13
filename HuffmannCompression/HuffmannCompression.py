from heapq import heappush, heappop, heapify
from collections import defaultdict
import string
 
def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def checkWord(word, huff):
    """Returns true if codeword exists in huff, or else it returns false"""
    for p in huff:
        if(p[1] == word):
            return 1
    return 0
    
def findCorrespondingCharacter(word, huff):
    """Returns the corresponding character for the given codeword"""
    for p in huff:
	if(p[1] == word):
            return p[0]


txt = "The latest version of Unicode contains a repertoire of more than 128,000 characters covering 135 modern and historic scripts, as well as multiple symbol sets. As it is not technically possible to list all of these characters in a single Wikipedia page, this list is limited to a subset of the most important characters for English-language readers, with links to other pages which list the supplementary characters. This page includes the 1062 characters in the Multilingual European Character Set 2 (MES-2) subset, and some additional related characters."

symb2freq = defaultdict(int)
for ch in txt:
    symb2freq[ch] += 1
# in Python 3.1+:
# symb2freq = collections.Counter(txt)
huff = encode(symb2freq)
compressed = ''
for ch in txt:
    for var in huff:
        if var[0] == ch:
            compressed = compressed + var[1]
            break
#DeCompression
word = ''
decompressed = ''
for bit in compressed:
    word = word + bit
    if(checkWord(word, huff)):
        decompressed = decompressed + findCorrespondingCharacter(word, huff)
        word = ''
print "___________________________________________________"
print "Symbol\tWeight\tHuffman Code"
quant = 0
for p in huff:
    print "%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1])
    quant = quant + int(symb2freq[p[0]])*len(p[1])
print "___________________________________________________"
print "The compressed length is: " + str(quant)
print "___________________________________________________"
print "The original length was: " + str(len(txt)*8)
print "___________________________________________________"
print "The compressed message is: "
print compressed
print "___________________________________________________"
print "The decompressed message is: "
print decompressed
print "___________________________________________________"
print "Is the decompressed message same as original message? "
print decompressed == txt
print "___________________________________________________"
print "The Compression Ratio is: "
print float(quant)/(len(txt)*8)
