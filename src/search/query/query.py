import requests
from search.nlp import NLP

hadith_books = ["bukhari", "muslim", "tirmidhi",
                "abu_dawud", "nasai", "ibne_maja"]


class Query:
    def __init__(self, text):
        self.text = text

    def response(self):
        url = None
        response_type = None
        r = {}
        nlp = NLP.analyze(self.text)

        r["query"] = self.text
        r["nlp"] = nlp.copy()
        del r["nlp"]["_debug"]

        if nlp["collection"] == "quran":
            url, response_type = self._quran_api_url(nlp)
        elif nlp["collection"] in hadith_books:
            url, response_type = self._hadith_api_url(nlp)

        r["nlp"]["url"] = url
        r["type"] = response_type
        #r["data"] = self._api_response(url)

        return r

    def _api_response(self, url):
        r = requests.get(url)
        return r.json()

    def _quran_api_url(self, nlp):
        base_url = "http://localhost:5001/v1"
        url = None
        response_type = None

        if "filters" in nlp:
            response_type = "single_ayah"
            f = nlp["filters"]

            # if filters len is greater than 1 than it means
            # it filter surah and ayah both otherwise only surah
            if len(f) > 1:
                # Generate ayah id with surah and number e.g 2-1
                ayah_id = str(f[0]["number"]) + "-" + str(f[1]["number"])
                url = base_url + "/ayah/" + ayah_id
            else:
                # Surah number
                surah_number = str(f[0]["number"])
                url = base_url + "/surah/" + surah_number

        # Check if there is any limit
        if "limit" in nlp:
            response_type = "multi_ayah"
            limit = nlp["limit"]
            url += '?maxResult=' + \
                str(limit["number"]) + "&direction=" + limit["direction"]

        # Check if there is any range
        if "range" in nlp:
            response_type = "multi_ayah"
            range = nlp["range"]
            url += '?offset=' + str(range["from"]) + \
                '&maxResult=' + str(range["to"])

        # Get Quran surahs only when there is no filter, range and limit
        if all(k not in nlp for k in ("filters", "range", "limit")):
            response_type = "surah_list"
            url = base_url + "/surah/list"

        return url, response_type

    def _hadith_api_url(self, nlp):
        base_url = "http://localhost:5002/v1"
        url = None
        response_type = None

        if "filters" in nlp:
            response_type = "single_hadith"
            f = nlp["filters"][0]
            url = base_url + "/" + nlp["collection"] + "/" + str(f["number"])

        # Get Quran surahs only when there is no filter, range and limit
        if all(k not in nlp for k in ("filters", "range", "limit")):
            response_type = "hadith_books"
            url = base_url + "/books/" + nlp["collection"]

        return url, response_type
