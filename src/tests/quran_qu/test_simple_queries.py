import pytest
from search.nlp.quran_qu import QuranQU

# Queries
#
# user_query = "Quran surah 2 ayah 1"
# user_query = "surah 2 ayah 1"
# user_query = "surah 2 ayat 1"
# user_query = "surat 2 ayat 1"
# user_query = "quran ayat 1 surah 2"
# user_query = "quran surah#2 ayat#1"
# user_query = "quran surah #2 ayat #1"
# user_query = "quran surah# 2 ayat# 1"
# user_query = "surah #2 ayat#1"
# user_query = "quran 2:1"
# user_query = "2:1"
# user_query = "2-1"
# user_query = "1 ayah of 2 surah from quran"
# user_query = "first ayah of second surah from quran"
# user_query = "surah number 2 ayat number 1"
# user_query = "surah num 2 ayah 1"
# user_query = "surah no 2 ayah 1"
# user_query = "surah no. 2 ayah no.1"
# user_query = "quran surahs"


def test_query1():
    user_query = "Quran surah 2 ayah 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["confidence"] >= 100
    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query2():
    user_query = "surah 2 ayah 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["confidence"] >= 100
    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query3():
    user_query = "surah 2 ayat 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query4():
    user_query = "surat 2 ayat 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query5():
    user_query = "quran ayat 1 surah 2"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    print(result)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "ayah"
    assert result["filters"][0]["number"] == 1
    assert result["filters"][1]["name"] == "surah"
    assert result["filters"][1]["number"] == 2


def test_query6():
    user_query = "quran surah#2 ayat#1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query7():
    user_query = "quran surah #2 ayat #1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query8():
    user_query = "quran surah# 2 ayat# 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query9():
    user_query = "surah #2 ayat#1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query10():
    user_query = "quran 2:1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query11():
    user_query = "quran 2:1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query12():
    user_query = "quran 2:1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query13():
    user_query = "quran 2:1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query14():
    user_query = "2:1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query15():
    user_query = "2-1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query16():
    user_query = "1 ayah of 2 surah from quran"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "ayah"
    assert result["filters"][0]["number"] == 1
    assert result["filters"][1]["name"] == "surah"
    assert result["filters"][1]["number"] == 2


def test_query17():
    user_query = "first ayah of second surah from quran"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "ayah"
    assert result["filters"][0]["number"] == 1
    assert result["filters"][1]["name"] == "surah"
    assert result["filters"][1]["number"] == 2


def test_query18():
    user_query = "surah number 2 ayat number 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query19():
    user_query = "surah num 2 ayah 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query20():
    user_query = "surah no 2 ayah 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query21():
    user_query = "surah no. 2 ayah no.1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_query22():
    user_query = "quran surahs"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["confidence"] >= 100
