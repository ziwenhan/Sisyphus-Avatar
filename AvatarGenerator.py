#!/usr/bin/python
# -*- coding:utf-8 -*-

import hashlib
from PIL import Image, ImageColor

info = raw_input("Please input your username or email: ")

hashInfo = hashlib.md5(info)
hexHash = hashInfo.hexdigest()
hexHash = list(str(hexHash))

binaryHash = ''
for i in hexHash:
	tmp = bin(int(i, 16))[2:]
	while len(tmp) != 4:
		tmp = '0' + tmp
	binaryHash = binaryHash + tmp

pixelList = [[], [], [], [], []]
counter = 0
row = 0
for i in range(0, 101):
	if binaryHash[i] == '1':
		counter = counter + 1

	if (i+1) % 10 == 0:
		if counter >= 6:
			pixelList[row].append(1)
			pixelList[4-row].append(1)
		else:
			pixelList[row].append(0)
			pixelList[4-row].append(0)
		counter = 0

	if (i+1) % 50 == 0:
		row = row + 1

counter = 0
for i in range(101, 126):
	if binaryHash[i] == '1':
		counter = counter + 1

	if i % 5 == 0:
		if counter >= 3:
			pixelList[2].append(1)
		else:
			pixelList[2].append(0)
		counter = 0

colorIndex = int(binaryHash[126:], 2)
colorRGB = ['#51574a', '#74c493', '#e4bf80', '#e279a3', '#9abf88', '#5698c4', '#65387d', '#5cbddd']

avatar = Image.new('RGB', (500, 500), 'white')
pixels = avatar.load()

for i in range(avatar.size[0]):
	for j in range(avatar.size[1]):
		if pixelList[i / 100][j / 100] == 1:
			pixels[i, j] = ImageColor.getrgb(colorRGB[colorIndex])

avatar.show()
avatar.save("avatar.png")

