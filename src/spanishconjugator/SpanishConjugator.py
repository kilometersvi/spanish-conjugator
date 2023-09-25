# -*- coding: iso-8859-15 -*-

# --------------------------------- Importing Tenses From Files ---------------------------- #
from spanishconjugator.tenses.indicative.preterite import indicative_preterite
from spanishconjugator.tenses.indicative.present import indicative_present
from spanishconjugator.tenses.indicative.imperfect import indicative_imperfect
from spanishconjugator.tenses.indicative.future import indicative_future
from spanishconjugator.tenses.indicative.present_perfect import (
    indicative_present_perfect,
)
from spanishconjugator.tenses.indicative.past_perfect import indicative_past_perfect
from spanishconjugator.tenses.indicative.past_anterior import indicative_past_anterior
from spanishconjugator.tenses.indicative.future_perfect import indicative_future_perfect

from spanishconjugator.tenses.conditional.simple_conditional import (
    conditional_simple_conditional,
)
from spanishconjugator.tenses.conditional.perfect import conditional_perfect

from spanishconjugator.tenses.imperative.affirmative import affirmative
from spanishconjugator.tenses.imperative.negative import negative

from spanishconjugator.tenses.subjunctive.present import subjunctive_present
from spanishconjugator.tenses.subjunctive.present_perfect import (
    subjunctive_present_perfect,
)
from spanishconjugator.tenses.subjunctive.pluperfect import subjunctive_pluperfect
from spanishconjugator.tenses.subjunctive.future_perfect import (
    subjunctive_future_perfect,
)
from spanishconjugator.tenses.subjunctive.imperfect import subjunctive_imperfect
from spanishconjugator.tenses.subjunctive.imperfect_se import subjunctive_imperfect_se
from spanishconjugator.tenses.subjunctive.future import subjunctive_future

# --------------------------------- Irregulars --------------------------------------------- #
from spanishconjugator.irregulars.irregular_dict import irregulars_dictionary

# --------------------------------- Conjugator --------------------------------------------- #


