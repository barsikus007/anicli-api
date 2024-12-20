# Auto generated code by ssc_gen
# WARNING: Any manual changes made to this file will be lost when this
# is run again. Do not edit this file unless you know what you are doing.

from typing import Dict, List, TypedDict

from .baseStruct import BaseParser


T_OngoingPage = TypedDict("T_OngoingPage", {"url": str, "title": str, "thumbnail": str, "episode": str, "dub": str})

T_SearchPage = TypedDict("T_SearchPage", {"title": str, "thumbnail": str, "url": str})

T_AnimePage = TypedDict("T_AnimePage", {"title": str, "description": str, "thumbnail": str, "id": str, "raw_json": str})

T_EpisodeDubbersView = Dict[str, str]

T_EpisodesView = TypedDict("T_EpisodesView", {"num": str, "title": str, "id": str})

T_EpisodePage = TypedDict("T_EpisodePage", {"dubbers": T_EpisodeDubbersView, "episodes": List["T_EpisodesView"]})

T_SourceVideoView = TypedDict(
    "T_SourceVideoView", {"title": str, "url": str, "data_provider": str, "data_provide_dubbing": str}
)

T_SourceDubbersView = Dict[str, str]

T_SourcePage = TypedDict("T_SourcePage", {"dubbers": T_SourceDubbersView, "videos": List["T_SourceVideoView"]})


class OngoingPage(BaseParser):
    """
        Get all available ongoings from the main page

        GET https://animego.me


    [
      {
        "url": "String",
        "title": "String",
        "thumbnail": "String",
        "episode": "String",
        "dub": "String"
      },
      "..."
    ]
    """

    def parse(self) -> List["T_OngoingPage"]:
        return self._run_parse()

    def _run_parse(self) -> List["T_OngoingPage"]:
        return [
            T_OngoingPage(
                **{
                    "url": self._parse_url(el),
                    "title": self._parse_title(el),
                    "thumbnail": self._parse_thumbnail(el),
                    "episode": self._parse_episode(el),
                    "dub": self._parse_dub(el),
                }
            )
            for el in self._part_document(self.__selector__)
        ]

    def _part_document(self, el):
        var = self._css_all(el, ".border-bottom-0.cursor-pointer")
        return var

    def _parse_url(self, el):
        var = self._attr(el, "onclick")
        var_1 = self._str_ltrim(var, "location.href=")
        var_2 = self._str_trim(var_1, "'")
        var_3 = self._str_format(var_2, "https://animego.me{}")
        return var_3

    def _parse_title(self, el):
        var = self._css(el, ".last-update-title")
        var_1 = self._attr_text(var)
        return var_1

    def _parse_thumbnail(self, el):
        var = self._css(el, ".lazy")
        var_1 = self._attr(var, "style")
        var_2 = self._str_ltrim(var_1, "background-image: url(")
        var_3 = self._str_rtrim(var_2, ");")
        return var_3

    def _parse_episode(self, el):
        var = self._css(el, ".text-truncate")
        var_1 = self._attr_text(var)
        var_2 = self._re_match(var_1, "(\\d+)\\s", 1)
        return var_2

    def _parse_dub(self, el):
        var = self._css(el, ".text-gray-dark-6")
        var_1 = self._attr_text(var)
        var_2 = self._str_replace(var_1, ")", "")
        var_3 = self._str_replace(var_2, "(", "")
        return var_3


class SearchPage(BaseParser):
    """
        Get all search results by query

        USAGE:

            GET https://animego.me/search/anime
            q={QUERY}

        EXAMPLE:

            GET https://animego.me/search/anime?q=LAIN


    [
      {
        "title": "String",
        "thumbnail": "String",
        "url": "String"
      },
      "..."
    ]
    """

    def parse(self) -> List["T_SearchPage"]:
        return self._run_parse()

    def _run_parse(self) -> List["T_SearchPage"]:
        return [
            T_SearchPage(
                **{
                    "title": self._parse_title(el),
                    "thumbnail": self._parse_thumbnail(el),
                    "url": self._parse_url(el),
                }
            )
            for el in self._part_document(self.__selector__)
        ]

    def _part_document(self, el):
        var = self._css_all(el, ".row > .col-ul-2")
        return var

    def _parse_title(self, el):
        var = self._css(el, ".text-truncate a")
        var_1 = self._attr(var, "title")
        return var_1

    def _parse_thumbnail(self, el):
        var = self._css(el, ".lazy")
        var_1 = self._attr(var, "data-original")
        return var_1

    def _parse_url(self, el):
        var = self._css(el, ".text-truncate a")
        var_1 = self._attr(var, "href")
        return var_1


