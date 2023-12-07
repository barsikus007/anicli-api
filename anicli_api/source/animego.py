from dataclasses import dataclass
from typing import Dict

from parsel import Selector

from anicli_api.base import BaseAnime, BaseEpisode, BaseExtractor, BaseOngoing, BaseSearch, BaseSource
from anicli_api.source.parsers.animego_parser import AnimeView as AnimeViewOld
from anicli_api.source.parsers.animego_parser import DubbersView, EpisodeView
from anicli_api.source.parsers.animego_parser import OngoingView as OngoingViewOld
from anicli_api.source.parsers.animego_parser import SearchView, SourceView


# patches
class AnimeView(AnimeViewOld):
    @staticmethod
    def _parse_description(part: Selector) -> str:
        # remove whitespaces patch
        val_0 = part.css(".description ::text").getall()
        return " ".join(line.strip() for line in val_0)


class OngoingView(OngoingViewOld):
    @staticmethod
    def _parse_dub(part: Selector) -> str:
        val_0 = part.css(".text-gray-dark-6 ::text").get()
        return val_0.replace(")", "").replace("(", "")  # type: ignore


class Extractor(BaseExtractor):
    BASE_URL = "https://animego.org"

    @staticmethod
    def _extract_search(resp: str):
        data = SearchView(resp).parse().view()
        return [Search(**d) for d in data]

    @staticmethod
    def _extract_ongoing(resp: str):
        data = OngoingView(resp).parse().view()
        ongs = [Ongoing(**d) for d in data]
        # remove duplicates and accumulate by episode and dubber keys
        sorted_ongs = {}
        for ong in ongs:
            key = hash(ong.url + ong.episode)
            if sorted_ongs.get(key):
                sorted_ongs[key].dub += f", {ong.dub}"
            else:
                sorted_ongs[key] = ong
        return list(sorted_ongs.values())

    def search(self, query: str):
        resp = self.HTTP().get(f"{self.BASE_URL}/search/anime", params={"q": query})
        return self._extract_search(resp.text)

    async def a_search(self, query: str):
        resp = await self.HTTP_ASYNC().get(f"{self.BASE_URL}/search/anime", params={"q": query})
        return self._extract_search(resp.text)

    def ongoing(self):
        resp = self.HTTP().get(self.BASE_URL)
        return self._extract_ongoing(resp.text)

    async def a_ongoing(self):
        resp = await self.HTTP_ASYNC().get(self.BASE_URL)
        return self._extract_ongoing(resp.text)


@dataclass
class Search(BaseSearch):
    @staticmethod
    def _extract(resp: str):
        data = AnimeView(resp).parse().view()[0]
        return Anime(**data)

    def get_anime(self):
        resp = self._http().get(self.url)
        return self._extract(resp.text)

    async def a_get_anime(self):
        resp = await self._a_http().get(self.url)
        return self._extract(resp.text)


@dataclass
class Ongoing(BaseOngoing):
    episode: str
    dub: str

    @staticmethod
    def _extract(resp: str):
        data = AnimeView(resp).parse().view()[0]
        return Anime(**data)

    def get_anime(self):
        resp = self._http().get(self.url)
        return self._extract(resp.text)

    async def a_get_anime(self):
        resp = await self._a_http().get(self.url)
        return self._extract(resp.text)

    def __str__(self):
        return f"{self.title} {self.episode} ({self.dub})"


@dataclass
class Anime(BaseAnime):
    id: str
    raw_json: str

    @staticmethod
    def _extract(resp: str):
        episodes_data = EpisodeView(resp).parse().view()
        dubbers_data = DubbersView(resp).parse().view()
        dubbers = {d["id"]: d["name"] for d in dubbers_data}
        return [Episode(**d, dubbers=dubbers) for d in episodes_data]

    def get_episodes(self):
        resp = self._http().get(f"https://animego.org/anime/{self.id}/player?_allow=true").json()["content"]
        return self._extract(resp)

    async def a_get_episodes(self):
        resp = await self._a_http().get(f"https://animego.org/anime/{self.id}/player?_allow=true")
        return self._extract(resp.json()["content"])


@dataclass
class Episode(BaseEpisode):
    dubbers: Dict[str, str]
    id: str  # episode id

    def _extract(self, resp: str):
        data = SourceView(resp).parse().view()
        data_source = [
            {"title": f'{self.dubbers.get(d["data_provide_dubbing"], "???").strip()}', "url": d["url"]} for d in data
        ]
        return [Source(**d) for d in data_source]

    def get_sources(self):
        resp = (
            self._http()
            .get(
                "https://animego.org/anime/series",
                params={"dubbing": 2, "provider": 24, "episode": self.num, "id": self.id},
            )
            .json()["content"]
        )
        return self._extract(resp)

    async def a_get_sources(self):
        resp = (
            await self._a_http().get(
                "https://animego.org/anime/series",
                params={"dubbing": 2, "provider": 24, "episode": self.num, "id": self.id},
            )
        ).json()["content"]
        return self._extract(resp)


@dataclass
class Source(BaseSource):
    pass


if __name__ == "__main__":
    print(Extractor().search("lai")[0].get_anime().get_episodes()[0].get_sources())
    print(Extractor().ongoing()[0].get_anime().get_episodes()[0].get_sources())
