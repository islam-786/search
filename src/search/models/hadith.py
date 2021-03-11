from fireo.models import Model
from fireo.fields import TextField, NumberField, MapField, IDField, BooleanField


class Hadith(Model):
    id = IDField()
    hadith_number = NumberField()
    international_number = NumberField()
    book_number = NumberField()
    book_name = MapField()
    chapter = MapField()
    text = MapField()
    is_sahih = BooleanField()
    uci = TextField()

    class Meta:
        collection_name = "must_be_set_runtime"
