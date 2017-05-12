import re
from Interest import research
from FieldExtraction import final

def tarea():
    li = final()   #li contains the list of faculty with their research publications
    li2 = research()   #li2 conatins the research fields and keyords 

    dict={}
    for u in li2:
        dict[u[0]]=[]

    for i in li:     #using regular expression finding the faculties working in a particular field
        for j in i:
            if j!=i[0]:
                for m in li2:
                    for n in m:
                        pat1="(.)*"+n+"(.)*"
                        
                        if re.match(pat1,j):
                            dict[m[0]].append(i[0])
                            break
                
                         

    for s,t in dict.items():  #removing redundancy
        newlist=[]
        for i in t:
            if i not in newlist:
                newlist.append(i)
        dict[s]=newlist    
    
    return dict

