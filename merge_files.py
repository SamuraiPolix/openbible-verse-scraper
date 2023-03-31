import io
import json

def merge_json_files(files):
    # Initialize empty sets for the verses and references
    all_verses = set()
    all_references = set()

    # Loop through each JSON file and extract the verses and references
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            all_verses.update(data['verses'])
            all_references.update(data['references'])

    # Combine the verses and references into a single dictionary
    combined_data = {'verses': list(set(all_verses)), 'references': list(set(all_references))}

    # Create combined file
    with io.open(f'merged_data.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(combined_data, ensure_ascii=False)
        outfile.write(str_)
    return outfile.name