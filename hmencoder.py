import sys

# open input file and store all the text in "inputText"
f = open(sys.argv[1], "r")
inputText = f.read()
f.close()

# dictionary to store all distinct characters with their count in the input file 
characters = {}
# count all number of characters
chrCount = 0

# count the number of appearance of characters 
for chr in inputText:
    chrCount += 1
    if characters.get(chr) is None:
        characters[chr] = 1
    else:
        characters[chr] += 1

chrsSortedCount = dict(sorted(characters.items(), key=lambda x: x[1]))
chrsSortedKey = dict(sorted(characters.items(), key=lambda x: x[0]))

# start building tree left to right, bottom up
class Node:
   def __init__(self, left, right, data=None):
      self.left = left
      self.right = right
      self.data = data

# convert element to a node if it's not
def convert(a):
    if not isinstance(a, Node):
        return Node(None, None, a)
    return a

while len(characters) != 1:
    # smallest at left, remove it from original dict
    left = min(characters, key=characters.get)
    lFreq = characters[left]
    characters.pop(left)
    # second smallest at right, remove it from original dict
    right = min(characters, key=characters.get)
    rFreq = characters[right]
    characters.pop(right)
    # put inside new node
    tmp = Node(convert(left), convert(right))
    # put new node in the dict
    characters.update({tmp: lFreq+rFreq})
    # for debugging
    # print(characters)

# now we have the root of the huffman code tree.
root = list(characters.keys())[0]

# get the codes
chrCode = {}

def getCode(currNode, chrCode, prv=""):
    # base case
    if currNode.data is not None:
        chrCode.update({currNode.data: prv})
        return
    # note that huffman code tree is a full binary tree and 
    # only leaves have values, i.e., if it is a None value node
    # it must have two children

    # go left and right subtree to find the leaves 
    getCode(currNode.left, chrCode, prv+"0")
    getCode(currNode.right, chrCode, prv+"1")
    return

getCode(root, chrCode)

# the chrCode is already, theoretically a huffman code tree (not unique)
def modify(a):
    if a == '\n':
        return '\\n'
    if a == ' ':
        return 'Space'
    return a

# write encoded message
msgf = open("encodemsg.txt", 'w')
for chr in inputText:
    msgf.write(chrCode[chr])
msgf.close()

# calculate encoded length
encodedLen = 0
for key in chrCode:
    encodedLen += (len(chrCode[key]) * chrsSortedKey[key])

# write encoded code
f = open("code.txt", 'w')
for i in chrsSortedKey:
    f.writelines(f'{modify(i)}: {chrCode[i]}\n')
f.writelines(f'Ave = {encodedLen/chrCount:.2f} bits per symbol')
f.close()