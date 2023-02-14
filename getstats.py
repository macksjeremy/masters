import numpy as np
import textstat
def obtainstatistic(test_data, verbose=False):
    flesch = textstat.flesch_reading_ease(test_data)
    kincaid = textstat.flesch_kincaid_grade(test_data)
    smog = textstat.smog_index(test_data)
    liau = textstat.coleman_liau_index(test_data)
    ari = textstat.automated_readability_index(test_data)
    dale = textstat.dale_chall_readability_score(test_data)
    difficult = textstat.difficult_words(test_data)
    linsear = textstat.linsear_write_formula(test_data)
    if(verbose):
        print("Calculating Statistics for:", test_data)
        print("-------------------------------------------------------------------------------------")
        print("fleschreadingease:",flesch )
        print("kincaid grade",kincaid)
        print("smog index", smog)
        print("coleman index",liau )
        print("automated readability index",ari)
        print("dale_chall readability:", dale)
        print("Difficult words", difficult)
        print("linsear:",linsear)
        print("-------------------------------------------------------------------------------------")
    return np.asarray([flesch,kincaid,smog,liau,ari,dale,difficult,linsear])