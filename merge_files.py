import io
import json

def merge_json_files(files):
    dupliactes = 0
    # Initialize empty sets for the verses and references
    all_verses = set()
    all_references = set()

    # Loop through each JSON file and extract the verses and references
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        len_before = len(all_verses)
        verses_data = data['verses']
        refs_data = data['references']
        for i in range(len(verses_data)-1, -1, -1):
            if i == 0:
                print()
            all_verses.add(verses_data[i])
            len_now = len(all_verses)
            if len_before != len_now:
                len_before = len(all_references)
                all_references.add(refs_data[i])
                len_now = len(all_references)
                if len_before == len_now:
                    all_verses.remove(verses_data[i])
                    dupliactes += 1
            else:
                dupliactes += 1

    # Combine the verses and references into a single dictionary
    combined_data = {'verses': list(set(all_verses)), 'references': list(set(all_references))}

    print(f"There were {dupliactes} duplicated verses.")

    # Create combined file
    with io.open(f'merged_data.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(combined_data, ensure_ascii=False, indent=4)
        outfile.write(str_)
    return outfile.name, len(all_verses)