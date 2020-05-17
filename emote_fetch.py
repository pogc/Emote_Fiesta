"""Module containing the tools to extract online emote data"""
import os.path

import requests
import re
import sys
from bs4 import BeautifulSoup
from pprint import pprint as pp
import sqlite3
from sqlite3 import Error

db_filename = "database.sqlite"


class Web_Page:
    """Respective to the emoticon library pages"""

    def __init__(self, url):
        self._url = url

    def _html_fetch(self):
        """Obtains the html of the page in question and formats it adequately.

        Returns:
            A soup object containing the html code of the page
        """
        page = requests.get(self._url)
        return BeautifulSoup(page.content, features="html.parser")

    def _emote_fetch(self):
        """Processes the obtained soup and extracts the relevant information.
           Depending on availability, the emote images will be 4x their size.

        Returns:
            A tuple with 2 lists containing the emote names and image urls
            respectively.
        """
        names = []
        img_urls = []
        soup = self._html_fetch()

        for a in soup.find_all('td', attrs={'class': 'emoticon light'}):
            _a = a.prettify()
            _a = re.sub("\n", "", _a)
            names.append(re.search("title=\"(.*)\"/>", _a).group(1))
            try:
                img_urls.append(re.search("2x, (.*) 4x", _a).group(1))
            except AttributeError:
                img_urls.append(re.search("srcset=\"(.*) 1x", _a).group(1))

        return names, img_urls

    def emote_dict(self):
        """Returns dictionary respective to emote_list"""
        keys, values = self.emote_fetch()
        return dict(zip(keys, values))

    def _sql_store(self, names, urls):
        """Stores the list of emotes in SQLite database."""
        conn = None
        if not (os.path.isfile(db_filename)):
            conn = sqlite3.connect("database.sqlite")
            conn.execute('''CREATE TABLE emotes(
                        ID PRIMARY KEY NOT NULL,
                        name TEXT NOT NULL,
                        url TEXT NOT NULL)''')
            conn.close()
        try:
            conn = sqlite3.connect("database.sqlite")
            conn.execute('''INSERT INTO emotes(name, url) VALUES (?, ?)''', (names, urls))
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    def emote_db(self)



def test_function(url="https://www.frankerfacez.com/emoticons/?q=&sort=count-desc"):
    page_1 = Web_Page(url)
    return page_1.emote_dict()


def create_db(db_name="database.sqlite"):
    url_base = "https://www.frankerfacez.com/emoticons/?q=&sort=count-desc&page=")


if __name__ == '__main__':
    test_function()
