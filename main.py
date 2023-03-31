import os
import extractor
import merge_files

tags = ['motivation', 'love', 'joy', 'peace', 'kindness', 'goodness', 'faith']

if __name__ == "__main__":
    count_verses = 0;
    json_files = list()
    for tag in tags:
        output = extractor.extract(tag)
        json_files.append(output[0])
        count_verses += output[1]

    if len(tags) > 1:
        output = merge_files.merge_json_files(json_files)
        merged_file = output[0]
        count_verses = output[1]
        # Delete temp files
        for file in json_files:
            os.remove(file)

    print(f"\nDONE Scraping {count_verses} verses!!!")