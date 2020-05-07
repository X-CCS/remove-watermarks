# -*- coding: utf-8 -*-
from PIL import Image


if __name__ == "__main__":
    for i in range(11):
        dst = Image.open("imgs/filled/{}.jpg".format(i+1))
        dst_w, dst_h = dst.size[0], dst.size[1]
        black = Image.new("RGB", [189, 79], "black")
        dst.paste(black, (130, 230))
        dst.save("imgs/ime/{}.jpg".format(i+1))
    for i in range(11):
        dst = Image.open("imgs/ime/{}.jpg".format(i+1))
        dst_w, dst_h = dst.size[0], dst.size[1]    
        src = Image.open("imgs/watermark/{}.jpg".format(i+1))
        src_w, src_h = src.size[0], src.size[1]
        dst.paste(src, (130, 230))
        dst.save("imgs/recover/{}.jpg".format(i+1))
    for i in range(11):
        dst = Image.open("imgs/recover/{}.jpg".format(i+1))
        dst_w, dst_h = dst.size[0], dst.size[1]
        src = Image.open("imgs/original/{}.jpg".format(i+1))
        src_w, src_h = src.size[0], src.size[1]
        final = dst.crop((dst_w - src_w, dst_h - src_h, dst_w, dst_h))
        final.save("imgs/final/{}.jpg".format(i+1))
