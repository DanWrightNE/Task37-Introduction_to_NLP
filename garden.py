import spacy
nlp = spacy.load('en_core_web_sm')

# create garden path sentences list
garden_path_sentences = ["The old man the boat",
                         "The horse raced past the barn fell",
                         "The complex houses married and single soldiers and their families",
                         "We painted the wall with cracks",
                         "The wild walk with haste"]

# tokenise each sentence in list
garden1_token = [(token, token.orth_, token.orth) for token in nlp(garden_path_sentences[0])]
garden2_token = [(token, token.orth_, token.orth) for token in nlp(garden_path_sentences[1])]
garden3_token = [(token, token.orth_, token.orth) for token in nlp(garden_path_sentences[2])]
garden4_token = [(token, token.orth_, token.orth) for token in nlp(garden_path_sentences[3])]
garden5_token = [(token, token.orth_, token.orth) for token in nlp(garden_path_sentences[4])]

# Entity recognition for sentence 1 in list
nlp_garden1 = nlp(garden_path_sentences[0])
print([(i, i.label_, i.label) for i in nlp_garden1.ents])

# Entity recognition for sentence 2 in list
nlp_garden2 = nlp(garden_path_sentences[1])
print([(i, i.label_, i.label) for i in nlp_garden2.ents])

# Entity recognition for sentence 3 in list
nlp_garden3 = nlp(garden_path_sentences[2])
print([(i, i.label_, i.label) for i in nlp_garden3.ents])

# Entity recognition for sentence 4 in list
nlp_garden4 = nlp(garden_path_sentences[3])
print([(i, i.label_, i.label) for i in nlp_garden4.ents])

# Entity recognition for sentence 5 in list
nlp_garden5 = nlp(garden_path_sentences[4])
print([(i, i.label_, i.label) for i in nlp_garden5.ents])

# chopra sentence entry recognition to check the method works adn there isn't a problem with my code
Chopra = nlp("""known by her married name Priyanka Chopra Jonas, is an Indian actress, horse
singer, film producer, boat, philanthropist, and the winner of the Miss World 2000 pageant.
One of India's highest-paid and most popular celebrities, Chopra has received numerous
awards, including a National Film Award and five Filmfare Awards. In 2016, the Government
of India honoured her with the Padma Shri, and Time named her one of the 100 most influential people in the world.""")
print([(i, i.label_, i.label) for i in Chopra.ents])

# the output for the garden sentences are all blank, I think that this is down to the words used in them.

# categorisation terms that I was unsure of so researched to understand
# NORP - nationality or religious groups
# GPE - locations/cities etc.
# CARDINAL - 'counting' numbers