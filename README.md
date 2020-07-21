# language-identification

This repository contains two different codes to detect languages from texts.

Part 1: Detects the language of a text by calculating the probability of a text being written in a language.

To do so :
- we used the stopwords() function to get all the stopwords of the languages in stopwords.fileids()
- than we used the function wordpunct_tokenize that extracts the tokens from strings of words or sentences in the form of Alphabetic and Non-Alphabetic character
- we compared between the stopwords of each language with the tokens we got from the text by using intersection() function
-finally we were able to get for each language of our text the lenght of stopwords 

To calculate the proability we needed the ratio(lenght of stopwords) of the two languages that have the most stopwords 
->  poba = most_rated_language_ratio/(most_rated_language_ratio+second_rated_language_ratio)*100
