from mongoengine import *
from Disease import Disease


def init():
    connect('Health', host="localhost", port=27017)

def insertDisease(d):
    d.save()
    pass

def getDiseases(symptomps):

    objects = Disease.objects()

    result = []

    for disease in objects:

        for symptomp in symptomps:

            if(symptomp in disease.symptoms):

                result.append(disease)

            else:
                pass

    return result

