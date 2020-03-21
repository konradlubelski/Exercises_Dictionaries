import json
import pprint

def smaller_dictionaries(number):
    dictionary_consist_of_3_smaller_dictionary ={f'person_{number}':{"surname":None,"name":None,"age":None,"profession":None,"marital status":None} for number in range (1,number+1)}
    with open('data.json', 'w') as fp:
        json.dump(dictionary_consist_of_3_smaller_dictionary, fp, indent=2)
        
smaller_dictionaries(3)
