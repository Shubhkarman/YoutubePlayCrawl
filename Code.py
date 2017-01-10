import os

def getLength(filepath):
  return os.popen("ffmpeg -i '" + filepath + "' 2>&1 | grep Duration | cut -d ' ' -f 4 | sed s/,//").read()

#getLength(os.path.abspath('/media/shubi/New Volume1/ALL LECTURES !!!/Python/Reverse Shell/rs.mp4'))



from bs4 import BeautifulSoup

def parser(filepath):
    soup = BeautifulSoup(open(filepath),'lxml')
    allTime = soup.findAll("div", {"class": "timestamp"})
    aT = []
    for i in allTime:
        x = i.string
        if x[1] == ':':     # to add leading 0 to make 0m:ss
            x = '0'+x
        aT.append(x)#print(i.string)
    allNames = soup.findAll("a", {"class": "pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link "})
    aN = []
    for i in allNames:
        str = i.string
        aN.append(str[str.find('P'):str[1:].find('\n')+1])#print(i.name)
    return zip(aT, aN)

import urllib.request
def downPage(url):
    urllib.request.urlretrieve(url,'file.html')

def rename(dir, url):
    vT = []
    vN = []
    for i in os.listdir(dir):
        x = getLength(os.path.join(dir,i))
        #print(x)
        vT.append(x[3:-1])  # to remove hour time(hh:mm:ss) and following '\n'
        vN.append(i)

    vids = zip(vT,vN)
    downPage(url)    # your link

    vidsNew = parser('file.html')
    vids = sorted(vids)
    #print(vids)
    vidsNew = sorted(vidsNew)
    for i in range(0,len(vids)):
        print(vids[i])
        print(vidsNew[i])
        os.rename(os.path.join(dir,vids[i][1]),os.path.join(dir,vidsNew[i][1]+'.mp4'))



rename('/media/shubi/New Volume1/ALL LECTURES !!!/Python/Reverse Shell','https://www.youtube.com/playlist?list=PL6gx4Cwl9DGCbpkBEMiCaiu_3OL-_Bz_8')