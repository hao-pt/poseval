import os
# import json
from scipy.io import loadmat
import argparse
import mat4py
import h5py
import json_tricks as json

parser = argparse.ArgumentParser(description="Convert .mat to .json file")
parser.add_argument("-ddir", "--data_dir", type=str, default="",
                    help="Data directory of .mat files")
args = parser.parse_args()

def list_dir(data_dir, allowed_extensions=['.mat']):
    """
    List files in directory

    Args:
        data_dir: data directory
        allowed_extensions: File extensions were accepted

    Returns:
        file_paths: list of files
    """
    file_paths = []
    # anot_paths = []
    # List files in data_dir
    for root, dirs, files in os.walk(data_dir):
        # print(root, dirs, files)
        for file in files:
            filename, extension = os.path.splitext(file)
            if extension in allowed_extensions:
                file_paths.append(os.path.join(root, file))
    
    # print(file_paths)
    return file_paths

def makedir(path):
    try:
        os.makedirs(path, exist_ok=True)
        print("Directory %s created successfully!" %path)
    except OSError:
        print("Directory %s failed to create!" %path)

def main(args):
    paths = list_dir(args.data_dir)

    for path in paths:
        print(path)
        x = loadmat(path)  # load mat file
        # x = h5py.File(path, 'r')
        # tables.openFile(path)
        # x = mat4py.loadmat(path)
        print(x["annolist"]["annorect"])
        json_fn = os.path.splitext(path)[0] + ".json"
        with open(json_fn, 'wt') as json_f:
            json.dump(x, json_f)
        # break

if __name__ == "__main__":
    main(args)

