import os
import shutil

doc_path = '/Users/faisalahmed/downloads/folderwithfolders'

for root, dirs, files in os.walk(doc_path, topdown=False):
    for file in files:
        try:
            shutil.move(os.path.join(root, file), doc_path)
        except OSError:
            pass