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

- set these:

```python
FILE_NAME = "filename"
CHARS_LIMIT = -1                    # limit length of verses generated, -1 disables the limit.
MAX_VERSES_PER_TOPIC = -1           # limit number of verses generated per topic, -1 disables the limit.
TRANSLATION = "ESV"                 # ESV is the default (openbible.info).
KEEP_INDIVIDUAL_FILES = "False"     # Do you want to have separate files for each topic? (you will always have a merged file as well)
```
- RUN!

<h2>Result:</h2>

```yaml
[
    {
        "topic": "Motivation",
        "reference": "Colossians 3:23",
        "verse": "Whatever you do, work heartily, as for the Lord and not for men,"
    },
    {
        "topic": "Love",
        "reference": "1 Corinthians 16:14",
        "verse": "Let all that you do be done in love."
    },
    {
        "topic": "Joy",
        "reference": "Romans 15:13",
        "verse": "May the God of hope fill you with all joy and peace in believing, so that by the power of the Holy Spirit you may abound in hope."
    },
    {
        "topic": "Kindness",
        "reference": "Ephesians 4:32",
        "verse": "Be kind to one another, tenderhearted, forgiving one another, as God in Christ forgave you."
    },
    {
        "topic": "Faith",
        "reference": "Matthew 21:22",
        "verse": "And whatever you ask in prayer, you will receive, if you have faith.”"
    },
    {
        "topic": "Goodness",
        "reference": "Psalm 23:6",
        "verse": "Surely goodness and mercy shall follow me all the days of my life, and I shall dwell in the house of the Lord forever."
    },
    {
        "topic": "Patience",
        "reference": "Romans 12:12",
        "verse": "Rejoice in hope, be patient in tribulation, be constant in prayer."
    },
    {
        "topic": "Peace",
        "reference": "John 16:33",
        "verse": "I have said these things to you, that in me you may have peace. In the world you will have tribulation. But take heart; I have overcome the world.”"
    }
]
```

<h3>Enjoy!</h3>


<h2>Practiced Technologies:</h2>

* Web scraping
* API
* JSON
