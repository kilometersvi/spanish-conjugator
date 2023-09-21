# -*- coding: iso-8859-15 -*-
def indicative_future_perfect(root_verb, pronoun):
    if pronoun == "yo":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"habré " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"habré " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "tu":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"habrás " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"habrás " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "usted":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"habrá " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"habrá " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "nosotros":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"habremos " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"habremos " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "vosotros":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"habréis " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"habréis " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "ustedes":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"habrán " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"habrán " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
