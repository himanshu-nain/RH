from mongoengine import *
from Disease import Disease


def init():
    connect('Health', host="localhost", port=27017)

def insertDisease(d):
    d.save()
    pass

def getDiseases(symptoms):

    objects = Disease.objects()

    result = []

    for disease in objects:

        for symptom in symptoms:

            if(symptom in disease.symptoms):

                if(disease not in result):
                    result.append(disease)

            else:
                pass

    return result

