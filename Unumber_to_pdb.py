import os
import requests

def download_alphafold_structure(uniprot_id, output_dir="/Users/matsuda_teppei/Documents/UAD/001_compre_gene/structures4"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    url = f"https://alphafold.ebi.ac.uk/files/AF-{uniprot_id}-F1-model_v4.pdb"
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(f"{output_dir}/{uniprot_id}.pdb", "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {uniprot_id}")
    else:
        print(f"Structure not found for: {uniprot_id}")


file_path = "/Users/matsuda_teppei/Documents/UAD/001_compre_gene/uniplot_num_3.txt"

with open(file_path, "r") as file:
    data_list = [line.strip() for line in file]

#print(data_list)

uniprot_ids = data_list
for uniprot_id in uniprot_ids:
    download_alphafold_structure(uniprot_id)