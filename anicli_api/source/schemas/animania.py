"""Auto generated code by selector_schema_codegen

id: animania
name: animania parser
author: vypivshiy
description:
    animania parser
source: https://animania.online/
tags:
    any

WARNING: Any manual changes made to this file will be lost when this
is run again. Do not edit this file unless you know what you are doing.
"""

from __future__ import annotations  # python 3.7, 3.8 typing comp
from typing import Any
import re

from parsel import Selector, SelectorList


class __BaseViewModel:
    def __init__(self, document: str):
        self.__raw__ = document
        self.__selector__ = Selector(document)
        self._cached_result: list[dict[str, Any]] = []
        self._aliases = {}
        self._view_keys = []

    @staticmethod
    def _pre_validate(doc):
        pass

    def _start_parse(self):
        pass

    def _part_document(self, part: Selector):
        pass

    def parse(self):
        self._pre_validate(self.__selector__)
        self._start_parse()
        return self

    def view(self) -> list[dict[str, list[str] | str]]:
        def map_fields(result):
            view_dict = {}
            for k in self._view_keys:
                if v := result.get(k):
                    k = self._aliases.get(k, k)
                    view_dict[k] = v
            return view_dict

        if len(self._cached_result) == 1:
            return [map_fields(self._cached_result[0])]
        return [map_fields(result) for result in self._cached_result]


class OngoingView(__BaseViewModel):
    """
      Prepare:
    1. GET https://animania.online/

      view() elements signature:

          title <TEXT> - title name

          thumbnail <TEXT> - thumbnail image

          url <TEXT> - url entrypoint to anime page


    """

    def __init__(self, document: str):
        super().__init__(document)
        self._aliases = {}
        self._view_keys = ["title", "thumbnail", "url"]

    @staticmethod
    def _pre_validate(part: Selector):
        pass

    def _part_document(self, part: Selector):
        val_0 = part.css(".short-tablet")
        return val_0

    @staticmethod
    def _parse_title(part: Selector) -> str:
        # script signature:
        # css "h5"
        # text
        #
        val_0 = part.css("h5")
        val_1 = val_0.xpath("./text()").get()
        return val_1

    @staticmethod
    def _parse_thumbnail(part: Selector) -> str:
        # script signature:
        # css "img"
        # attr "data-src"
        # format "https://animania.online{{}}"
        #
        val_0 = part.css("img")
        val_1 = val_0.attrib["data-src"]
        val_2 = "https://animania.online{}".format(val_1)
        return val_2

    @staticmethod
    def _parse_url(part: Selector) -> str:
        # script signature:
        # css ".st-poster"
        # attr "href"
        #
        val_0 = part.css(".st-poster")
        val_1 = val_0.attrib["href"]
        return val_1

    def _start_parse(self):
        # clear cache
        self._cached_result.clear()
        for part in self._part_document(self.__selector__):
            self._cached_result.append(
                {
                    "title": self._parse_title(part),
                    "thumbnail": self._parse_thumbnail(part),
                    "url": self._parse_url(part),
                }
            )


class SearchView(__BaseViewModel):
    """
      Prepare:
    1. GET https://animania.online/index.php?story=<QUERY>&do=search&subaction=search

      view() elements signature:

          title <TEXT> - title name

          thumbnail <TEXT> - thumbnail image

          url <TEXT> - url entrypoint to anime page


    """

    def __init__(self, document: str):
        super().__init__(document)
        self._aliases = {}
        self._view_keys = ["title", "thumbnail", "url"]

    @staticmethod
    def _pre_validate(part: Selector):
        pass

    def _part_document(self, part: Selector):
        val_0 = part.css("#short")
        return val_0

    @staticmethod
    def _parse_title(part: Selector) -> str:
        # script signature:
        # css "img"
        # attr "alt"
        #
        val_0 = part.css("img")
        val_1 = val_0.attrib["alt"]
        return val_1

    @staticmethod
    def _parse_thumbnail(part: Selector) -> str:
        # script signature:
        # css "img"
        # attr "src"
        # format "https://animania.online{{}}"
        #
        val_0 = part.css("img")
        val_1 = val_0.attrib["src"]
        val_2 = "https://animania.online{}".format(val_1)
        return val_2

    @staticmethod
    def _parse_url(part: Selector) -> str:
        # script signature:
        # css "a"
        # attr "href"
        #
        val_0 = part.css("a")
        val_1 = val_0.attrib["href"]
        return val_1

    def _start_parse(self):
        # clear cache
        self._cached_result.clear()
        for part in self._part_document(self.__selector__):
            self._cached_result.append(
                {
                    "title": self._parse_title(part),
                    "thumbnail": self._parse_thumbnail(part),
                    "url": self._parse_url(part),
                }
            )


