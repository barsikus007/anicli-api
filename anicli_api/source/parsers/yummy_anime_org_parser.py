# autogenerated by ssc-gen DO NOT_EDIT

import re
from typing import List, TypedDict, Union, Optional
from contextlib import suppress


from parsel import Selector, SelectorList

T_OngoingPage = TypedDict(
    "T_OngoingPage",
    {
        "thumbnail": str,
        "url": str,
        "episode": int,
        "title": str,
    },
)
T_SearchPage = TypedDict(
    "T_SearchPage",
    {
        "title": str,
        "thumbnail": str,
        "url": str,
    },
)
T_AnimePage = TypedDict(
    "T_AnimePage",
    {
        "title": str,
        "alt_title": Optional[str],
        "description": str,
        "thumbnail": str,
        "player_url": Optional[str],
    },
)


class OngoingPage:
    """Get all available ongoings from the main page

        USAGE:

            GET https://yummy-anime.org/



    [
        {
            "thumbnail": "String",
            "url": "String",
            "episode": "Int",
            "title": "String"
        },
        "..."
    ]"""

    def __init__(self, document: Union[str, Selector, SelectorList]) -> None:
        self._document = Selector(document) if isinstance(document, str) else document

    def _split_doc(self, v: Union[Selector, SelectorList]) -> SelectorList:
        return v.css(".ksupdate_block a")

    def _parse_thumbnail(self, v: Union[Selector, SelectorList]) -> str:
        v0 = v.css(".xfieldimage[src]")
        v1 = v0.attrib["src"]
        return f"https://yummy-anime.org{v1}"

    def _parse_url(self, v: Union[Selector, SelectorList]) -> str:
        v0 = v.attrib["href"]
        return f"https://yummy-anime.org{v0}"

    def _parse_episode(self, v: Union[Selector, SelectorList]) -> int:
        v0 = v.css(".cell-2")
        v1 = "".join(v0.css("::text").getall())
        v2 = re.search("(\\d+)\\s", v1)[1]
        return int(v2)

    def _parse_title(self, v: Union[Selector, SelectorList]) -> str:
        v0 = v.css(".xfieldimage[alt]")
        return v0.attrib["alt"]

    def parse(self) -> List[T_OngoingPage]:
        return [
            {
                "thumbnail": self._parse_thumbnail(el),
                "url": self._parse_url(el),
                "episode": self._parse_episode(el),
                "title": self._parse_title(el),
            }
            for el in self._split_doc(self._document)
        ]


class SearchPage:
    """Get search results

        USAGE:

            POST https://yummy-anime.org
            do=search&subaction=search&story=<QUERY>

        EXAMPLE:

            POST https://yummy-anime.org/index.php
            do=search&subaction=search=from_page=0story=ван-пис


    [
        {
            "title": "String",
            "thumbnail": "String",
            "url": "String"
        },
        "..."
    ]"""

    def __init__(self, document: Union[str, Selector, SelectorList]) -> None:
        self._document = Selector(document) if isinstance(document, str) else document

    def _split_doc(self, v: Union[Selector, SelectorList]) -> SelectorList:
        return v.css("a.has-overlay")

    def _parse_title(self, v: Union[Selector, SelectorList]) -> str:
        v0 = v.css(".poster__title")
        return "".join(v0.css("::text").getall())

    def _parse_thumbnail(self, v: Union[Selector, SelectorList]) -> str:
        v0 = v.css(".xfieldimage[data-src]")
        v1 = v0.attrib["data-src"]
        return f"https://yummy-anime.org{v1}"

    def _parse_url(self, v: Union[Selector, SelectorList]) -> str:
        return v.attrib["href"]

    def parse(self) -> List[T_SearchPage]:
        return [
            {
                "title": self._parse_title(el),
                "thumbnail": self._parse_thumbnail(el),
                "url": self._parse_url(el),
            }
            for el in self._split_doc(self._document)
        ]


class AnimePage:
    """get anime page

        USAGE:

            GET https://yummy-anime.org/<...>.html

        EXAMPLE:

            GET https://yummy-anime.org/4790-vedma-i-chudovische.html



    {
        "title": "String",
        "alt_title": "String",
        "description": "String",
        "thumbnail": "String",
        "player_url": "String"
    }"""

    def __init__(self, document: Union[str, Selector, SelectorList]) -> None:
        self._document = Selector(document) if isinstance(document, str) else document

    def _parse_title(self, v: Union[Selector, SelectorList]) -> str:
        v0 = v.css(".anime__title h1")
        return "".join(v0.css("::text").getall())

    def _parse_alt_title(self, v: Union[Selector, SelectorList]) -> Optional[str]:
        v0 = v
        with suppress(Exception):
            v1 = v0.css(".anime__title .pmovie__original-title")
            return "".join(v1.css("::text").getall())
        return None

    def _parse_description(self, v: Union[Selector, SelectorList]) -> str:
        v0 = v
        with suppress(Exception):
            v1 = v0.css(".page__text p")
            v2 = v1.css("::text").getall()
            return "".join(v2)
        return ""

    def _parse_thumbnail(self, v: Union[Selector, SelectorList]) -> str:
        v0 = v.css(".pmovie__poster .xfieldimage[data-src]")
        v1 = v0.attrib["data-src"]
        return f"https://yummy-anime.org{v1}"

    def _parse_player_url(self, v: Union[Selector, SelectorList]) -> Optional[str]:
        v0 = v
        with suppress(Exception):
            v1 = v0.css(".pmovie__player iframe[src]")
            v2 = v1.attrib["src"]
            return f"https:{v2}"
        return None

    def parse(self) -> T_AnimePage:
        return {
            "title": self._parse_title(self._document),
            "alt_title": self._parse_alt_title(self._document),
            "description": self._parse_description(self._document),
            "thumbnail": self._parse_thumbnail(self._document),
            "player_url": self._parse_player_url(self._document),
        }
