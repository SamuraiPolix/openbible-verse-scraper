# Import necessary libraries
import time
import random
import requests
from lxml import html
import json
import io
from lxml.html.clean import unicode


def extract(tag, chars_limit, max_verses, output_folder):
    # Define empty lists to store extracted data
    verses_list = list()
    refs_list = list()

    count_skipped = 0  # Skipped verses because of chars_limit
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
        verses_list.append(p_text)

    # Extract bible reference - text content of <a> elements under <h3> elements under <div> elements with class 'verse'
    div_elements = tree.xpath("//div[@class='verse']//h3//a[@class='bibleref']//text()")
    refs_list = div_elements

    # Remove verses that are too long (if limit is not -1)
    if chars_limit != -1:
        for i in range(len(verses_list) - 1, -1, -1):
            if len(verses_list[i]) > chars_limit:
                count_skipped += 1
                del verses_list[i]
                del refs_list[i]
    # Remove the verses at the end to stay in the given range
    if max_verses != -1 and len(verses_list) > max_verses:
        for i in range(len(verses_list) - 1, max_verses - 1, -1):
            del verses_list[i]
            del refs_list[i]

    json_array = []
    for i in range(0, len(verses_list)):
        verse_dict = dict()
        verse_dict["topic"] = tag.capitalize()
        verse_dict["reference"] = refs_list[i]
        verse_dict["verse"] = verses_list[i]
        json_array.append(verse_dict)

    # Write extracted data to a JSON file
    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str

    with io.open(f'{output_folder}/{tag}_data.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(json_array, ensure_ascii=False, indent=4)
        outfile.write(to_unicode(str_))


    # for debugging:
    # print(verse_approve == data_loaded['verses'])
    # print(ref_approve == data_loaded['references'])
    if chars_limit != -1 and max_verses == -1:
        print(f"skipped {count_skipped} verses that exceeded {chars_limit} chars.")
    elif max_verses != -1:
        print(f"generated {len(verses_list)} verses.")
    return outfile.name, len(verses_list)


def extract_other_translation(file: str, translation, chars_limit, output_folder):
    all_data = []

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    count_exceeded = 0

    for i in range(0, len(data)):
        # time.sleep(random.randint(5, 9))
        if i != 0 and i % 14 == 0:
            time.sleep(30)
        print(i)
        translated_verse: str = get_bible_text(data[i]['reference'], translation).replace("\n", " ").strip()
        if len(translated_verse) > chars_limit:
            count_exceeded += 1
        else:
            all_data.append(data[i])
            all_data[len(all_data)-1]['verse'] = translated_verse

    file_name = file.strip(".json")
    print(count_exceeded)
    # Create combined file
    with io.open(f'{file.strip(".json")}_{translation}.json', 'w', encoding='utf-8') as outfile:
        str_ = json.dumps(all_data, ensure_ascii=False, indent=4)
        outfile.write(str_)
    return outfile.name, len(all_data)


def get_bible_text(verse, translation):
    base_url = 'https://bible-api.com/'
    url = base_url + verse + '?translation=' + translation

    response = requests.get(url)
    try:
        data = response.json()
    except:
        # DO NOT CHANGE THIS! - THE API WILL BLOCK YOUR IP FOR TOO MANY REQUESTS
        print("SLEEP 20")
        time.sleep(20)
        return get_bible_text(verse, translation)

    return data['text']
