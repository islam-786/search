from fireo.models import Model
from fireo.fields import TextField, NumberField, MapField, IDField


class QuranAyah(Model):
    id = IDField()
    uci = TextField()
    ayah = NumberField(column_name="number")
    surah = NumberField(column_name="surah_number")
    content = MapField()

    class Meta:
        collection_name = "quran"
