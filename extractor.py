# Import necessary libraries
import requests
from lxml import html
import json
import io
from lxml.html.clean import unicode

# Define empty lists to store extracted data
verse_approve = []
ref_approve = []

# Loop twice to fetch data from the website
for i in range(2):
    print(i)
    # Define URL to fetch data from
    url = "https://www.openbible.info/topics/motivation/"
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

# Write extracted data to a JSON file
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

with io.open('verse_data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps({'verses': verse_approve, 'references': ref_approve}, ensure_ascii=False)
    outfile.write(to_unicode(str_))

# Read data from JSON file and compare with original data
with open('verse_data.json', 'r', encoding='utf-8') as data_file:
    data_loaded = json.load(data_file)

print(verse_approve == data_loaded['verses'])
print(ref_approve == data_loaded['references'])
