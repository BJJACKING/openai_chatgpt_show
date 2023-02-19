# -*-coding:utf-8-*-


from config import *
from urllib import request
from PIL import Image


def get_openai_image(query):
    response = openai.Image.create(
        prompt=query,    #图片描述
        n=1,             #每次生成图片的数量
        size="256x256"   #图片大小,可选有 256x256, 512x512, 1024x1024
    )
    image_url = response['data'][0]['url']
    print("image_url: {}".format(image_url))
    return image_url


def image_show(image_url):
    img = Image.open(request.urlopen(image_url))
    img.show()


if __name__ == "__main__":
    query = "法式豪宅"
    image_url = get_openai_image(query)
    image_show(image_url)
