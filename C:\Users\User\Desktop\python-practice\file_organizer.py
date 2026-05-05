import os
import shutil

# Folder to organize (change this path)
source_folder = "C:/Users/User/Downloads"

# File type categories
file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Others": []
}

# Create folders if not exist
for folder in file_types:
    folder_path = os.path.join(source_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in file_types.items():
            for ext in extensions:
                if file.lower().endswith(ext):
                    shutil.move(file_path, os.path.join(source_folder, folder, file))
                    moved = True
                    break
            if moved:
                break

        if not moved:
            shutil.move(file_path, os.path.join(source_folder, "Others", file))

print("✅ Files organized successfully!")
