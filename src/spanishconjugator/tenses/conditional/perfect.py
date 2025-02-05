# -*- coding: iso-8859-15 -*-
from spanishconjugator.irregulars.irregular_dict              import irregulars_dictionary
def conditional_perfect_first_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["conditional"]["perfect_conditional"]["yo"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"habría " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"habría " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def conditional_perfect_first_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["conditional"]["perfect_conditional"]["nosotros"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"habríamos " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"habríamos " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        

def conditional_perfect_second_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["conditional"]["perfect_conditional"]["tu"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"habrías " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"habrías " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def conditional_perfect_second_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["conditional"]["perfect_conditional"]["vosotros"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"habríais " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"habríais " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def conditional_perfect_third_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["conditional"]["perfect_conditional"]["usted"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"habría " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"habría " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def conditional_perfect_third_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["conditional"]["perfect_conditional"]["ustedes"]
        return  {"result":conjugation,"flag":"irregular","mood":"","tense":"","pronoun":"","root_verb":""}
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"habrían " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"habrían " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

def conditional_perfect(root_verb, pronoun):
    if pronoun == "yo":
        return conditional_perfect_first_person_singular(root_verb)
            
    elif pronoun == "tu":
        return conditional_perfect_second_person_singular(root_verb)


    elif pronoun == "usted" or pronoun == "el" or pronoun == "ella":
        return conditional_perfect_third_person_singular(root_verb)


    elif pronoun == "nosotros":
        return conditional_perfect_first_person_plural(root_verb)


    elif pronoun == "vosotros":
        return conditional_perfect_second_person_plural(root_verb)


    elif pronoun == "ustedes" or pronoun == "ellos" or pronoun == "ellas":
        return conditional_perfect_third_person_plural(root_verb)

    else:
        # no pronoun is given
        _dict = {'el/ella/usted': conditional_perfect_third_person_singular(root_verb), \
                 'ellos/ellas/ustedes':conditional_perfect_third_person_plural(root_verb),\
                 'tu':conditional_perfect_second_person_singular(root_verb),\
                 'vosotros':conditional_perfect_second_person_plural(root_verb),\
                 'yo':conditional_perfect_first_person_singular(root_verb),\
                 'nosotros':conditional_perfect_first_person_plural(root_verb)\
                }
        return _dict