from search.quran_qu import QuranQU

# Queries
#
# user_query = "quran"
# user_query = "something"
# user_query = "kuran"
# user_query = "kuran surt 2 ayt 1"


def test_query1():
    user_query = "quran"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"


def test_query2():
    user_query = "something"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] is None


def test_query3():
    user_query = "kuran"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"


def test_query4():
    user_query = "kuran surt 2 ayt 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["query"]["filters"][0]["name"] == "surah"
    assert result["query"]["filters"][0]["number"] == 2
    assert result["query"]["filters"][1]["name"] == "ayah"
    assert result["query"]["filters"][1]["number"] == 1
