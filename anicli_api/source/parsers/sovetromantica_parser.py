# Auto generated code by ssc_gen
# WARNING: Any manual changes made to this file will be lost when this
# is run again. Do not edit this file unless you know what you are doing.

from __future__ import annotations  # python 3.7, 3.8 comp
import re
from typing import Any, Union

from parsel import Selector, SelectorList

_T_DICT_ITEM = dict[str, Union[str, list[str]]]
_T_LIST_ITEMS = list[dict[str, Union[str, list[str]]]]


class _BaseStructParser:
    def __init__(self, document: str):
        self.__raw__ = document
        self.__selector__ = Selector(document)
        self._cached_result: Union[_T_DICT_ITEM, _T_LIST_ITEMS] = {}

    def _pre_validate(self, document: Selector) -> None:
        # pre validate entrypoint, contain assert expressions
        pass

    def parse(self):
        """run parser"""
        self._pre_validate(self.__selector__)
        self._start_parse()
        return self

    def view(self) -> Union[_T_DICT_ITEM, _T_LIST_ITEMS]:
        """get parsed values"""
        return self._cached_result

    def _start_parse(self):
        """parse logic entrypoint"""
        pass


class OngoingView(_BaseStructParser):
    """
        GET https://sovetromantica.com/anime

        OngoingView view() item signature:

    {
        "url": "String",
        "title": "String",
        "thumbnail": "String",
        "alt_title": "String"
    }
    """

    def __init__(self, document: str):
        super().__init__(document)
        self._cached_result: _T_LIST_ITEMS = []

    def _part_document(self) -> SelectorList:
        doc = self.__selector__
        var_0 = doc
        var_1 = var_0.css(".anime--block__desu")
        return var_1

    def _start_parse(self):
        self._cached_result.clear()
        for part in self._part_document():
            self._cached_result.append(
                {
                    "url": self._parse_url(part),
                    "title": self._parse_title(part),
                    "thumbnail": self._parse_thumbnail(part),
                    "alt_title": self._parse_alt_title(part),
                }
            )

    def view(self) -> _T_LIST_ITEMS:
        return self._cached_result

    def _parse_url(self, doc: Selector):
        """ongoing page"""

        var_0 = doc
        var_1 = var_0.css(".anime--block__desu a")
        var_2 = var_1.attrib["href"]
        return var_2

    def _parse_title(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css(".anime--block__name > span + span")
        var_2 = var_1.css("::text").get()
        return var_2

    def _parse_thumbnail(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css(".anime--poster--loading > img")
        var_2 = var_1.attrib["src"]
        return var_2

    def _parse_alt_title(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css(".anime--block__name > span")
        var_2 = var_1.css("::text").get()
        return var_2


class SearchView(_BaseStructParser):
    """Get all search results by query

        GET https://sovetromantica.com/anime
        query=<QUERY>

        EXAMPLE:
            GET https://sovetromantica.com/anime
            query=LAIN

        SearchView view() item signature:

    {
        "title": "String",
        "thumbnail": "String",
        "alt_title": "String",
        "url": "String"
    }
    """

    def __init__(self, document: str):
        super().__init__(document)
        self._cached_result: _T_LIST_ITEMS = []

    def _pre_validate(self, doc: Selector) -> None:
        var_0 = doc
        var_1 = var_0.css("title")
        var_2 = var_1.css("::text").get()
        assert re.search(r"Аниме / SovetRomantica", var_2)
        return

    def _part_document(self) -> SelectorList:
        doc = self.__selector__
        var_0 = doc
        var_1 = var_0.css(".anime--block__desu")
        return var_1

    def _start_parse(self):
        self._cached_result.clear()
        for part in self._part_document():
            self._cached_result.append(
                {
                    "title": self._parse_title(part),
                    "thumbnail": self._parse_thumbnail(part),
                    "alt_title": self._parse_alt_title(part),
                    "url": self._parse_url(part),
                }
            )

    def view(self) -> _T_LIST_ITEMS:
        return self._cached_result

    def _parse_title(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css(".anime--block__name > span + span")
        var_2 = var_1.css("::text").get()
        return var_2

    def _parse_thumbnail(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css(".anime--poster--loading > img")
        var_2 = var_1.attrib["src"]
        return var_2

    def _parse_alt_title(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css(".anime--block__name > span")
        var_2 = var_1.css("::text").get()
        return var_2

    def _parse_url(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css(".anime--block__desu a")
        var_2 = var_1.attrib["href"]
        return var_2


class AnimeView(_BaseStructParser):
    """Anime page information

        GET https://sovetromantica.com/anime/<ANIME PATH>

        EXAMPLE:
            GET https://sovetromantica.com/anime/1459-sousou-no-frieren

        AnimeView view() item signature:

    {
        "title": "String",
        "description": "String",
        "thumbnail": "String",
        "video": "String"
    }
    """

    def __init__(self, document: str):
        super().__init__(document)
        self._cached_result: _T_DICT_ITEM = {}

    def _start_parse(self):
        self._cached_result.clear()
        self._cached_result["title"] = self._parse_title(self.__selector__)
        self._cached_result["description"] = self._parse_description(self.__selector__)
        self._cached_result["thumbnail"] = self._parse_thumbnail(self.__selector__)
        self._cached_result["video"] = self._parse_video(self.__selector__)

    def view(self) -> _T_DICT_ITEM:
        return self._cached_result

    def _parse_title(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css(".anime-name .block--container")
        var_2 = var_1.css("::text").get()
        return var_2

    def _parse_description(self, doc: Selector):
        var_0 = doc
        try:
            var_2 = var_0.css("#js-description_open-full")
            var_3 = var_2.css("::text").get()
            return var_3
        except Exception as e:
            return ""

    def _parse_thumbnail(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css("#poster")
        var_2 = var_1.attrib["src"]
        var_3 = "https://sovetromantica.com{}".format(var_2)
        return var_3

    def _parse_video(self, doc: Selector):
        """WARNING!

        in main page give first episode video contains in <meta> tag and maybe does not exist

        EG:

          https://sovetromantica.com/anime/1398-tsundere-akuyaku-reijou-liselotte-to-jikkyou-no-endou-kun-to-kaisetsu-no-kobayashi-san

        """

        var_0 = doc
        try:
            var_2 = var_0.get()
            var_3 = re.search(r"\"file\":\"([^>]+\.m3u8)\"\s*}", var_2)[1]
            return var_3
        except Exception as e:
            return None


class EpisodeView(_BaseStructParser):
    """WARNING!

        target page maybe does not contain video!

        GET https://sovetromantica.com/anime/<ANIME PATH>

        EXAMPLE:
            GET https://sovetromantica.com/anime/1459-sousou-no-frieren


        EpisodeView view() item signature:

    {
        "url": "String",
        "thumbnail": "String",
        "title": "String"
    }
    """

    def __init__(self, document: str):
        super().__init__(document)
        self._cached_result: _T_LIST_ITEMS = []

    def _pre_validate(self, doc: Selector) -> None:
        var_0 = doc
        var_1 = var_0.css("title")
        var_2 = var_1.css("::text").get()
        assert re.search(r"/ SovetRomantica", var_2)
        return

    def _part_document(self) -> SelectorList:
        doc = self.__selector__
        var_0 = doc
        var_1 = var_0.css(".episodes-slick_item")
        return var_1

    def _start_parse(self):
        self._cached_result.clear()
        for part in self._part_document():
            self._cached_result.append(
                {
                    "url": self._parse_url(part),
                    "thumbnail": self._parse_thumbnail(part),
                    "title": self._parse_title(part),
                }
            )

    def view(self) -> _T_LIST_ITEMS:
        return self._cached_result

    def _parse_url(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css("a")
        var_2 = var_1.attrib["href"]
        var_3 = "https://sovetromantica.com{}".format(var_2)
        return var_3

    def _parse_thumbnail(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css("img")
        var_2 = var_1.attrib["src"]
        return var_2

    def _parse_title(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css("img")
        var_2 = var_1.attrib["alt"]
        return var_2
