import os
import re


def remove(data, i, line, regex, left, right):
    m = re.search(regex, line)
    if m:
        digits = m.group(0)
        start, end = m.start(0), m.end(0)
        data[i] = line[:start+left] + '*' * (right-left+1) + line[start+right+1:]
        return True
    return False

infile = os.path.join(os.getcwd(), 'data.txt')
# infile = 'data.txt'
outfile = os.getcwd() + 'data_proc.txt'
with open(infile) as fr:
    data = fr.readlines()

regex_id = '(\d{18}|\d{17}X)'
regex_phone = '1\d{10}'
for i, line in enumerate(data):
    status = remove(data, i, line, regex_id, 5, 14)
    if not status:
        status = remove(data, i, line, regex_phone, 3, 6)

with open(outfile, 'w') as fw:
    for line in data:
        fw.write(line)