from dbutils import *
from Disease import Disease

init()


# disease = Disease(name="Flu",symptoms=['fatigue','body ache', 'cough','sore throat','fever','gastrointestinal disorder'],pd=10000, loc=8000,cli=2000)
# insertDisease(disease)

print(getDiseases(["a","b","c"]))
