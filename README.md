# Task37-Introduction_to_NLP

-- In order to access the spacy module within Python, you must first follow the below steps in the command line --
open command line (cmd)
Type in "pip3 install spacy"
Then, type "python3 -m spacy download en"

-- Once this has downloaded, you can then add it to the Python script by typing the below 2 lines at the top of your code --

import spacy #This statement should work if you have spaCy installed 
nlp = spacy.load('en_core_web_sm')
