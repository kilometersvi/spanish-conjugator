# -*- coding: iso-8859-15 -*-
from spanishconjugator.irregulars.irregular_dict              import irregulars_dictionary
def conditional_simple_conditional_first_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["conditional"]["simple_conditional"]["yo"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "ía"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def conditional_simple_conditional_first_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["conditional"]["simple_conditional"]["nosotros"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "íamos"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def conditional_simple_conditional_second_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["conditional"]["simple_conditional"]["tu"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "ías"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def conditional_simple_conditional_second_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["conditional"]["simple_conditional"]["vosotros"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "íais"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def conditional_simple_conditional_third_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["conditional"]["simple_conditional"]["usted"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "ía"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def conditional_simple_conditional_third_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["conditional"]["simple_conditional"]["ustedes"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "ían"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def conditional_simple_conditional(root_verb, pronoun):
    if pronoun == "yo":
        return conditional_simple_conditional_first_person_singular(root_verb)
            
    elif pronoun == "tu":
        return conditional_simple_conditional_second_person_singular(root_verb)


    elif pronoun == "usted" or pronoun == "el" or pronoun == "ella":
        return conditional_simple_conditional_third_person_singular(root_verb)


    elif pronoun == "nosotros":
        return conditional_simple_conditional_first_person_plural(root_verb)


    elif pronoun == "vosotros":
        return conditional_simple_conditional_second_person_plural(root_verb)


    elif pronoun == "ustedes" or pronoun == "ellos" or pronoun == "ellas":
        return conditional_simple_conditional_third_person_plural(root_verb)

    else:
        # no pronoun is given
        _dict = {'el/ella/usted': conditional_simple_conditional_third_person_singular(root_verb), \
                 'ellos/ellas/ustedes':conditional_simple_conditional_third_person_plural(root_verb),\
                 'tu':conditional_simple_conditional_second_person_singular(root_verb),\
                 'vosotros':conditional_simple_conditional_second_person_plural(root_verb),\
                 'yo':conditional_simple_conditional_first_person_singular(root_verb),\
                 'nosotros':conditional_simple_conditional_first_person_plural(root_verb)\
                }
        return _dict
        
