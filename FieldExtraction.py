from FacultyNameExtraction import fac
import re

def final():
    finalList =[]

    t = fac()
    for i in t:
        temp = [i]
        finalList.append(temp)

    l=[]
    i=0
    with open("input.txt","r") as fd:
        a = fd.readline()
        while(i<32):
            while(not(re.match('~Research Publication',a))):
                if '"' in a:
                    s = a.index('"')
                    e = a.rfind('"')
                    temp = a[s:e+1]
                    finalList[i].append(temp)
                a = fd.readline()
            a = fd.readline()
            i+=1
               
    fd.close()
    c=0
    for i in finalList:
        for j in i:
            s=j.upper()
            i[c]=s
            c=int(c)+1
        c=0
    return finalList

  
