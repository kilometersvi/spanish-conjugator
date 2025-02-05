# -*- coding: iso-8859-15 -*-
from spanishconjugator.irregulars.irregular_dict              import irregulars_dictionary
def indicative_present_perfect_first_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present_perfect"]["yo"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"he " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"he " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_present_perfect_first_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present_perfect"]["nosotros"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"hemos " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"hemos " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_present_perfect_second_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present_perfect"]["tu"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"has " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"has " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_present_perfect_second_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present_perfect"]["vosotros"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"habéis " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"habéis " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_present_perfect_third_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present_perfect"]["usted"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"ha " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"ha " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_present_perfect_third_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present_perfect"]["ustedes"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"han " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"han " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_present_perfect(root_verb, pronoun):
    if pronoun == "yo":
        return indicative_present_perfect_first_person_singular(root_verb)

    elif pronoun == "tu":
        return indicative_present_perfect_second_person_singular(root_verb)
        
    elif pronoun == "usted" or pronoun == "el" or pronoun == "ella":
        return indicative_present_perfect_third_person_singular(root_verb)
        
    elif pronoun == "nosotros":
        return indicative_present_perfect_first_person_plural(root_verb)
        
    elif pronoun == "vosotros":
        return indicative_present_perfect_second_person_plural(root_verb)
        
    elif pronoun == "ustedes" or pronoun == "ellos" or pronoun == "ellas":
        return indicative_present_perfect_third_person_plural(root_verb)

    else:
        # no pronoun is given
        _dict = {'el/ella/usted': indicative_present_perfect_third_person_singular(root_verb), \
                 'ellos/ellas/ustedes':indicative_present_perfect_third_person_plural(root_verb),\
                 'tu':indicative_present_perfect_second_person_singular(root_verb),\
                 'vosotros':indicative_present_perfect_second_person_plural(root_verb),\
                 'yo':indicative_present_perfect_first_person_singular(root_verb),\
                 'nosotros':indicative_present_perfect_first_person_plural(root_verb)\
                }
        return _dict