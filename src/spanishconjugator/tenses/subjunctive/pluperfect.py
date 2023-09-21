# -*- coding: iso-8859-15 -*-
def subjunctive_pluperfect(root_verb, pronoun):
    if pronoun == "yo":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"hubiera " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"hubiera " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "tu":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"hubieras " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"hubieras " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "usted":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"hubiera " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"hubiera " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "nosotros":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"hubiéramos " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"hubiéramos " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "vosotros":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"hubierais " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"hubierais " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}

    if pronoun == "ustedes":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return {"result":"hubieran " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return {"result":"hubieran " + conjugation,"flag":"none","mood":"","tense":"","pronoun":"","root_verb":""}
