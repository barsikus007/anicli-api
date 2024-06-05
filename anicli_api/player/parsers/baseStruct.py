# Auto generated code by ssc_gen
# WARNING: Any manual changes made to this file will be lost when this
# is run again. Do not edit this file unless you know what you are doing.

import re
from typing import List, Type, Union

from parsel import Selector, SelectorList


class BaseParser:
    def __init__(self, html: Union[str, SelectorList, Selector]):
        self.__selector__ = Selector(html) if isinstance(html, str) else html

    def parse(self):
        self._pre_validate(self.__selector__)
        return self._run_parse()

    def _run_parse(self):
        # start parse entrypoint
        pass

    def _part_document(self, el: Selector):
        # split document to elements entrypoint
        pass

    def _pre_validate(self, el: Union[Selector, SelectorList]) -> None:
        # pre validate document entrypoint
        pass

    @staticmethod
    def _css(el: Selector, query) -> SelectorList:
        return el.css(query)

    @staticmethod
    def _css_all(el, q) -> SelectorList:
        return el.css(q)

    @staticmethod
    def _xpath(el, q) -> SelectorList:
        return el.xpath(q)

    @staticmethod
    def _xpath_all(el, q) -> SelectorList:
        return el.xpath(q)

    @staticmethod
    def _attr_text(el) -> str:
        return el.css("::text").get()

    @staticmethod
    def _attr_text_all(el) -> List[str]:
        return el.css("::text").getall()

    @staticmethod
    def _attr_raw(el) -> str:
        return el.get()

    @staticmethod
    def _attr_raw_all(el) -> List[str]:
        return el.getall()

    @staticmethod
    def _attr(el, name) -> str:
        return el.attrib.get(name)

    @staticmethod
    def _attr_all(el, name) -> list[str]:
        return el.attrib.get(name)

    @staticmethod
    def _assert_css(item: Selector, query, msg):
        assert item.css(query), msg
        return item

    @staticmethod
    def _assert_xpath(item: Selector, query, msg):
        assert item.xpath(query), msg
        return item

    @staticmethod
    def _str_trim(s, sep) -> str:
        return s.strip(sep)

    @staticmethod
    def _str_ltrim(s, sep) -> str:
        return s.lstrip(sep)

    @staticmethod
    def _str_rtrim(s, sep) -> str:
        return s.rstrip(sep)

    @staticmethod
    def _str_replace(s, old, new) -> str:
        return s.replace(old, new)

    @staticmethod
    def _str_split(s, sep) -> list[str]:
        return s.split(sep)

    @staticmethod
    def _str_format(s, template) -> str:
        return template.format(s)

    @staticmethod
    def _re_match(s, pattern, group: int = 1) -> str:
        return re.search(pattern, s)[group]  # type: ignore

    @staticmethod
    def _re_match_all(s, pattern) -> list[str]:
        return re.findall(pattern, s)

    @staticmethod
    def _re_sub(s, pattern, repl) -> str:
        return re.sub(s, pattern, repl)

    # ARRAY
    @staticmethod
    def _arr_index(lst, i):
        return lst[i]

    @staticmethod
    def _arr_join(lst, sep) -> str:
        return sep.join(lst)

    @staticmethod
    def _nested_parser(el, parser_schema: Type["BaseParser"]):
        return parser_schema(el).parse()

    @staticmethod
    def _assert_equal(item, other, msg):
        assert item == other, msg
        return item

    @staticmethod
    def _assert_contains(item, other, msg):
        assert other in item, msg
        return item

    @staticmethod
    def _assert_re_match(item, pattern, msg):
        assert re.search(pattern, item), msg
        return item
