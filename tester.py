from classifier import classifier
from Disease import  Disease
from dbutils import getDiseases, init
init()

all = getDiseases(['constipation','nausea','headache','fever','abdominal pain'])

classifier(all, ['constipation','nausea','headache','fever','abdominal pain'])
