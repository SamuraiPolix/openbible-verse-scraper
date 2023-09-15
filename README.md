![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
<a href = "https://www.paypal.com/donate/?hosted_button_id=5JK8CUWFUU9B6">![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)</a>

# OPENBIBLE.INFO Website Verse Scraper

This script scrapes the verses and references from an openbible.info/topics/{} page into a JSON file, if another bible translation is needed, we use bible-api.com to translate the verses.
  
<h3>Bible versions available:</h3>

## Translation List

| Language        | Name                                             | bible-api.com Identifier    |
|-----------------|--------------------------------------------------|-----------------------------|
| English  	      | English Standart Translation	                   | (default on openbible.info) |
| Cherokee	      | Cherokee New Testament	                         | cherokee                    |
| English	        | Bible in Basic English	                         | bbe                         |
| English	        | King James Version	                             | kjv                         |
| English	        | World English Bible	                             | web                         |
| English (UK)    |	Open English Bible, Commonwealth Edition         | oeb-cw                      |
| English (UK)    |	World English Bible, British Edition             | webbe                       |
| English (US)    |	Open English Bible, US Edition                   | oeb-us                      |
| Latin	          | Clementine Latin Vulgate                         | clementine                  |
| Portuguese      |	João Ferreira de Almeida                         | almeida                     |
| Romanian	      | Protestant Romanian Corrected Cornilescu Version | rccv                        |

*This table was taken from bible-api.com - please head to their website for the updated list.


<h2>How to run:</h2>
<h3>Using an IDE:</h3>

- Open main.py

- set your tags (choose biblical topics to get verses of)

```python
tags = ['love', 'joy', 'kindness']
```

- RUN!

<h3>Using Terminal (CMD):</h3>


<h2>Result:</h2>
The output file is "data.json"

<h3>Enjoy!</h3>


<h2>Practiced Technologies:</h2>

* Web scraping
* API
