import pytest
from search.quran_qu import QuranQU


def test_user_query1():
    user_query = "Quran surah 2 ayah 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_user_query2():
    user_query = "surah 2 ayah 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_user_query3():
    user_query = "surah 2 ayat 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_user_query4():
    user_query = "surat 2 ayat 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_user_query5():
    user_query = "quran ayat 1 surah 2"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    print(result)

    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "ayah"
    assert result["filters"][0]["number"] == 1
    assert result["filters"][1]["name"] == "surah"
    assert result["filters"][1]["number"] == 2


def test_user_query6():
    user_query = "quran surah#2 ayat#1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_user_query7():
    user_query = "quran surah #2 ayat #1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_user_query8():
    user_query = "quran surah# 2 ayat# 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_user_query9():
    user_query = "surah #2 ayat#1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_user_query10():
    user_query = "quran 2:1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_user_query11():
    user_query = "quran 2:1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_user_query12():
    user_query = "quran 2:1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_user_query13():
    user_query = "quran 2:1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_user_query14():
    user_query = "2:1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_user_query15():
    user_query = "2-1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "surah"
    assert result["filters"][0]["number"] == 2
    assert result["filters"][1]["name"] == "ayah"
    assert result["filters"][1]["number"] == 1


def test_user_query16():
    user_query = "1 ayah of 2 surah from quran"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "ayah"
    assert result["filters"][0]["number"] == 1
    assert result["filters"][1]["name"] == "surah"
    assert result["filters"][1]["number"] == 2


def test_user_query17():
    user_query = "first ayah of second surah from quran"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result["collection"] == "quran"
    assert result["filters"][0]["name"] == "ayah"
    assert result["filters"][0]["number"] == 1
    assert result["filters"][1]["name"] == "surah"
    assert result["filters"][1]["number"] == 2
