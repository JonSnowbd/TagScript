from .. import Parse_Verb, VerbContext
import pytest

@pytest.fixture
async def test_verb_parsing():
    parsed = await Parse_Verb("{hello:world}")
    assert type(parsed) is VerbContext
    assert parsed.declaration == "hello"
    assert parsed.payload == "world"

    parsed2 = await Parse_Verb("{greetings(green):planet}")
    assert type(parsed2) is VerbContext
    assert parsed2.parameter == "green"
    assert parsed2.declaration == "greetings"
    assert parsed2.payload == "planet"