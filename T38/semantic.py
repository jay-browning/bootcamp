__author__ = "Jay Browning"

# this program will check for similarity between two strings

import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(f'{word1} and {word2} similarity = {word1.similarity(word2)}')
print(f'{word3} and {word2} similarity = {word3.similarity(word2)}')
print(f'{word3} and {word1} similarity = {word3.similarity(word1)}\n\n')

# as the 'interesting' points about the comparisons above have already been pointed out in the instructions
# pdf, so I've compared three words of my own below.

word1 = nlp("boat")
word2 = nlp("train")
word3 = nlp("captain")
print(f'{word1} and {word2} similarity = {word1.similarity(word2)}')
print(f'{word3} and {word2} similarity = {word3.similarity(word2)}')
print(f'{word3} and {word1} similarity = {word3.similarity(word1)}\n\n')

'''
Results:
boat and train similarity = 0.4188301721388612
captain and train similarity = 0.20810945418210208
captain and boat similarity = 0.29320689178076254
'''
# I would have thought that boat and captain would have a higher similarity rating, similar to banana and monkey
# and that boat and train would be more similar due to them both being vehicles or modes of transport
# I suppose that having only seen like six similarity ratings I've not got a very large dataset of ratings to compare


tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print(f'\n')


sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

print(f'base sentence: {sentence_to_compare}\n')
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


'''
results from en_core_web_md:
cat and monkey similarity = 0.5929930274321619
banana and monkey similarity = 0.40415016164997786
banana and cat similarity = 0.22358825939615987


boat and train similarity = 0.4188301721388612
captain and train similarity = 0.20810945418210208
captain and boat similarity = 0.29320689178076254


cat cat 1.0
cat apple 0.2036806046962738
cat monkey 0.5929930210113525
cat banana 0.2235882580280304
apple cat 0.2036806046962738
apple apple 1.0
apple monkey 0.2342509925365448
apple banana 0.6646699905395508
monkey cat 0.5929930210113525
monkey apple 0.2342509925365448
monkey monkey 1.0
monkey banana 0.4041501581668854
banana cat 0.2235882580280304
banana apple 0.6646699905395508
banana monkey 0.4041501581668854
banana banana 1.0


base sentence: Why is my cat on the car

where did my dog go -  0.630065230699739
Hello, there is my car -  0.8033180111627156
I've lost my car in my car -  0.6787541571030323
I'd like my boat back -  0.5624940517078084
I will name my dog Diana -  0.6491444739190607
'''

'''
results using en_core_web_sm:
cat and monkey similarity = 0.6770565478895127
banana and monkey similarity = 0.7276309976205778
banana and cat similarity = 0.6806929391210822


boat and train similarity = 0.5346879972376472
captain and train similarity = 0.4401866534691076
captain and boat similarity = 0.7393210693551548


cat cat 1.0
cat apple 0.7018378973007202
cat monkey 0.6455236077308655
cat banana 0.2214718759059906
apple cat 0.7018378973007202
apple apple 1.0
apple monkey 0.7389943599700928
apple banana 0.36197030544281006
monkey cat 0.6455236077308655
monkey apple 0.7389943599700928
monkey monkey 1.0
monkey banana 0.4232020080089569
banana cat 0.2214718759059906
banana apple 0.36197030544281006
banana monkey 0.4232020080089569
banana banana 1.0


base sentence: Why is my cat on the car

semantic.py:12: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(f'{word1} and {word2} similarity = {word1.similarity(word2)}')
semantic.py:13: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(f'{word3} and {word2} similarity = {word3.similarity(word2)}')
semantic.py:14: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(f'{word3} and {word1} similarity = {word3.similarity(word1)}\n\n')
semantic.py:22: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(f'{word1} and {word2} similarity = {word1.similarity(word2)}')
semantic.py:23: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(f'{word3} and {word2} similarity = {word3.similarity(word2)}')
semantic.py:24: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(f'{word3} and {word1} similarity = {word3.similarity(word1)}\n\n')
semantic.py:40: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Token.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(token1.text, token2.text, token1.similarity(token2))
semantic.py:55: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  similarity = nlp(sentence).similarity(model_sentence)
where did my dog go -  0.4043351553824302
Hello, there is my car -  0.5648939507997681
I've lost my car in my car -  0.548028403302901
I'd like my boat back -  0.3007499696891998
I will name my dog Diana -  0.3904074310483232
'''

# overall, the ratings are quite different, in some cases dramatically.
# this seems to be the result of the error messages returned when running the code
