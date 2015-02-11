import urllib2,re
url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
value="56789"
 
for i in range(400):
    text=urllib2.urlopen(url+value).read()
    value="".join(re.findall(r"nothing is (\d+)",str(text)))
    try :
        int(value)
        print("The Next Nothing is :",value)
    except :
        print("Last:",text)
        break
