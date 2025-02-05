# -*- coding: iso-8859-15 -*-
from spanishconjugator.irregulars.irregular_dict              import irregulars_dictionary
def indicative_present_first_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present"]["yo"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "o"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "o"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "o"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_present_first_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present"]["nosotros"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "amos"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "emos"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "imos"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_present_second_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present"]["tu"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "as"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "es"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "es"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_present_second_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present"]["vosotros"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "áis"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "éis"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "ís"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_present_third_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present"]["usted"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "a"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "e"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "e"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_present_third_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present"]["ustedes"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "an"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "en"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "en"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_present(root_verb, pronoun):
    if pronoun == "yo":
        return indicative_present_first_person_singular(root_verb)
            
    elif pronoun == "tu":
        return indicative_present_second_person_singular(root_verb)


    elif pronoun == "usted" or pronoun == "el" or pronoun == "ella":
        return indicative_present_third_person_singular(root_verb)


    elif pronoun == "nosotros":
        return indicative_present_first_person_plural(root_verb)


    elif pronoun == "vosotros":
        return indicative_present_second_person_plural(root_verb)


    elif pronoun == "ustedes" or pronoun == "ellos" or pronoun == "ellas":
        return indicative_present_third_person_plural(root_verb)

    else:
        # no pronoun is given
        _dict = {'el/ella/usted': indicative_present_third_person_singular(root_verb), \
                 'ellos/ellas/ustedes':indicative_present_third_person_plural(root_verb),\
                 'tu':indicative_present_second_person_singular(root_verb),\
                 'vosotros':indicative_present_second_person_plural(root_verb),\
                 'yo':indicative_present_first_person_singular(root_verb),\
                 'nosotros':indicative_present_first_person_plural(root_verb)\
                }
        return _dict