class Conjugator:
    def conjugate(self, root_verb, tense, mood, pronoun=None, return_attrs=False):
        tense = tense.lower()
        mood = mood.lower()
        try:
            if pronoun:
                pronoun = pronoun.lower()

                try:
                    conjugation = irregulars_dictionary[root_verb][mood][tense][pronoun]
                    c_dt = {"result":conjugation,"flag":"irregular","mood":mood,"tense":tense,"pronoun":pronoun,"root_verb":root_verb}

                    if return_attrs:
                        return c_dt
                    else:
                        return conjugation
                except:
                    # root_verb does not have an irregular conjugation with the given pronoun
                    c_dt = self.conjugate_tense_mood(root_verb, tense, mood, pronoun)

                    if return_attrs:
                        return c_dt
                    else:
                        return c_dt['result']

            else:
                # in case no pronoun is passed
                c_dt = self.conjugate_tense_mood(root_verb, tense, mood, None)

                if return_attrs:
                    return c_dt
                else:
                    return c_dt['result']

        except:
            # --------------------------------- Catch Missed Conjugations ------------------------------- #
            return "Error - verb not found"


    def conjugate_tense_mood(self, root_verb, tense, mood, pronoun=None):
        c_dt = {}

        # --------------------------------- The Indicatives ---------------------------------------- #

        # --------------------------------- Present Indicative ------------------------------------- #
        if tense == "present":
            if mood == "indicative":
                c_dt = indicative_present(root_verb, pronoun)


        # --------------------------------- Imperfect Indicative ----------------------------------- #

        if tense == "imperfect":
            if mood == "indicative":
                c_dt = indicative_imperfect(root_verb, pronoun)


        # --------------------------------- Preterite Indicative ----------------------------------- #

        if tense == "preterite":
            if mood == "indicative":
                c_dt = indicative_preterite(root_verb, pronoun)


        # --------------------------------- Future Simple Indicative ------------------------------- #

        if tense == "future":
            if mood == "indicative":
                c_dt = indicative_future(root_verb, pronoun)


        # --------------------------------- Present Perfect Compound Tense -------------------------- #

        if tense == "present_perfect":
            if mood == "indicative":
                c_dt = indicative_present_perfect(root_verb, pronoun)


        # --------------------------------- Past Perfect Compound Tense ----------------------------- #

        if tense == "past_perfect":
            if mood == "indicative":
                c_dt = indicative_past_perfect(root_verb, pronoun)


        # --------------------------------- Past Anterior Compound Tense ---------------------------- #

        if tense == "past_anterior":
            if mood == "indicative":
                c_dt = indicative_past_anterior(root_verb, pronoun)


        # --------------------------------- Future Perfect Compound Tense --------------------------- #

        if tense == "future_perfect":
            if mood == "indicative":
                c_dt = indicative_future_perfect(root_verb, pronoun)



        # --------------------------------- The Conditional ----------------------------------------- #

        #---------------------------------- Simple Conditional -------------------------------------- #

        if tense == "simple_conditional":
            if mood == "conditional":
                c_dt = conditional_simple_conditional(root_verb, pronoun)


        #---------------------------------- Perfect Conditional -------------------------------------- #

        if tense == "perfect":
            if mood == "conditional":
                c_dt = conditional_perfect(root_verb, pronoun)


        # --------------------------------- The Imperative ----------------------------------------- #

        #---------------------------------- Affirmative Imperative -------------------------------------- #

        if tense == "affirmative":
            if mood == "imperative":
                c_dt = affirmative_wrapper(root_verb, pronoun)


        #---------------------------------- Negative Imperative -------------------------------------- #

        if tense == "negative":
            if mood == "imperative":
                c_dt = negative(root_verb, pronoun)


        # --------------------------------- The Subjunctive ----------------------------------------- #

        #---------------------------------- Present Subjunctive ------------------------------------- #

        if tense == "present":
            if mood == "subjunctive":
                c_dt = subjunctive_present(root_verb, pronoun)


        #---------------------------------- Present Perfect Subjunctive ----------------------------- #

        if tense == "present_perfect":
            if mood == "subjunctive":
                c_dt = subjunctive_present_perfect(root_verb, pronoun)


        #---------------------------------- Pluperfect Subjunctive ---------------------------------- #

        if tense == "pluperfect":
            if mood == "subjunctive":
                c_dt = subjunctive_pluperfect(root_verb, pronoun)


        #---------------------------------- Future Perfect Subjunctive ------------------------------ #

        if tense == "future_perfect":
            if mood == "subjunctive":
                c_dt = subjunctive_future_perfect(root_verb, pronoun)


        #---------------------------------- Imperfect Subjunctive -------------------------------------- #

        if tense == "imperfect":
            if mood == "subjunctive":
                c_dt = subjunctive_imperfect(root_verb, pronoun)


        #---------------------------------- imperfect se Subjunctive -------------------------------------- #

        if tense == "imperfect_se":
            if mood == "subjunctive":
                c_dt = subjunctive_imperfect_se(root_verb, pronoun)


        #---------------------------------- Future Subjunctive -------------------------------------- #

        if tense == "future":
            if mood == "subjunctive":
                c_dt = subjunctive_future(root_verb, pronoun)


        c_dt["mood"] = mood
        c_dt["tense"] = tense
        c_dt["root_verb"] = root_verb
        c_dt["pronoun"] = pronoun

        return c_dt

    def affirmative_wrapper(root_verb, pronoun):
        if pronoun in ["usted", "ustedes"]:
            p_i = self.conjugate(root_verb, "indicative", "present", pronoun="yo", return_attrs=False)
            if p_i != "Error - verb not found":
                return affirmative(p_i, pronoun)
        else:
            return affirmative(p_i, pronoun)
