__author__ = "Jay Browning"

# this program will compare movie descriptions to make a recommendation using semantic similarity in the spaCy package

import spacy

nlp = spacy.load('en_core_web_md')

movies_desc = []
recc_scores = []
hulk = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati 
       trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, 
       Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''

# read movies.txt file in to movies_desc, stripping line breaks
# and splitting into nested lists with 'movie x' and description as separate list items
with open('./movies.txt', 'r') as db:
    for line in db:
        movies_desc.append(line.strip('\n').split(' :'))


token_ = nlp(hulk)
for movie in movies_desc:                                   # iterate through list of movies descriptions
    token = nlp(movie[1])                                   # compare only the description, not the 'Movie x' portion
    recc_scores.append([token.similarity(token_), movie])   # run comparison, add to scores list for further analysis

# format and display scores, cause, why not.
print('************** scores **************')
for score in recc_scores:
    rejoin = ' - '.join(score[1])
    print(f'{score[0]:.5f} : {rejoin}')

# run check to determine the highest score, format and print out to console.
value = 0.0
for score in recc_scores:
    check = score[0]
    if check > value:
        value = check
        recco = ' - '.join(score[1])
print(f'\nyour reccomendation, with a score of {value:.5f} is:\n'
      f'{recco}\n')



