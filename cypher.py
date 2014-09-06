from cypherio import CypherIO
from s_box import S_Box
from focus import Focus
import re

def split_string(string, length):
    return [string[i:i+length] for i in range(0, len(string), length)]

def xor(seg1,seg2):
    a = list(seg1)
    b = list(seg2)
    c = ''
    for x in range(len(seg1)):
        if(a[x]==b[x]):
            c+='0'
        else:
            c+='1'

    return c

print xor('111','011')
  
class Cypher:   
    key_S_box = [4,8,1,7,3,5,6,2] 
    key_focus = [2,3,1]
    IV = '101'
    segment_size=3   
    c = CypherIO()   
    b = S_Box(key_S_box)
    f = Focus(key_focus)
    input = c.openFile('test') 
    in_text = c.getFileText()
    char_arr = [ord(w) for w in in_text]
    bin_arr = []
    message = ''
    for c in char_arr:
        bin_arr.append('0'+bin(c)[2:])
        message+='0'+bin(c)[2:]
    
    if(len(message) % segment_size != 0):
        amount = segment_size-(len(message) % segment_size)
    
        
    for x in range(amount):
        message+='0'
        
    segment_list = split_string(message,segment_size)
    first=True
    cypertext = ''
    for segment in segment_list:
        if(first):
            out_segment = xor(IV,segment)
            first=False
        else:
            out_segment = xor(out_segment,segment)        

        out_segment = b.cypherSegment(out_segment)
        out_segment = f.cypherSegment(out_segment) 
        cypertext+=out_segment   
            
            
        
    cypher_segment_list = []
    for segment in segment_list:
        cypher_segment_list.append(b.cypherSegment(segment))
        
    cypher_segment_list1 = []
    for segment in segment_list:
        cypher_segment_list1.append(f.cypherSegment(segment))
        
        
        
    print message
    print cypertext