class AnimePage(BaseParser):
    """
        Anime page information. anime path contains in SearchView.url or Ongoing.url

        - id needed for next API requests
        - raw_json used for extract extra metadata (unescape required)

        USAGE:

            GET https://animego.me/anime/<ANIME_PATH>

        EXAMPLE:

            GET https://animego.me/anime/eksperimenty-leyn-1114


    {
      "title": "String",
      "description": "String",
      "thumbnail": "String",
      "id": "String",
      "raw_json": "String"
    }
    """

    def parse(self) -> T_AnimePage:
        return self._run_parse()

    def _run_parse(self) -> T_AnimePage:
        return T_AnimePage(
            **{
                "title": self._parse_title(self.__selector__),
                "description": self._parse_description(self.__selector__),
                "thumbnail": self._parse_thumbnail(self.__selector__),
                "id": self._parse_id(self.__selector__),
                "raw_json": self._parse_raw_json(self.__selector__),
            }
        )

    def _parse_title(self, el):
        var = self._css(el, ".anime-title h1")
        var_1 = self._attr_text(var)
        return var_1

    def _parse_description(self, el):
        try:
            var = self._css_all(el, ".description")
            var_1 = self._attr_text_all(var)
            var_2 = self._arr_join(var_1, "")
            var_3 = self._re_sub(var_2, "^\\s+|\\s+$", "")
            return var_3
        except Exception:
            return ""

    def _parse_thumbnail(self, el):
        var = self._css(el, "#content img")
        var_1 = self._attr(var, "src")
        return var_1

    def _parse_id(self, el):
        var = self._css(el, ".br-2 .my-list-anime")
        var_1 = self._attr(var, "id")
        var_2 = self._str_ltrim(var_1, "my-list-")
        return var_2

    def _parse_raw_json(self, el):
        var = self._css(el, "script[type='application/ld+json']")
        var_1 = self._attr_text(var)
        return var_1


class EpisodeDubbersView(BaseParser):
    """


    {
      "K": "V",
      "...": "..."
    }
    """

    def parse(self) -> T_EpisodeDubbersView:
        return self._run_parse()

    def _run_parse(self) -> T_EpisodeDubbersView:
        return {self._parse_key(el): self._parse_value(el) for el in self._part_document(self.__selector__)}

    def _parse_key(self, el):
        var = self._attr(el, "data-dubbing")
        return var

    def _parse_value(self, el):
        var = self._css(el, "span")
        var_1 = self._attr_text(var)
        var_2 = self._re_sub(var_1, "^\\s+|\\s+$", "")
        return var_2

    def _part_document(self, el):
        var = self._css_all(el, "#video-dubbing .mb-1")
        return var


class EpisodesView(BaseParser):
    """


    [
      {
        "num": "String",
        "title": "String",
        "id": "String"
      },
      "..."
    ]
    """

    def parse(self) -> List["T_EpisodesView"]:
        return self._run_parse()

    def _run_parse(self) -> List["T_EpisodesView"]:
        return [
            T_EpisodesView(
                **{
                    "num": self._parse_num(el),
                    "title": self._parse_title(el),
                    "id": self._parse_id(el),
                }
            )
            for el in self._part_document(self.__selector__)
        ]

    def _part_document(self, el):
        var = self._css_all(el, "#video-carousel .mb-0")
        return var

    def _parse_num(self, el):
        var = self._attr(el, "data-episode")
        return var

    def _parse_title(self, el):
        var = self._attr(el, "data-episode-title")
        return var

    def _parse_id(self, el):
        var = self._attr(el, "data-id")
        return var


