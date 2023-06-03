# Import necessary libraries
import requests
from lxml import html
import json
import io
from lxml.html.clean import unicode

def extract(tag, chars_limit):
    # Define empty lists to store extracted data
    verse_approve = list()
    ref_approve = list()

    count_skipped = 0       # Skipped verses because of chars_limit
    print(f"Scraping \"{tag}\" from OpenBible.info ...")
    # Define URL to fetch data from
    url = f"https://www.openbible.info/topics/{tag}/"
    # Fetch the HTML content from the URL
    response = requests.get(url)
    html_str = response.text

    # Convert HTML content to lxml tree object
    tree = html.fromstring(html_str)

    # Extract verse - text content of <p> elements under <div> elements with class 'verse'
    div_elements = tree.xpath("//div[@class='verse']")
    for div_element in div_elements:
        p_text = ''.join(div_element.xpath('.//p//text()')).replace('\t', '').replace('\n', '')
        verse_approve.append(p_text)

    # Extract bible reference - text content of <a> elements under <h3> elements under <div> elements with class 'verse'
    div_elements = tree.xpath("//div[@class='verse']//h3//a[@class='bibleref']//text()")
    ref_approve = div_elements

    # Remove verses that are too long (if limit is not -1)
    if chars_limit != -1:
        for i in range(len(verse_approve)-1, -1, -1):
            if len(verse_approve[i]) > chars_limit:
                count_skipped += 1
                del verse_approve[i]
                del ref_approve[i]

    # Write extracted data to a JSON file
    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str

    with io.open(f'{tag}_data.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps({'verses': verse_approve, 'references': ref_approve}, ensure_ascii=False, indent=4)
        outfile.write(to_unicode(str_))

    # Read data from JSON file and compare with original data
    with open(f'{tag}_data.json', 'r', encoding='utf-8') as data_file:
        data_loaded = json.load(data_file)

    # for debugging:
    # print(verse_approve == data_loaded['verses'])
    # print(ref_approve == data_loaded['references'])
    if chars_limit != -1:
        print(f"skipped {count_skipped} verses who exceeded {chars_limit} chars.")
    return outfile.name, len(verse_approve)


def extract_other_translation(file, translation):
    all_verses = list()
    # all_references = list()

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # verses_data = data['verses']
    refs_data = data['references']
    for i in range(len(refs_data)):
        all_verses.append(get_bible_text(refs_data[i], translation).replace("\n", " ").strip())

    # Combine the verses and references into a single dictionary
    combined_data = {'verses': list(all_verses), 'references': list(refs_data)}

    # Create combined file
    with io.open(f'merged_data_{translation}.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(combined_data, ensure_ascii=False, indent=4)
        outfile.write(str_)
    return outfile.name, len(all_verses)


def get_bible_text(verse, translation):
    base_url = 'https://bible-api.com/'
    url = base_url + verse + '?translation=' + translation

    response = requests.get(url)
    data = response.json()

    if 'text' in data:
        return data['text']
    else:
        return 'Error: Unable to fetch Bible text.'
