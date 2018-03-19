from dbutils import *
from Disease import Disease

init()

# disease = Disease(name="Malaria",
#                   symptoms=['chills', 'fatigue', 'fever', 'night sweats', 'shivering', 'sweating', 'diarrhoea', 'nausea', 'vomiting', 'fast heart rate', 'headache', 'confusion', 'pallor', 'muscle pain', 'abdominal pain'],
#                   pd=6546,
#                   loc=2158,
#                   cli=3462)
# insertDisease(disease)
# disease = Disease(name="Typhoid Fever",
#                   symptoms=['abdominal pain', 'muscle pain', 'bloating', 'constipation', 'diarrhoea', 'nausea', 'vomiting', 'fatigue', 'fever', 'chills', 'loss of appetite', 'malaise', 'headache', 'muscle weakness', 'rash', 'weight loss'],
#                   pd=5000,
#                   loc=3000,
#                   cli=2500)
# insertDisease(disease)
# disease = Disease(name="Cholera",
#                   symptoms=['abdominal pain', 'nausea', 'diarrhoea', 'vomiting', 'dehydration', 'lethargy', 'electrolyte imbalance'],
#                   pd=6000,
#                   loc=4000,
#                   cli=2125)
# insertDisease(disease)
# disease = Disease(name="Flu",
#                   symptoms=['muscle pain', 'body pain', 'cough', 'chills', 'dehydration', 'fatigue', 'fever', 'flushing', 'loss of appetite', 'sweating', 'congestion', 'runny nose', 'sneezing', 'chest discomfort', 'confusion', 'headache', 'nausea', 'shortness of breath', 'sore throat', 'swollen lymph nodes'],
#                   pd=8000,
#                   loc=6000,
#                   cli=4000)
# insertDisease(disease)
# disease = Disease(name="Tuberculosis",
#                   symptoms=['chest pain', 'chest discomfort', 'cough','fatigue', 'fever', 'loss of appetite', 'malaise', 'sweating', 'muscle loss', 'phlegm', 'weight loss', 'shortness of breath', 'swollen lymph nodes'],
#                   pd=5782,
#                   loc=4928,
#                   cli=5928)
# insertDisease(disease)
# disease = Disease(name="Brucellosis",
#                   symptoms=['abdominal pain', 'back pain', 'joint pain', 'muscle pain', 'fever', 'chills', 'fatigue','loss of appetite', 'sweating', 'cough','headache','swollen lymph nodes','weight loss'],
#                   pd=1000,
#                   loc=800,
#                   cli=628)
# insertDisease(disease)
# disease = Disease(name="Jaundice",
#                   symptoms=['fatigue','abdominal pain','weight loss','vomiting','fever','pale stools','dark urine'],
#                   pd=4829,
#                   loc=2238,
#                   cli=2387)
# insertDisease(disease)
# disease = Disease(name="Diarrhoea",
#                   symptoms=['abdominal cramps','abdominal pain','nausea','vomiting','loose motion'],
#                   pd=8000,
#                   loc=7000,
#                   cli=2397)
#
# insertDisease(disease)

print(getDiseases(['constipation','nausea','headache','fever','abdominal pain']))
