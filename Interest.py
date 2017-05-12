def research():
    researchList=[]   
    t=['ANDROID PROGRAMMING', 'ARTIFICIAL INTELLIGENCE','CLOUD COMPUTING', 'COMPILER DESIGN', 'COMPUTE NETWORKS AND SECURITY', 'COMPUTER GRAPHICS', 'COMPUTER NETWORKS', 'COMPUTER ORGANIZATION', 'COMPUTER SECURITY', 'DATA ANALYTICS', 'DATA COMMUNICATIONS', 'DATA MINING AND BIG DATA', 'DATA SCIENCE', 'DATA STRUCTURES AND ANALYSIS OF ALGORITHMS', 'DATABASE MANAGEMENT SYSTEMS', 'EMBEDDED SYSTEM', 'ENTREPRENEURSHIP', 'GRAPH THEORY', 'IMAGE PROCESSING', 'INDUSTRY ASSOCIATION', 'INFORMATION RETRIEVAL', 'INFORMATION SECURITY', 'INTERNET OF THINGS', 'MACHINE LEARNING', 'MATHEMATICAL MODELLING', 'MICROPRECESSORS', 'MOBILE AND WIRELESS SENSOR NETWORKS', 'NATURAL LANGUAGE PROCESSING', 'OPERATING SYSTEMS', 'SOCIAL NETWORK ANALYSIS', 'SOFTWARE DEFINED NETWORKS', 'SOFTWARE ENGINEERING', 'THEORY OF COMPUTATION', 'WEB DESGINING', 'WIRELESS NETWORK']
    #list of list containing fields with the keywords attached
    Flist=[['ANDROID PROGRAMMING','application development', 'android'], ['ARTIFICIAL INTELLIGENCE', ' Hidden Markov','IMAGE PROCESSING', 'NATURAL LANGUAGE PROCESSING', 'face recognition', 'Pattern recognition', 'Neural Networks', 'NLP', 'Image Recognition'], ['CLOUD COMPUTING', 'cloud'], ['COMPILER DESIGN', 'compiler', 'lexical', 'lexeme', 'parser'], ['COMPUTE NETWORKS AND SECURITY', 'computer networks', 'computer security', 'morse code', 'cryptography', 'cipher', 'cryptanalysis'], ['COMPUTER GRAPHICS'], ['COMPUTER NETWORKS', 'computer network', 'routing', 'routing protocol', 'Routing Algorithm', 'adhoc'], ['COMPUTER ORGANIZATION'], ['COMPUTER SECURITY', 'morse code', 'cryptography', 'cipher', 'cryptanalysis'], ['DATA ANALYTICS'], ['DATA COMMUNICATIONS'], ['DATA MINING AND BIG DATA', 'data mining', 'big data'], ['DATA SCIENCE'], ['DATA STRUCTURES AND ANALYSIS OF ALGORITHMS', 'data structure', 'algorithms'], ['DATABASE MANAGEMENT SYSTEMS', 'DBMS', 'Database'], ['EMBEDDED SYSTEM', 'embedded'], ['ENTREPRENEURSHIP', 'ENTREPRENEUR'], ['GRAPH THEORY'], ['INDUSTRY ASSOCIATION'], ['INFORMATION RETRIEVAL','Information Extraction'], ['INFORMATION SECURITY'], ['INTERNET OF THINGS', 'iot'], ['MACHINE LEARNING'], ['MATHEMATICAL MODELLING'], ['MICROPRECESSORS'], ['MOBILE AND WIRELESS SENSOR NETWORKS', 'mobile network', 'wireless network'], ['OPERATING SYSTEMS', 'windows', 'linux', 'ubuntu'], ['SOCIAL NETWORK ANALYSIS'], ['SOFTWARE DEFINED NETWORKS', 'SOFTWARE NETWORKS'], ['SOFTWARE ENGINEERING'], ['THEORY OF COMPUTATION'], ['WEB DESGINING', 'WEB DESIGN'],['DISTRIBUTED COMPUTING','HADOOP','MAPREDUCE']]
    for i in t:
        temp = [i]
        researchList.append(temp)
        
    c=0
    
    for i in Flist:   #converting ino uppercase
        for j in i:
            s=j.upper()
            i[c]=s
            c=int(c)+1
        c=0
    
    return Flist  #returning the list



