# -*- coding: iso-8859-15 -*-
from spanishconjugator.irregulars.irregular_dict              import irregulars_dictionary
def indicative_past_perfect_first_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["past_perfect"]["yo"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"había " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"había " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_past_perfect_first_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["past_perfect"]["nosotros"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"habíamos " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"habíamos " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_past_perfect_second_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["past_perfect"]["tu"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
                conjugation = root_verb[:-2] + "ado"
                return {"result":"habías " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"habías " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_past_perfect_second_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["past_perfect"]["vosotros"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"habíais " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"habíais " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_past_perfect_third_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["past_perfect"]["usted"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"había " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"había " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_past_perfect_third_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["past_perfect"]["ustedes"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"habían " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"habían " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def indicative_past_perfect(root_verb, pronoun):
    if pronoun == "yo":
        return indicative_past_perfect_first_person_singular(root_verb)

    elif pronoun == "tu":
        return indicative_past_perfect_second_person_singular(root_verb)
        
    elif pronoun == "usted" or pronoun == "el" or pronoun == "ella":
        return indicative_past_perfect_third_person_singular(root_verb)
        
    elif pronoun == "nosotros":
        return indicative_past_perfect_first_person_plural(root_verb)
        
    elif pronoun == "vosotros":
        return indicative_past_perfect_second_person_plural(root_verb)
        
    elif pronoun == "ustedes" or pronoun == "ellos" or pronoun == "ellas":
        return indicative_past_perfect_third_person_plural(root_verb)

    else:
        # no pronoun is given
        _dict = {'el/ella/usted': indicative_past_perfect_third_person_singular(root_verb), \
                 'ellos/ellas/ustedes':indicative_past_perfect_third_person_plural(root_verb),\
                 'tu':indicative_past_perfect_second_person_singular(root_verb),\
                 'vosotros':indicative_past_perfect_second_person_plural(root_verb),\
                 'yo':indicative_past_perfect_first_person_singular(root_verb),\
                 'nosotros':indicative_past_perfect_first_person_plural(root_verb)\
                }
        return _dict
       