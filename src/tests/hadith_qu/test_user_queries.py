from search.nlp.hadith_qu import HadithQU

# Queries
#
# user_query = "sahih bukhari hadith 1"
# user_query = "sahih bukhari hadees 1"
# user_query = "sahih bukhari hadees number 1"
# user_query = "sahih bukhari"
# user_query = "sahih bukhari hadith"
# user_query = "hadith number 1"


def test_query1():
    hadith_qu = HadithQU()
    result = hadith_qu.analyze("sahih bukhari hadith 1")

    assert result['collection'] == "bukhari"
    assert result["confidence"] >= 100
    assert result['filters'][0]["name"] == "hadith_number"
    assert result['filters'][0]["number"] == 1


def test_query2():
    hadith_qu = HadithQU()
    result = hadith_qu.analyze("sahih bukhari hadees 1")

    assert result['collection'] == "bukhari"
    assert result["confidence"] >= 100
    assert result['filters'][0]["name"] == "hadith_number"
    assert result['filters'][0]["number"] == 1


def test_query3():
    hadith_qu = HadithQU()
    result = hadith_qu.analyze("sahih bukhari hadees number 1")

    assert result['collection'] == "bukhari"
    assert result["confidence"] >= 100
    assert result['filters'][0]["name"] == "hadith_number"
    assert result['filters'][0]["number"] == 1


def test_query4():
    hadith_qu = HadithQU()
    result = hadith_qu.analyze("sahih bukhari")

    assert result['collection'] == "bukhari"
    assert result["confidence"] >= 100
    assert len(result['filters']) == 0


def test_query5():
    hadith_qu = HadithQU()
    result = hadith_qu.analyze("bukhari")

    assert result['collection'] == "bukhari"
    assert result["confidence"] >= 100
    assert len(result['filters']) == 0


def test_query6():
    hadith_qu = HadithQU()
    result = hadith_qu.analyze("hadith number 1")

    assert result['collection'] == "bukhari"
    assert result["confidence"] >= 100
    assert result['filters'][0]["name"] == "hadith_number"
    assert result['filters'][0]["number"] == 1
