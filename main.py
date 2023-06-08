import os
import time
import extractor
import merge_files

# Limit the length of every scraped verse (verses with more chars than CHARS_LIMIT will not be scraped)
# Set to -1 to disable limit
CHARS_LIMIT = 175
TRANSLATION = "KJV"
CUSTOMER_NAME = "nigelwilliam646"

# tags = ['patience']
# tags = ['faith', 'strength', 'healing', 'trust', 'love', 'heal', 'motivation', 'hope']
tags = ['repentance', 'judgment', 'heaven', 'hell', 'justice', 'born_again', 'grace', 'mercy']
# tags = ['foster_care', 'adoption', 'children', 'family_forgiveness', 'caring', 'forgiveness', 'parenting', 'family', 'love', 'goodness', 'helping']
# tags = ['motivation', 'love', 'inspiration', 'joy', 'peace', 'kindness', 'goodness', 'faith', 'spiritual_growth', 'courage']
# tags = ['motivation', 'love', 'inspiration', 'joy', 'peace', 'kindness', 'goodness', 'faith', 'spiritual_growth', 'courage', 'patience']

if __name__ == "__main__":
    start_time_total = time.time()
    count_verses = 0;
    json_files = list()
    merged_file: str = None
    for tag in tags:
        output = extractor.extract(tag, CHARS_LIMIT)
        json_files.append(output[0])
        count_verses += output[1]

    if len(tags) > 1:
        output = merge_files.merge_json_files(json_files, CUSTOMER_NAME)
        merged_file = output[0]
        count_verses = output[1]
        # Delete temp files
        for file in json_files:
            os.remove(file)

    if (TRANSLATION != "ESV"):
        print(f"\nTranslating to {TRANSLATION}...")
        if merged_file is not None:
            extractor.extract_other_translation(merged_file, TRANSLATION)
        else:
            extractor.extract_other_translation(json_files[0], TRANSLATION)

    end_time_total = time.time()
    print(f"\nDONE Scraping {count_verses} verses in {TRANSLATION}!!!"
          f"\nTotal run time:", round(end_time_total-start_time_total, 2), "seconds = ", round((end_time_total-start_time_total) / 60, 2), " minutes!")