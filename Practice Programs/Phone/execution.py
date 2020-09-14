#import os

#print(os.getcwd())

import Phones
import Phones.Sounds
#import Phones.G3 #Only import G3 file from Phones package
#from Phones import G3 #Same as above statment

Phones.Pots()
Phones.G3_phone()
Phones.Isdn()
Phones.Sounds.Big_Bang()
#G3.G3_phone() #File functions called this way using the from import line


#with open('Text.txt') as f:
    #for line in f:
        #print(line)

#f = open('Text.txt', 'r+')
#read_line = f.readline()
#print(read_line)
#value = ('Sonic speed', 42069)
#s = str(value)
#f = open('Text.txt', 'w')
#f.seek(5)
#print(f.write(s))
#print(f.read())
#f.close()

import json
print(json.dumps([1, 'simple', 'list']))
f = open('Tism.txt', 'r+')
x = (2, 'simple', 'list')
deserialized = json.dumps(x)
q = json.loads(deserialized)
print(q)
#data = json.dump(x, f)
d_data = json.load(f)
print(d_data)
f.close()
