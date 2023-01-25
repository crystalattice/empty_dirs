import os
from pathlib import Path


def find_empty_dir(path):
    for subdir in path.iterdir():
        check = os.listdir(subdir)
        if len(check) == 0:
            subdir.rmdir()


if __name__ == "__main__":
    image_path = Path("/home/codyjackson/MEGASync/piz/rips")
    find_empty_dir(image_path)
