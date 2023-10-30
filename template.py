#This script creates the directory structure and placeholder files specified in list_of_files,but it doesn't write any content to these files if they already exist or are not empty.

import os
from pathlib import Path

package_name="DimondPricePrediction"

""".gitkeep is conventional and not requirement;use any file name Git, by default,does not track empty directories because it only tracks files 
and the changes made to them.(.gitkeep) file doesn't have to contain any specific content; it's often an empty file.
Its purpose is simply to signal to Git that the directory should be tracked, even if it's empty. 
"""
list_of_files=[
    "github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py", # __init__.py files are used to define and mark directories as Python packages,allowing us to organize and import modules within our project.
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py", #All .py files are our modules
    f"src/{package_name}/components/data_transformation.py",
    f"src/{package_name}/components/model_trainer.py",
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/training_pipeline.py",
    f"src/{package_name}/pipelines/prediction_pipeline.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/utils/__init__.py",
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep",
    "requirements.txt",
    "setup.py",
    "init_setup.sh"
]

# here we are careing directories with relative files
# Path (imported from pathlib) generates cross-compatibility between different OS. Windows use backslash and UNIX linux uses forward slash in pathname.

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    """ how exist_ok works:if "directory" already exists, 
    os.makedirs() will not raise an error, and it will do nothing. 
    If "my_directory" doesn't exist, it will create the directory.
    """
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:   # The with statement is used to ensure that the file is properly closed after writing
            pass
    else:
        print("file already exists")

