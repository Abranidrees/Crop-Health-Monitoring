import os 

"""
    This function creates four directories at the specified paths if they do not already exist.
    
    Parameters:
        folder_path (str): The path to the parent folder where the directories are created.
        download_path (str): The path to the "download" directory.
        processed_path (str): The path to the "processed" directory.
        indices_path (str): The path to the "indices" directory.
    
    Returns:
        None
    """
    
def folder(folder_path: str):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

def download(download_path: str):
    if not os.path.exists(download_path):
        os.mkdir(download_path)

def processed(processed_path: str):
    if not os.path.exists(processed_path):
        os.mkdir(processed_path)

def indices(indices_path: str):
    if not os.path.exists(indices_path):
        os.mkdir(indices_path)
    print("Directories successfully created")