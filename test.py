from dbutils import *
from Disease import Disease

init()

# disease = Disease(name="Cold",pd=9000, cli=6000, loc=4000, symptoms=['nausea','mild fever','headache','vomiting','body ache','throat ache','cough'])
# insertDisease(disease)
#
disease = Disease(name="Typhoid",pd=4500, cli=3000, loc=6000,symptoms=['nausea', 'rash', 'weakness', 'abdominal pain', 'high fever', 'headache', 'constipation','confusion', 'diarrhoea','vomiting'])
insertDisease(disease)

#print(getDiseases(["nausea"]))
