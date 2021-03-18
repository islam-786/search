from search.nlp.hadith_qu import HadithQU

# Queries
#
# user_query = "bukhari 123"
# user_query = "bukhari number 123"
# user_query = "bukhari #123"
# user_query = "bukhari number #123"


def test_query1():
    user_query = "bukhari 123"
    hadith_qu = HadithQU()
    result = hadith_qu.analyze(user_query)

    assert result["collection"] == "bukhari"
    assert result["filters"][0]["name"] == "hadith_number"
    assert result["filters"][0]["number"] == 123


def test_query2():
    user_query = "bukhari number 123"
    hadith_qu = HadithQU()
    result = hadith_qu.analyze(user_query)

    assert result["collection"] == "bukhari"
    assert result["filters"][0]["name"] == "hadith_number"
    assert result["filters"][0]["number"] == 123


def test_query3():
    user_query = "bukhari #123"
    hadith_qu = HadithQU()
    result = hadith_qu.analyze(user_query)

    assert result["collection"] == "bukhari"
    assert result["filters"][0]["name"] == "hadith_number"
    assert result["filters"][0]["number"] == 123


def test_query4():
    user_query = "bukhari number #123"
    hadith_qu = HadithQU()
    result = hadith_qu.analyze(user_query)

    assert result["collection"] == "bukhari"
    assert result["filters"][0]["name"] == "hadith_number"
    assert result["filters"][0]["number"] == 123
