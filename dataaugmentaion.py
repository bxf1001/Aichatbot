import nltk
from nltk.corpus import wordnet, stopwords
from random import randint

nltk.download('wordnet')
nltk.download('stopwords')

def synonym_replacement(sentence):
    words = nltk.word_tokenize(sentence)
    stop_words = set(stopwords.words('english'))
    new_words = words.copy()
    
    random_word = words[randint(0, len(words)-1)]
    
    # Choose a random word that is not a stop word
    while random_word in stop_words:
        random_word = words[randint(0, len(words)-1)]
    
    # Get synonyms of the word
    synonyms = wordnet.synsets(random_word)
    
    # If synonyms are found, replace the word with a synonym
    if synonyms:
        synonym = synonyms[0].lemmas()[0].name()
        new_words = [synonym if word == random_word else word for word in words]
    
    return " ".join(new_words)

# Test the function
sentence = "hi, how are you doing?"
print(synonym_replacement(sentence))