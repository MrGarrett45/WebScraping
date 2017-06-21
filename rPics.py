#! python3
# rPics.py - Downloads pictures on the frontpage of r/pics

import requests, os, bs4

url = 'https://www.reddit.com/r/pics/'             
os.makedirs('C:\\Users\\gmclaughlin\\Python\\rPics')  

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
    
pic = soup.select('img')
print(len(pic))

for i in range (25):
    if pic[i] == []:
         print('Could not find the pic.')
    else:

        picUrl = 'http:' + pic[i].get('src')
        #Download the image.
        print('Downloading image %s...' % (picUrl))
        res = requests.get(picUrl)
        res.raise_for_status()
    
    #save the image to xkcd folder
    imageFile = open(os.path.join('C:\\Users\\gmclaughlin\\Python\\rPics', os.path.basename(picUrl)), 'wb')
    for chunk in res.iter_content(100000):
            imageFile.write(chunk)
    imageFile.close()

print("DONE")
