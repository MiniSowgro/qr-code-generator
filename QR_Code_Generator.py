import pyqrcode
import os, shutil
import getpass

title = input("Give your QR Code a title!")
text = input("What would you like your QR code to say?")

file_name_svg = title + ".svg"
file_name_png = text + ".png"

url = pyqrcode.create(text)

url.svg(file_name_svg, scale=8)
url.png(file_name_png, scale=10)

os.mkdir(fr"C:\Users\alvin\Desktop\{title}")

shutil.move(file_name_svg, fr"C:Users\alvin\Desktop\{title}")
shutil.move(file_name_png, fr"C:Users\alvin\Desktop\{title}")
