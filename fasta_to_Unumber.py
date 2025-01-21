import re

with open('', 'r') as file:
    data = file.read()

entry_numbers = re.findall(r'tr\|([A-Z0-9]+)\|', data)

for entry in entry_numbers:
    print(entry)


entry_num = '\n'.join(entry_numbers)
with open("" ,'wt') as f:
    f.write(entry_num)
