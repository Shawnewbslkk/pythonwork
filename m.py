import re
out = []
filein = open('w.txt', 'r', encoding='gbk')
fileout = open('out.txt', 'w', encoding='gbk')
lines = filein.readlines()
for line in lines:
    line = line.strip('\n')
    dt = re.findall("[\u4e00-\u9fa5]+", line)
    print(dt)
    dtb = str(dt)
    out.append(dtb)
    print(dtb)
print(out)
for words in out:
    fileout.write(words)