import json

def smaller_dictionaries():
    dictionary_consist_of_3_smaller_dictionary={}
    dictionary_consist_of_3_smaller_dictionary["person_1"]={"surname":None,"name":None,"age":None,"profession":None,"marital status":None}
    dictionary_consist_of_3_smaller_dictionary["person_2"]={"surname":None,"name":None,"age":None,"profession":None,"marital status":None}
    dictionary_consist_of_3_smaller_dictionary["person_3"]={"surname":None,"name":None,"age":None,"profession":None,"marital status":None}

    with open('data.json', 'w') as fp:
        json.dump(dictionary_consist_of_3_smaller_dictionary, fp, indent=4)
        
smaller_dictionaries()

