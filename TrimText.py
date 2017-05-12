import GrabTexthtml
from FacultyNameExtraction import fac
    
i = 1
l = fac()
while(i<33):
    text =GrabTexthtml.grabText("F:\\STUDY MATERIALS\\6TH SEM\\Compiler Design\\Compiler Design Project\\WebpageInput\\"+str(i)+".html")   #grabbing html text
    name = l[i-1]
    a=0
    b=0

    if "Research Publication" in text:
        a =text.index('Research Publication')

    if "Workshop/FDP" in text:
        b = text.index('Workshop/FDP')

    text = text[a+len('Research Publication')+1:b]   #grabbing text under research publication field
    
    with open("input1.txt", "a",encoding='utf-8') as fd:
        fd.write('~Research Publication\n'+name+text+"\n\n")   #writing in into input file
    fd.close()
    i+=1
    
