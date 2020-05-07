# -*- coding: utf-8 -*-
import glob
import os
from PIL import Image


def image_size(img):
    im = Image.open(img)
    return im.size[0], im.size[1]


def fill_up_top_left(img, max_w, max_h):
    dst = Image.new("RGB", [max_w, max_h], "black")
    src = Image.open(img)
    w, h = src.size[0], src.size[1]
    dst.paste(src, (0, 0))
    dst.save("resouces/filled/{}".format(os.path.basename(img)))


def fill_up_top_right(img, max_w, max_h):
    dst = Image.new("RGB", [max_w, max_h], "black")
    src = Image.open(img)
    w, h = src.size[0], src.size[1]
    dst.paste(src, (max_w - w, 0))
    dst.save("resouces/filled/{}".format(os.path.basename(img)))


def fill_up_bottom_left(img, max_w, max_h):
    dst = Image.new("RGB", [max_w, max_h], "black")
    src = Image.open(img)
    w, h = src.size[0], src.size[1]
    dst.paste(src, (0, max_h - h))
    dst.save("resouces/filled/{}".format(os.path.basename(img)))


def fill_up_bottom_right(img, max_w, max_h):
    dst = Image.new("RGB", [max_w, max_h], "black")
    src = Image.open(img)
    w, h = src.size[0], src.size[1]
    dst.paste(src, (max_w - w, max_h - h))
    dst.save("resouces/filled/{}".format(os.path.basename(img)))


def fill_up_center(img, max_w, max_h):
    dst = Image.new("RGB", [max_w, max_h], "black")
    src = Image.open(img)
    w, h = src.size[0], src.size[1]
    dst.paste(src, ((max_w - w)//2, (max_h - h)//2))
    dst.save("resouces/filled/{}".format(os.path.basename(img)))


if __name__ == "__main__":
    max_w, max_h = 0, 0
    for img in glob.glob("resouces/raw/*.jpg"):
        w, h = image_size(img)
        if max_w < w:
            max_w = w
        if max_h < h:
            max_h = h
    
    print("max width <{}>, max height <{}>".format(max_w, max_h))

    for img in glob.glob("resouces/raw/*.jpg"):
        fill_up_bottom_right(img, max_w, max_h)
    