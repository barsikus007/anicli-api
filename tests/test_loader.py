import pytest

from anicli_api.loader import ExtractorLoader, run_extractor_test

FAKE_WRONG_EXTRACTOR = "tests.fixtures.fake_extractor_bad"


@pytest.mark.parametrize("module", ["math", "urllib", "json", "csv", FAKE_WRONG_EXTRACTOR,
                                    "anicli_api.base",
                                    "anicli_api.extractors.__template__"])
def test_wrong_load_extractor(module: str):
    with pytest.raises(AttributeError):
        ExtractorLoader.load(module_name=module)


@pytest.mark.parametrize("module", ["extractors.123foobarbaz",
                                    "extractors.__foooooooooooo",
                                    "extractors._asd12f3gsdfg23",
                                    "why what"])
def test_not_exist_load_extractor(module: str):
    with pytest.raises(ModuleNotFoundError):
        ExtractorLoader.load(module_name=module)


@pytest.mark.parametrize("module", ["anicli_api.extractors.animego.py",
                                    "anicli_api.extractors.animego",
                                    "tests.fixtures.fake_extractor"])
def test_success_import_extractor(module):
    ExtractorLoader.load(module_name=module)


def test_extractor_tester():
    run_extractor_test("tests.fixtures.fake_extractor")
