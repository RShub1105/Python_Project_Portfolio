import os 
import shutil
source_folder = "Downloads1"
file_types = {
    "image":['.jpg','.jpeg','.png','.gif'],
    "Documents":['.pdf','.docx','.pptx'],
    "Texts":['.txt','.md'],
    "Music":['.mp3','.wav'],
    "Videos":['.mp4','.mov'],
    "Compressed":['.zip','.rar'],
    "Python":['.py']

}

def Create_folder(folder_name):
    folder_path = os.path.join(source_folder,folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
def move_file(file,folder_name):
    source_path = os.path.join(source_folder,file)
    target_path = os.path.join(source_folder,folder_name,file)
    shutil.move(source_path,target_path)

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder,file)
    if os.path.isfile(file_path):
        _,ext = os.path.splitext(file)
        moved = False
        
        for folder_name,extensions in file_types.items():
            if ext.lower()in extensions:
                Create_folder(folder_name)
                move_file(file,folder_name)
                moved = True
                break
        if not moved:
            Create_folder("others")
            move_file(file,"others")
print("file organizing completed!")
