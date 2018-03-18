from dbutils import *
from Disease import Disease

init()

disease = Disease(name="Cholera",symptoms=['fatigue','body ache','nausea','vomiting','dehydration','water diarrhoea','lethargy'],pd=5000, loc=5000,cli=3000)
insertDisease(disease)

#print(getDiseases(["cold"]))
