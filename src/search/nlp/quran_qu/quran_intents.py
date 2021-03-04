from .surah_intents import surahs_intent

basic_intents = [
    {
        "name": "quran",
        "collection": "quran",
        "type": "collection",
        "words": ["quran", "kuran", "qoran"]
    },
    {
        "name": "surah",
        "collection": "quran",
        "type": "filter",
        "words": ["surah", "surat", "surahs"]
    },
    {
        "name": "ayah",
        "collection": "quran",
        "type": "filter",
        "words": ["ayah", "ayat", "ayahs"]
    }
]

quran_intents = basic_intents + surahs_intent
