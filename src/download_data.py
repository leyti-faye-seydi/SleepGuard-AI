import kagglehub
import os
import shutil

download_path = kagglehub.dataset_download("akashshingha850/mrl-eye-dataset")
source_path = os.path.join(download_path, "data")
target_path = "data"

os.makedirs(target_path, exist_ok=True)
if os.path.exists(source_path):
    shutil.copytree(source_path, target_path, dirs_exist_ok=True)
else:
    shutil.copytree(download_path, target_path, dirs_exist_ok=True)

print(f"✅ Téléchargement et extraction terminés ! Les données sont disponibles dans : {target_path}")