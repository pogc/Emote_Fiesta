"""Module containing the tools to extract online emote data"""

import requests
import re
import sys
from bs4 import BeautifulSoup
from pprint import pprint as pp


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

    def emote_list(self):
        """Processes the obtained soup and extracts the relevant information.
           Depending on availability, the emote images will be 4x their size.

        Returns:
            A tuple with 2 lists containing the emote names and image urls
            respectively.
        """
        name = []
        img_url = []
        soup = self._html_fetch()

        for a in soup.find_all('td', attrs={'class': 'emoticon light'}):
            _a = a.prettify()
            _a = re.sub("\n", "", _a)
            name.append(re.search("title=\"(.*)\"/>", _a).group(1))
            try:
                img_url.append(re.search("2x, (.*) 4x", _a).group(1))
            except AttributeError:
                img_url.append(re.search("srcset=\"(.*) 1x", _a).group(1))

        return name, img_url

    def emote_dict(self):
        """Returns dictionary respective to emote_list"""
        keys, values = self.emote_list()
        return dict(zip(keys, values))


def test_function(url="https://www.frankerfacez.com/emoticons/?q=&sort=count-desc"):
    page_1 = Web_Page(url)
    return page_1.emote_dict()


if __name__ == '__main__':
    test_function()
