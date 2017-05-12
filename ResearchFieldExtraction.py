import GrabTexthtml

interest = []
i=1
while(i<33):
    text =GrabTexthtml.grabText("C:/Users/Ankit/Desktop/Compiler Design/WebpageInput/"+str(i)+".html")   #grabbing html text

    if "Area of Interest" in text:
        a =text.index('Area of Interest')
        a = a + len('Area of interest') + len('subject') + 2
        b = text.index('Education Details')
        text = text[a:b]                        #grabbing the research field
        temp = text.split('\n')
        interest.extend(temp)             #adding research field name to list
    i+=1

for i in range(0,interest.count('none')):   #removing 'none' 
    interest.remove('none')
newlist = []

interest = list(set(i.upper() for i in interest))

for i in interest:   #removing duplicate fields
    if i not in newlist:
        newlist.append(i)

