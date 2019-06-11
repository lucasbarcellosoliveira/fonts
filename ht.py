"""Author Web Scraper"""

import requests

def postprocessing(nameList):
    nameList=list(map(lambda a:a.replace("and",""),nameList))
    for i in range(len(nameList)):
        if "  " in nameList[i]:
            nameList+=[nameList[i].split("  ")[1]]
            nameList[i]=nameList[i].split("  ")[0]
    nameList=list(map(lambda a:a.replace("‘",""),nameList)) #removes a problematic character
    nameList=list(map(lambda a:a.replace("’",""),nameList)) #removes a problematic character
    nameList=list(map(lambda a:a.strip(),nameList))
    return nameList

#VIS2018's Accepted Papers
response=requests.get("http://ieeevis.org/year/2018/info/papers")
response.encoding=response.apparent_encoding
authors2018=[]
for i in response.text.split("Authors: "):
    authors2018+=i.split("</p>")[0].split(", ")
authors2018=authors2018[1:]
authors2018=postprocessing(authors2018)

#VIS2017's Accepted Papers
response=requests.get("http://ieeevis.org/year/2017/info/papers")
response.encoding=response.apparent_encoding
authors2017=[]
for i in response.text.split("Authors: "):
    authors2017+=i.split("</p>")[0].split(", ")
authors2017=authors2017[1:]
authors2017=postprocessing(authors2017)

#VIS2016's Accepted Papers
response=requests.get("http://ieeevis.org/year/2016/info/overview-amp-topics/papers")
response.encoding=response.apparent_encoding
authors2016=[]
for i in response.text.split("Authors: "):
    authors2016+=i.split("</p>")[0].split(", ")
authors2016=authors2016[1:]
authors2016=postprocessing(authors2016)

totalAuthors=authors2018+authors2017+authors2016
totalAuthors=list(dict.fromkeys(totalAuthors)) #remove duplicates
print(totalAuthors)
print("Total # of authors: "+str(len(totalAuthors)))