class EpisodePage(BaseParser):
    """
        Representation episodes

        Prepare:
          1. get id from Anime object
          2. GET 'https://animego.me/anime/{Anime.id}/player?_allow=true'
          3. extract html from json by ['content'] key
          4. OPTIONAL: unescape HTML

        EXAMPLE:

            GET https://animego.me/anime/anime/1114//player?_allow=true


    {
      "dubbers": {
        "<dubber_id>": "<dubber_name>",
        "<id>": "..."
      },
      "episodes": [
        {
          "num": "String",
          "title": "String",
          "id": "String"
        },
        "..."
      ]
    }
    """

    def parse(self) -> T_EpisodePage:
        return self._run_parse()

    def _run_parse(self) -> T_EpisodePage:
        return T_EpisodePage(
            **{
                "dubbers": self._parse_dubbers(self.__selector__),
                "episodes": self._parse_episodes(self.__selector__),
            }
        )

    def _parse_dubbers(self, el):
        var = self._nested_parser(el, EpisodeDubbersView)
        return var

    def _parse_episodes(self, el):
        var = self._nested_parser(el, EpisodesView)
        return var


class SourceVideoView(BaseParser):
    """


    [
      {
        "title": "String",
        "url": "String",
        "data_provider": "String",
        "data_provide_dubbing": "String"
      },
      "..."
    ]
    """

    def parse(self) -> List["T_SourceVideoView"]:
        return self._run_parse()

    def _run_parse(self) -> List["T_SourceVideoView"]:
        return [
            T_SourceVideoView(
                **{
                    "title": self._parse_title(el),
                    "url": self._parse_url(el),
                    "data_provider": self._parse_data_provider(el),
                    "data_provide_dubbing": self._parse_data_provide_dubbing(el),
                }
            )
            for el in self._part_document(self.__selector__)
        ]

    def _part_document(self, el):
        var = self._css_all(el, "#video-players > span")
        return var

    def _parse_title(self, el):
        var = self._attr_text(el)
        return var

    def _parse_url(self, el):
        var = self._attr(el, "data-player")
        var_1 = self._str_format(var, "https:{}")
        return var_1

    def _parse_data_provider(self, el):
        var = self._attr(el, "data-provider")
        return var

    def _parse_data_provide_dubbing(self, el):
        var = self._attr(el, "data-provide-dubbing")
        return var


class SourceDubbersView(BaseParser):
    """


    {
      "K": "V",
      "...": "..."
    }
    """

    def parse(self) -> T_SourceDubbersView:
        return self._run_parse()

    def _run_parse(self) -> T_SourceDubbersView:
        return {self._parse_key(el): self._parse_value(el) for el in self._part_document(self.__selector__)}

    def _parse_key(self, el):
        var = self._attr(el, "data-dubbing")
        return var

    def _parse_value(self, el):
        var = self._attr_text(el)
        var_1 = self._re_sub(var, "^\\s+", "")
        var_2 = self._re_sub(var_1, "\\s+$", "")
        return var_2

    def _part_document(self, el):
        var = self._css_all(el, "#video-dubbing > span")
        return var


class SourcePage(BaseParser):
    """
        representation player urls

        Prepare:
          1. get num and id from Episode

          2.

          GET https://animego.me/anime/series
          dubbing=2&provider=24&episode={Episode.num}id={Episode.id}

          3. extract html from json by ["content"] key

          4. OPTIONAL: unescape document

        EXAMPLE:

            GET https://animego.me/anime/series?dubbing=2&provider=24&episode=2&id=15837


    {
      "dubbers": {
        "<dubber_id>": "<dubber_name>",
        "...": "..."
      },
      "videos": [
        {
          "title": "String",
          "url": "String",
          "data_provider": "String",
          "data_provide_dubbing": "String"
        },
        "..."
      ]
    }
    """

    def parse(self) -> T_SourcePage:
        return self._run_parse()

    def _run_parse(self) -> T_SourcePage:
        return T_SourcePage(
            **{
                "dubbers": self._parse_dubbers(self.__selector__),
                "videos": self._parse_videos(self.__selector__),
            }
        )

    def _parse_dubbers(self, el):
        var = self._nested_parser(el, SourceDubbersView)
        return var

    def _parse_videos(self, el):
        var = self._nested_parser(el, SourceVideoView)
        return var
