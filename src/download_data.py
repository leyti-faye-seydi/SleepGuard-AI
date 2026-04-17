import kagglehub
import os
import shutil

download_path = kagglehub.dataset_download("akashshingha850/mrl-eye-dataset")

target_path = "data/raw"

os.makedirs(target_path, exist_ok=True)

shutil.copytree(download_path, target_path, dirs_exist_ok=True)

print(f"✅ Téléchargement et extraction terminés ! Les données sont disponibles dans : {target_path}")