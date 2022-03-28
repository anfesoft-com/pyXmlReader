# www.anfesoft.com
# check how it was made
# https://youtu.be/NsMkxn26Nms
#author: Andres F Sanchez
#anfesoft@gmail.com
import urllib.request
from xml.dom import minidom


response = urllib.request.urlopen("https://www.youtube.com/feeds/videos.xml?channel_id=UCpjkgOAY4ohqPaxAtPxq9pA")
results = response.read()
dom = minidom.parseString(results)


nodeIds = dom.getElementsByTagName("yt:videoId")
nodeTitles = dom.getElementsByTagName("media:title")

def getSingle(nodelist,inde):
    return nodelist[inde].firstChild.data
    


def showNodes(nodelist):
    i = 0
    for x in nodelist:
        print(x.firstChild.data +"|" + getSingle(nodeTitles, i))
        i = i + 1

showNodes(nodeIds)
