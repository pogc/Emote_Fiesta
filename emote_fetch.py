"""Module containing the tools to extract online emote data"""
import os.path

import requests
import re
import sys
from bs4 import BeautifulSoup
from pprint import pprint as pp
import sqlite3
from sqlite3 import Error


class Web_Page:
    """Respective to the emoticon library pages"""

    def __init__(self, url, db_filename="database.sqlite"):
        self._url = url
        self._db_filename = db_filename

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
        """Returns dictionary respective to _emote_fetch"""
        keys, values = self.emote_fetch()
        return dict(zip(keys, values))

    def _sql_store(self, names, urls):
        """Stores the list of emotes in SQLite database.

            Args:
                names: List of strings with names corresponding to the images
                urls: List of strings with urls corresponding to the images
        """
        conn = None
        if not (os.path.isfile(self._db_filename)):
            conn = sqlite3.connect("database.sqlite")
            conn.execute('''CREATE TABLE emotes(
                        name TEXT NOT NULL,
                        url TEXT NOT NULL)''')
            conn.close()
        try:
            conn = sqlite3.connect("database.sqlite")
        except Error as e:
            print(e)
        for n, u in zip(names, urls):
            try:
                conn.execute('''INSERT INTO emotes (name, url) VALUES (?, ?)''', (n, u))
            except sqlite3.IntegrityError as e:
                print(e)
        if conn:
            conn.close()

    def emote_db(self):
        """Performs the above methods to add the webpage to the database"""
        names, urls = self._emote_fetch()
        self._sql_store(names, urls)


def test_function(url="https://www.frankerfacez.com/emoticons/?q=&sort=count-desc"):
    page_1 = Web_Page(url)
    return page_1.emote_dict()


def create_db(db_name="database.sqlite"):
    url_base = "https://www.frankerfacez.com/emoticons/?q=&sort=count-desc&page="
    for x in range(1,10):
        print(x)
        Web_Page(url_base + str(x), db_name).emote_db()


def db_string(orig, x="url", y="name", db_name="database.sqlite"):
    """Searches a database for an item and returns it in a usable form.

        Args:
            orig = item corresponding to the one to find in the database.
            x = name of the type of item to retrieve.
            y = name of the type of item orig is.
            db_name = Name of the database.

        Raises:
            KeyError - If item could not be obtained.
    """
    try:
        conn = sqlite3.connect("database.sqlite")
    except Error as e:
        print(e)
    a = conn.execute("SELECT url FROM emotes WHERE name=?", (orig,)).fetchall()
    if conn:
        conn.close()
    print(a)
    if not a:
        raise KeyError
    return a[0][0]


if __name__ == '__main__':
    create_db()

