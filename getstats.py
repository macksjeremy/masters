import textstat
def obtainstatistic(test_data):
    print("Calculating Statistics for:", test_data)
    print("-------------------------------------------------------------------------------------")
    print("fleschreadingease:", textstat.flesch_reading_ease(test_data))
    print("kincaid grade",textstat.flesch_kincaid_grade(test_data))
    print("smog index", textstat.smog_index(test_data))
    print("coleman index", textstat.coleman_liau_index(test_data))
    print("automated readability index",textstat.automated_readability_index(test_data))
    print("dale_chall readability:", textstat.dale_chall_readability_score(test_data))
    print("Difficult words", textstat.difficult_words(test_data))
    print("linsear:",textstat.linsear_write_formula(test_data))
    print("-------------------------------------------------------------------------------------")
    return