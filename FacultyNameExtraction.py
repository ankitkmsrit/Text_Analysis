from GrabTexthtml import grabText


def fac():
    
    facultyList =[]
    i=1
    while(i<33):
        text = grabText("F:\\STUDY MATERIALS\\6TH SEM\\Compiler Design\\Compiler Design Project\\WebpageInput\\"+str(i)+".html")  #returns text using the Grabtext file

        a=0
        if "Faculty Details" in text:        
            a = text.index("Faculty Details")
            a = a + 2*len("Faculty Details")+2
            text = text[a:]

        s=""
        for letter in text:
            if(letter=="\n"):
                break
            s+=letter              #grabbing faculty name


        facultyList.append(s)    #adding faculty name to list
        i+=1
    return facultyList



