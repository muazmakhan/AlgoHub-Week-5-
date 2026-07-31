import os
import shutil

# Folder to organize
source_folder = "scraped_data"

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav"],
    "Others": []
}

# Check if source folder exists
if not os.path.exists(source_folder):
    print("Source folder not found!")
    exit()

# Loop through all files
for file in os.listdir(source_folder):

    file_path = os.path.join(source_folder, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    extension = os.path.splitext(file)[1].lower()

    # Default category
    category = "Others"

    # Find matching category
    for folder, extensions in file_types.items():
        if extension in extensions:
            category = folder
            break

    # Create destination folder
    destination_folder = os.path.join(source_folder, category)
    os.makedirs(destination_folder, exist_ok=True)

    # Move the file
    shutil.move(file_path, os.path.join(destination_folder, file))

    print(f"{file} moved to {category}")

print("\nAll files have been organized successfully!")