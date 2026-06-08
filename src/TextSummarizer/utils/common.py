import os 
from box.exceptions import BoxValueError
from ensure import ensure_annotations
import yaml
from TextSummarizer.logging import logger
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read a yaml file and return as ConfigBox 

    Args:
        path_to_yaml (Path): _description_

    Returns:
        ConfigBox: _description_
    """
    
    try:
        with open(path_to_yaml) as y_file:
            content = yaml.safe_load(y_file)
            logger.info(f"yaml file: {path_to_yaml} loaded succesfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty")
    except Exception as e:
        logger.error(f"Error occurred while loading yaml file: {path_to_yaml}")
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create a list of directories
    Arguments:
    path_to_directories: list of path of directories
    verbose: bool, if True, print information about created directories
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created a directory at: {path}")
            
            
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in kb"""
    size_in_kb = round(os.path.getsize(path)/1024, 2)
    return f"{size_in_kb} KB"
