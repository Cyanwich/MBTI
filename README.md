# What is this repo about

This is a CNN based text classifier that uses spaCy and is able to classify your Myers–Briggs personality type (e.g. INTJ, ENFP) based on a (self-)description or profile of your personality.  

# How to use it 

A new model will need to be trained using jupyter notebook as the current one is too large for upload. The version of spaCy that has been used for previous models is 2.2.3. 

'mbti.py' uses two functions: MBTI(text) and MBTIDoc(textfile) to type an input. MBTI(text) uses text that the user types as input for the function, whereas MBTIDoc(textfile) takes a directory to a .txt file and reads its content for input. A four-letter type based on dichotomies will be printed, as well as six two-letter group results.

# Loading from pre-trained model

This is done using mbti.py lines 1 and 2:

```
import spacy
nlp = spacy.load("./mbti profile model")
 ```

