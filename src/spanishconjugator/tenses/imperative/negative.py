# -*- coding: iso-8859-15 -*-
def negative(root_verb, pronoun):
    if pronoun == "yo":
        return "prounoun 'yo' does not have imperative conjugations"

    if pronoun == "tu":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "es"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "as"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "as"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "usted":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "e"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "a"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "a"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "nosotros":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "emos"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "amos"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "amos"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "vosotros":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "éis"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "áis"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "áis"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "ustedes":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "en"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "an"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "an"
            return {"result":conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
