# allo = "ab"
# words = ["ad","bd","aaab","baa","badab"]
#
# a = []
# for i in words:
#     a.append(all([x in set(allo) for x in i]))
# print(a)
#
# for m in range(3,5):
#     print(m)

import tesserocr
from PIL import Image

image = r'G:\自测\sdining-master\12.jpg'
open_img = Image.open(image)
result = tesserocr.im