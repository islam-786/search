basic_intents = [
    {
        "name": "quran",
        "collection": "quran",
        "type": "collection",
        "words": ["quran"]
    },
    {
        "name": "surah",
        "collection": "quran",
        "type": "filter",
        "words": ["surah", "surat"]
    },
    {
        "name": "ayah",
        "collection": "quran",
        "type": "filter",
        "words": ["ayah", "ayat"]
    }
]

surahs_intent = [
    {
        "name": "surah",
        "collection": "quran",
        "type": "pre_define_filter",
        "number": 2,
        "words": ["al-baqarah", "baqarah", "baqara"]
    }
]


quran_intents = basic_intents + surahs_intent
