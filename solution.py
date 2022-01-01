def count_occur(sub_list):
    character_set = {}
    for i in sub_list: 
        if i in character_set:
            character_set[i] += 1
        else:
            character_set[i] = 1
    return character_set
    
words = [
   "examples", "shows", "how", "to", "set", "a", "limit",
   "for", "a", "group", "of", "product", "store", "or",
   "a", "product", "store", "scope", "with", "the",
   "lower", "limit", "table", "parameter","rest", "of",
   "the", "scope", "uses", "the", "limit", "set", "with",
   "lower", "limit", "parameter"
]
string = "a scope uses product set with a limit parameter"

def is_valid_sentence(word_list, sentence):
    sentence = sentence.split()
    a_1 = count_occur(word_list)
    a_2 = count_occur(sentence)
    for key, val in a_2.items(): 
        try:
            if a_1[key] < val: 
                return Falses
        except:
            return False

    return True 

print(is_valid_sentence(words, string))