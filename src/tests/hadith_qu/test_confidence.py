from search.quran_qu import QuranQU
from search.hadith_qu import HadithQU


def test_quran_wining_queries():
    queries = [
        "Quran surah 2 ayah 1",
        "surah 2 ayah 1",
        "surah 2 ayat 1",
        "surat 2 ayat 1",
        "quran ayat 1 surah 2",
        "quran surah#2 ayat#1",
        "quran surah #2 ayat #1",
        "quran surah# 2 ayat# 1",
        "surah #2 ayat#1",
        "quran 2:1",
        "2:1",
        "2-1",
        "1 ayah of 2 surah from quran",
        "first ayah of second surah from quran",
        "surah number 2 ayat number 1",
        "surah num 2 ayah 1",
        "surah no 2 ayah 1",
        "surah no. 2 ayah no.1",
        "quran surahs",
        "quran",
        "kuran",
        "kuran surt 2 ayt 1",
        "surah 2 first 5 ayah",
        "surah 2 first 5 ayahs",
        "first 5 ayahs of surah 2",
        "surah 2 last 5 ayahs",
        "last 5 ayahs of surah 2",
        "surah 2 first five ayahs",
        "surah 2 last five ayahs",
        "surah 2 ayah from 1 to 5",
        "surah 2 from 1 to 5",
        "surah 2 start from 1 end 5",
        "surah 2 start 1 end 5",
        "surah 2 start from 1 to end 5",
        "surah al-baqarah ayat 1",
        "surah baqra ayat 1",
        "surah-al-baqarah ayah 1",
        "al-baqarah ayah 1",
        "surat-ul-baqarah ayah 1",
        "surah al-baqarah ayah from 1 to 5"
    ]

    for query in queries:
        quran_qu = QuranQU()
        q = quran_qu.analyze(query)

        hadith_qu = HadithQU()
        h = hadith_qu.analyze(query)

        assert q["confidence"] > h["confidence"]


def test_hadith_wining_queries():
    queries = [
        "sahih bukhari hadith 1",
        "sahih bukhari hadees 1",
        "sahih bukhari hadees number 1",
        "sahih bukhari",
        "sahih bukhari hadith",
        "hadith number 1"
    ]

    for query in queries:
        quran_qu = QuranQU()
        q = quran_qu.analyze(query)

        hadith_qu = HadithQU()
        h = hadith_qu.analyze(query)

        assert h["confidence"] > q["confidence"]
