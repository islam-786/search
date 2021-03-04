from search.nlp.quran_qu import QuranQU

# Queries
#
# user_query = "surah 2 ayah from 1 to 5"
# user_query = "surah 2 from 1 to 5"
# user_query = "surah 2 start from 1 end 5"
# user_query = "surah 2 start 1 end 5"
# user_query = "surah 2 start from 1 to end 5"


def test_query1():
    quran_qu = QuranQU()
    result = quran_qu.analyze("surah 2 ayah from 1 to 5")

    assert result["collection"] == "quran"
    assert result["score"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["range"]["from"] == 1
    assert result["range"]["to"] == 5


def test_query2():
    quran_qu = QuranQU()
    result = quran_qu.analyze("surah 2 from 1 to 5")

    assert result["collection"] == "quran"
    assert result["score"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["range"]["from"] == 1
    assert result["range"]["to"] == 5


def test_query3():
    quran_qu = QuranQU()
    result = quran_qu.analyze("surah 2 start from 1 end 5")

    assert result["collection"] == "quran"
    assert result["score"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["range"]["from"] == 1
    assert result["range"]["to"] == 5


def test_query4():
    quran_qu = QuranQU()
    result = quran_qu.analyze("surah 2 start 1 end 5")

    assert result["collection"] == "quran"
    assert result["score"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["range"]["from"] == 1
    assert result["range"]["to"] == 5


def test_query5():
    quran_qu = QuranQU()
    result = quran_qu.analyze("surah 2 start from 1 to end 5")

    assert result["collection"] == "quran"
    assert result["score"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["range"]["from"] == 1
    assert result["range"]["to"] == 5
