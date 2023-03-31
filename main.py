import os

import extractor
import merge_files

tags = ['motivation', 'love']

if __name__ == "__main__":
    json_files = list()
    for tag in tags:
        json_files.append(extractor.extract(tag))
    if len(tags) > 1:
        merged_file = merge_files.merge_json_files(json_files)
        # Delete temp files
    for file in json_files:
        os.remove(file)
    print("DONE!")