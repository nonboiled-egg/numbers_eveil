import itertools 
import pyperclip as cb
import os
from os import path


file = open(path.join(path.dirname(__file__),'numbers.txt'),'r', encoding='utf-8')

target_number = int(input("No."))

rank_numbers = {
1:[],
2:[],
3:[],
4:[],
5:[],
6:[],
7:[],
8:[],
9:[],
10:[],
11:[],
12:[],
13:[]
}

for line in file:
    items=line.split("\t")
    if "禁止" in items[len(items)-1]:
        continue
        
    rank = int(items[4])
    number = items[1].split(" ")[0].split("No.")[1]
    name = items[1]
    
    
    if number == "XX":
        continue
    number = int(number)
    
    if rank == 0:
        continue
        
    pair = (number, rank, name)

    rank_numbers[rank].append(pair)
    #print("★"+str(rank)+"\t"+str(number)+"\t"+name)


whole = ""
combs = itertools.combinations(rank_numbers, 4)
counts = 0
for c in combs:
    for first in rank_numbers[c[0]]:
        if target_number < first[0]:
            continue
        
        for second in rank_numbers[c[1]]:
            if target_number < second[0]:
                continue
                
            for third in rank_numbers[c[2]]:
                if target_number < third[0]:
                    continue
            
                for fourth in rank_numbers[c[3]]:
                    if target_number < fourth[0]:
                        continue
                    
                    total = first[0]+second[0]+third[0]+fourth[0]
                    if total == target_number:
                        buffer = first[2]  + "(★"+str(first[1]) +")\t"
                        buffer += second[2] + "(★"+str(second[1])+")\t"
                        buffer += third[2]  + "(★"+str(third[1]) +")\t"
                        buffer += fourth[2] + "(★"+str(fourth[1])+")"
                        
                        whole += buffer + "\n"
                        
                        counts+=1
print(whole)
print(counts, "combinations are found")
cb.copy(whole)
