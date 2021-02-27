from search.quran_qu import QuranQU

# Queries
#
# user_query = "surah 2 first 5 ayah"


def test_query1():
    user_query = "surah 2 first 5 ayah"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["query"]["filters"][0]["name"] == "surah"
    assert result["query"]["filters"][0]["number"] == 2
    assert result["query"]["limit"]["name"] == "ayah"
    assert result["query"]["limit"]["number"] == 5
    assert result["query"]["limit"]["direction"] == "start"
