# -*- coding: utf-8 -*-
import glob
from PIL import Image

def get_img_size(img_name):
    im = Image.open(img_name)
    print("img width ({}), height ({})".format(im.size[0], im.size[1]))
    return im.size[0], im.size[1]

def fill_up_top_left(max_w, max_h, img_name):
    dst = Image.new("RGB", [max_w, max_h], "black")
    src = Image.open(img_name)
    w, h = src.size[0], src.size[1]
    dst.paste(src, (0, 0))
    dst.save("imgs/filled/{}".format(img_name.split("/")[len(img_name.split("/")) - 1]))

def fill_up_top_right(max_w, max_h, img_name):
    dst = Image.new("RGB", [max_w, max_h], "black")
    src = Image.open(img_name)
    w, h = src.size[0], src.size[1]
    dst.paste(src, (max_w - w, 0))
    dst.save("imgs/filled/{}".format(img_name.split("/")[len(img_name.split("/")) - 1]))

def fill_up_bottom_left(max_w, max_h, img_name):
    dst = Image.new("RGB", [max_w, max_h], "black")
    src = Image.open(img_name)
    w, h = src.size[0], src.size[1]
    dst.paste(src, (0, max_h - h))
    dst.save("imgs/filled/{}".format(img_name.split("/")[len(img_name.split("/")) - 1]))

def fill_up_bottom_right(max_w, max_h, img_name):
    dst = Image.new("RGB", [max_w, max_h], "black")
    src = Image.open(img_name)
    w, h = src.size[0], src.size[1]
    dst.paste(src, (max_w - w, max_h - h))
    dst.save("imgs/filled/{}".format(img_name.split("/")[len(img_name.split("/")) - 1]))

def fill_up_center(max_w, max_h, img_name):
    dst = Image.new("RGB", [max_w, max_h], "black")
    src = Image.open(img_name)
    w, h = src.size[0], src.size[1]
    dst.paste(src, ((max_w - w)//2, (max_h - h)//2))
    dst.save("imgs/filled/{}".format(img_name.split("/")[len(img_name.split("/")) - 1]))

if __name__ == "__main__":
    max_w, max_h = 0, 0
    for img in glob.glob("imgs/original/*.jpg"):
        w, h = get_img_size(img)
        if max_w < w:
            max_w = w
        if max_h < h:
            max_h = h
    print("max width ({}), max height ({})".format(max_w, max_h))
    for img in glob.glob("imgs/original/*.jpg"):
        fill_up_bottom_right(max_w, max_h, img)
    