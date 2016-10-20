

# Create hash indicating number of each letter in a word
def word_hash(word):
    wh = {}
    for ch in word:
        if ch in wh:
            wh[ch] += 1
        else:
            wh[ch] = 1
    return wh

# Store words into nested hash. 
# The levels of the nested has correspond to each letter in the alphabet.
# The keys of each hash are the number of times that letter apperas in a word. 
def storeit(word, wordh, alphabet, nestedhash):
    subalphabet = list(alphabet)
    ch = subalphabet.pop(0)

    if ch in wordh:
        numch = wordh[ch]
    else:
        numch = 0
    
    if len(subalphabet) == 0:
        if numch not in nestedhash:
            nestedhash[numch] = [word]
        else:
            nestedhash[numch].append(word)
    else:
        if numch not in nestedhash:
            nestedhash[numch] = {}
        storeit(word, wordh, subalphabet, nestedhash[numch])

def find_anagrams(hh):
    for k,v in hh.items():
        if type(v) == dict:
            find_anagrams(v)
        else:
            word_length = len(v[0])
            if len(v) >= word_length:
                str = " ".join(v)
                print str

master = {}

# Create array of all letters
al = []
als = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for ch in als:
    al.append(ch)

# Store all dictionary words into hash organized by number of occurences of each letter in a word
f = open("/usr/share/dict/words", "r")
for line in f:
    word = line.strip()
    if len(word) >= 4:
        wh = word_hash(word)
        storeit(word,wh,al,master)
f.close

find_anagrams(master)


