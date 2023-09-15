import os
import time
import extractor
import merge_files

FILE_NAME = "filename"
tags = ['motivation', 'love']

# Limit the length of every scraped verse (verses with more chars than CHARS_LIMIT will not be scraped)
# Set to -1 to disable limit
CHARS_LIMIT = 175

# Limit the number of verses scraped per topic
# Set to -1 to disable limit
MAX_VERSES_PER_TOPIC = 2

# ESV is the default scraped from openbible.info
# If you want another translation, please head over to bible-api.com and set this to be the "Identifier" from the website
TRANSLATION = "KJV"

# If you have more than 1 tag, setting this to:
# True:  will generate a file for each tag and a merged file with all the tags
# False: will only generate a merged file with all the tags
keep_individual_files = "False"


if __name__ == "__main__":
    project_dir = os.getcwd().replace("\\", "/")
    output_folder = f'{project_dir}/scraped'
    if not os.path.exists(f'{project_dir}/scraped'):
        os.makedirs(f'{project_dir}/scraped')

    start_time_total = time.time()
    count_verses = 0;
    json_files = list()
    merged_file: str = None
    for tag in tags:
        output = extractor.extract(tag, CHARS_LIMIT, MAX_VERSES_PER_TOPIC, output_folder)
        json_files.append(output[0])
        count_verses += output[1]

    if len(tags) > 1:
        output = merge_files.merge_json_files(json_files, FILE_NAME, output_folder)
        merged_file = output[0]
        count_verses = output[1]
        # Delete temp files
        if keep_individual_files == 'False':
            for file in json_files:
                os.remove(file)

    # If the translation is not ESV - Go through scraped verses and use bible-api.com to translate
    if (TRANSLATION != "ESV"):
        print(f"\nTranslating to {TRANSLATION}... (This may take a few minutes, depending on the amount of verses you scraped)")
        if keep_individual_files == 'True':
            new_count_verses = 0;
            new_json_files = list()
            for file in json_files:
                output = extractor.extract_other_translation(file, TRANSLATION, CHARS_LIMIT, MAX_VERSES_PER_TOPIC, output_folder)
                new_json_files.append(output[0])
                new_count_verses += output[1]
                # Delete temp ESV file
                os.remove(file)
            if len(tags) > 1:
                output = merge_files.merge_json_files(new_json_files, FILE_NAME, output_folder)
                merged_file = output[0]
                count_verses = output[1]
        else:
            if merged_file is not None:
                extractor.extract_other_translation(merged_file, TRANSLATION, CHARS_LIMIT, output_folder)
                # Delete merged ESV file
                os.remove(merged_file)
            else:
                extractor.extract_other_translation(json_files[0], TRANSLATION, CHARS_LIMIT, output_folder)
                # Delete temp ESV file
                os.remove(json_files[0])

    end_time_total = time.time()
    print(f"\nDONE Scraping {count_verses} verses in {TRANSLATION}!!!"
          f"\nTotal run time:", round(end_time_total-start_time_total, 2), "seconds")
    if round(end_time_total - start_time_total, 2) > 60:
        print(" = ", round((end_time_total-start_time_total) / 60, 2), "minutes!")