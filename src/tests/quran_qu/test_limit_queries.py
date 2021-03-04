from search.nlp.quran_qu import QuranQU

# Queries
#
# user_query = "surah 2 first 5 ayah"
# user_query = "surah 2 first 5 ayahs"
# user_query = "first 5 ayahs of surah 2"
# user_query = "surah 2 last 5 ayahs"
# user_query = "last 5 ayahs of surah 2"
# user_query = "surah 2 first five ayahs"
# user_query = "surah 2 last five ayahs"


def test_query1():
    user_query = "surah 2 first 5 ayah"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["score"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["limit"]["name"] == "ayah"
    assert result["limit"]["number"] == 5
    assert result["limit"]["direction"] == "start"


def test_query2():
    user_query = "surah 2 first 5 ayahs"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["score"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["limit"]["name"] == "ayah"
    assert result["limit"]["number"] == 5
    assert result["limit"]["direction"] == "start"


def test_query3():
    user_query = "first 5 ayahs of surah 2"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["score"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["limit"]["name"] == "ayah"
    assert result["limit"]["number"] == 5
    assert result["limit"]["direction"] == "start"


def test_query4():
    user_query = "surah 2 last 5 ayahs"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["score"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["limit"]["name"] == "ayah"
    assert result["limit"]["number"] == 5
    assert result["limit"]["direction"] == "end"


def test_query5():
    user_query = "last 5 ayahs of surah 2"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["score"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["limit"]["name"] == "ayah"
    assert result["limit"]["number"] == 5
    assert result["limit"]["direction"] == "end"


def test_query6():
    user_query = "surah 2 first five ayahs"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["score"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["limit"]["name"] == "ayah"
    assert result["limit"]["number"] == 5
    assert result["limit"]["direction"] == "start"


def test_query7():
    user_query = "surah 2 last five ayahs"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["score"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["limit"]["name"] == "ayah"
    assert result["limit"]["number"] == 5
    assert result["limit"]["direction"] == "end"
