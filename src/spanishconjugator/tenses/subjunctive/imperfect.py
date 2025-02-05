# -*- coding: iso-8859-15 -*-
def subjunctive_imperfect(root_verb, pronoun):
    if pronoun == "yo":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ara"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "iera"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "tu":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "aras"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ieras"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "usted":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ara"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "iera"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "nosotros":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "áramos"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "iéramos"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "vosotros":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "arais"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ierais"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "ustedes":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "aran"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ieran"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
