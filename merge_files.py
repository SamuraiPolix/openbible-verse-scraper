import array
import io
import json

def merge_json_files(files, output_name, output_folder):
    duplicates = 0
    # Initialize empty lists for the verses and references
    all_data = []
    found = False

    # Loop through each JSON file and extract the verses and references
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for i in range(len(data)):
            data_topic = data[i]['topic']
            data_verse = data[i]['verse']
            data_ref = data[i]['reference']

            # Make sure it doesn't exist yet
            for curr_data in all_data:
                if curr_data['reference'] == data_ref:
                    found = True
                elif curr_data['verse'] == data_verse:
                    found = True
            # Add if it doesn't exist
            if not found:
                all_data.append(data[i])
            found = False
            '''
            len_before = len(all_verses)
            all_verses.add(verses_data[i])
            len_now = len(all_verses)
            if len_before != len_now:
                len_before = len(all_references)
                all_references.add(refs_data[i])
                len_now = len(all_references)
                if len_before == len_now:
                    all_verses.remove(verses_data[i])
                    duplicates += 1
            else:
                duplicates += 1
            '''

    print(f"There were {duplicates} duplicated verses.")

    # Create combined file
    with io.open(f'{output_folder}/{output_name}_data.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(all_data, ensure_ascii=False, indent=4)
        outfile.write(str_)
    return outfile.name, (len(all_data) + 1)