from __future__ import division
import lxml.html
from PIL import Image
import requests
from io import BytesIO
import numpy as np


def getImageUrl(url):
    response = requests.get(url)
    tree = lxml.html.fromstring(response.content)
    img = tree.xpath('//*[@id="site-takeover"]/div[3]/div[2]/div/div[1]/img/@src')[0]
    imgUrl = 'https://basketball.realgm.com'+img
    return imgUrl
	

def getImageData(url):
    response = requests.get(url)
    inputImg = Image.open(BytesIO(response.content))
    img4 = np.array(inputImg.convert("RGBA").rotate(180).getdata()).reshape(100,75,4)
    X = 100
    Y = 75
    img = np.empty((X,Y), dtype=np.uint32)

    view = img.view(dtype=np.uint8).reshape((X, Y, 4))
    for i in range(X):
        for j in range(Y):
            view[i, j, 0] = img4[i,j,0]
            view[i, j, 1] = img4[i,j,1]
            view[i, j, 2] = img4[i,j,2]
            view[i, j, 3] = img4[i,j,3]
    return img	