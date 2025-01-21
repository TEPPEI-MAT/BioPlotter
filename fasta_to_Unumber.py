import re

with open('/Users/matsuda_teppei/idmapping_2024_11_24', 'r') as file:
    data = file.read()

entry_numbers = re.findall(r'tr\|([A-Z0-9]+)\|', data)

for entry in entry_numbers:
    print(entry)


entry_num = '\n'.join(entry_numbers)
with open("/Users/matsuda_teppei/Documents/UAD/001_compre_gene/uniplot_num_3.txt" ,'wt') as f:
    f.write(entry_num)