# DemoOSPath.py

import random

print(random.random())
print(random.random())
print("---randrange()---")
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print("---sample()---")
print(random.sample(range(20),10))
print(random.sample(range(20),10))

lotto = list(range(1, 46))
print(lotto)
random.shuffle(lotto)
print(lotto)

#파일과 폴더 다루기
from os.path import*

print(abspath("python.exe"))
print(basename("python.exe"))
if exists("C:\\Python310\\python.exe"):
    print("파일이 있습니다")
else:
    print("파일 없음")

print("파일크기:{0}".format(getsize("C:\\Python310\\python.exe")))

from os import*

print(f"운영체제이름:{name}")

import glob

print(f"현재폴더:{getcwd()}")
chdir("..")
chdir(r"c:\work")
lst = glob.glob("*.py")
for item in lst:
    print(item)