class AnimeView(__BaseViewModel):
    """
      Prepare:
    1. GET to anime page

      view() elements signature:

          title <TEXT> - title name

          thumbnail <TEXT> - thumbnail image

          description <TEXT> - anime description


    """

    def __init__(self, document: str):
        super().__init__(document)
        self._aliases = {}
        self._view_keys = ["title", "thumbnail", "description"]

    @staticmethod
    def _pre_validate(part: Selector):
        pass

    def _part_document(self, part: Selector):
        return [part]

    @staticmethod
    def _parse_title(part: Selector) -> str:
        # script signature:
        # css "h1"
        # text
        #
        val_0 = part.css("h1")
        val_1 = val_0.xpath("./text()").get()
        return val_1

    @staticmethod
    def _parse_thumbnail(part: Selector) -> str:
        # script signature:
        # css ".fposter img"
        # attr "data-src"
        # format "https://animania.online{{}}"
        #
        val_0 = part.css(".fposter img")
        val_1 = val_0.attrib["data-src"]
        val_2 = "https://animania.online{}".format(val_1)
        return val_2

    @staticmethod
    def _parse_description(part: Selector) -> str:
        # script signature:
        # css "#fdesc"
        # text
        #
        val_0 = part.css("#fdesc")
        val_1 = val_0.xpath("./text()").get()
        return val_1

    def _start_parse(self):
        # clear cache
        self._cached_result.clear()
        for part in self._part_document(self.__selector__):
            self._cached_result.append(
                {
                    "title": self._parse_title(part),
                    "thumbnail": self._parse_thumbnail(part),
                    "description": self._parse_description(part),
                }
            )


class DubbersView(__BaseViewModel):
    """
      Prepare:
    1. GET to anime page

      view() elements signature:

          id <TEXT> - dubber id

          name <TEXT> - dubber name


    """

    def __init__(self, document: str):
        super().__init__(document)
        self._aliases = {}
        self._view_keys = ["id", "name"]

    @staticmethod
    def _pre_validate(part: Selector):
        pass

    def _part_document(self, part: Selector):
        val_0 = part.css("#ks-translations > span")
        return val_0

    @staticmethod
    def _parse_id(part: Selector) -> str:
        # script signature:
        # // get dubber id
        # // attr signature kodikSlider.season('1', this)
        # attr "onclick"
        # re "(\d+)"
        #
        val_0 = part.attrib["onclick"]
        val_1 = re.search(r"(\d+)", val_0)[1]
        return val_1

    @staticmethod
    def _parse_name(part: Selector) -> str:
        # script signature:
        # text
        #
        val_0 = part.xpath("./text()").get()
        return val_0

    def _start_parse(self):
        # clear cache
        self._cached_result.clear()
        for part in self._part_document(self.__selector__):
            self._cached_result.append(
                {
                    "id": self._parse_id(part),
                    "name": self._parse_name(part),
                }
            )


class VideoView(__BaseViewModel):
    """
      Prepare:
    1. GET to anime page

      view() elements signature:

          id <TEXT> - dubber id (for relationship with DubbersView)

          names <ARRAY> - episode names

          urls <ARRAY> - episode urls to player WARNING: `https:` prefix EXCLUDE!!!


    """

    def __init__(self, document: str):
        super().__init__(document)
        self._aliases = {}
        self._view_keys = ["id", "names", "urls"]

    @staticmethod
    def _pre_validate(part: Selector):
        pass

    def _part_document(self, part: Selector):
        val_0 = part.css("#ks-episodes > li")
        return val_0

    @staticmethod
    def _parse_id(part: Selector) -> str:
        # script signature:
        # // get dubber id
        # // attr signature <li id="season1" ...>
        # attr "id"
        # lStrip "season"
        #
        val_0 = part.attrib["id"]
        val_1 = val_0.lstrip("season")
        return val_1

    @staticmethod
    def _parse_names(part: Selector) -> list[str]:
        # script signature:
        # cssAll "span"
        # text
        #
        val_0 = part.css("span")
        val_1 = val_0.xpath("./text()").getall()
        return val_1

    @staticmethod
    def _parse_urls(part: Selector) -> list[str]:
        # script signature:
        # raw
        # reAll "'(//.*?)'"
        #
        val_0 = part.get()
        val_1 = re.findall(r"'(//.*?)'", val_0)
        return val_1

    def _start_parse(self):
        # clear cache
        self._cached_result.clear()
        for part in self._part_document(self.__selector__):
            self._cached_result.append(
                {
                    "id": self._parse_id(part),
                    "names": self._parse_names(part),
                    "urls": self._parse_urls(part),
                }
            )
