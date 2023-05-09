from jellyfish import soundex
import csv


def indices(lst, item):
    return [i for i, x in enumerate(lst) if x == item]


data = {}
similar_sounding_words = {}

names = []
similar_names = []
sounds = []
popularity = []

# Loading data into lists and dictionaries for analysis
with open('Names (Example).csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        names.append(row[0])
        sounds.append(soundex(row[0]))
        popularity.append(row[1])
        data.update({row[0]: row[1]})

# Here we detect similar sounding words and note them in similar_sounding_words
for i in sounds:
    if len(indices(sounds, i)) > 1: # If its greater then 1 one means there are other names who sound similar. It return list with indexes of similar sounding words
        for j in indices(sounds, i):
            if names[j] not in similar_names:
                similar_names.append(names[j]) # We are appending those names here to avoid looping dictionary. If name is in this list means it has similar sounding words
            if sounds[j] not in similar_sounding_words:
                similar_sounding_words.update({sounds[j]: [[names[j], popularity[j]]]}) # it is appending dictionary with sound_code as key and list having name and popularity as values
            else:
                if [names[j], popularity[j]] not in similar_sounding_words[sounds[j]]:
                    similar_sounding_words[sounds[j]].append([names[j], popularity[j]]) # {B5002 : [["Christopher " : "2052438"], ["Christine", "587447"]]}

get_input = input("Enter Name: ")
print("")

if get_input in similar_names:
    for key, values in similar_sounding_words.items():
        if isinstance(values, list):
            for similar_sounding_names in values:
                if get_input in similar_sounding_names:
                    sorted_list = sorted(similar_sounding_words[key], key=lambda x: int(x[1]), reverse=True) # Re-Sorting List with highest population
                    for person in similar_sounding_words[key]:
                        print(f'{person[0]:20} : {person[1]:15}')
else:
    if get_input in data:
        print(f'{get_input:30} : {data[get_input]:30}')
    else:
        print("No Name Found")


