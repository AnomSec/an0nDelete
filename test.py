import os

os.mkdir("test")
for i in range(100):
    os.system(f'echo test > test/test{i}.txt')