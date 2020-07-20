#coding:utf-8


import sys

try:
    from nltk import wordpunct_tokenize
    from nltk.corpus import stopwords
except ImportError:
    print ("[!] You need to install nltk (http://nltk.org/index.html)")


def calculate_ratios(text):

    ratios_dict = {}
    words_dict ={}
    #text tokenization
    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    #loop on the languages in stopwords
    for langue in stopwords.fileids():
        # oget stopwords from the selected language
        stopwords_set = set(stopwords.words(langue))
        #add the words of our text to a set
        words_set = set(words)
        # get the list intersection between the words of our text and the stopwords of the language
        common_words = words_set.intersection(stopwords_set)
        # add the number of the intersection list words
        ratios_dict[langue] = len(common_words)
        #add the intersection list of words
        words_dict[langue] = common_words

    return ratios_dict, words_dict


def detect_language(text):

    # get the ratio and words dictionnary
    ratios = calculate_ratios(text)
    
    #get the first most rated language
    first_rated_language = max(ratios[0], key=ratios[0].get)
    most_common_words = ratios[0][first_rated_language]
    
    #get the second most rated language
    sorted_language_list = sorted(ratios[0].items(), key=lambda item: item[1], reverse=True)
    second_rated_language = list(sorted_language_list)[1][0]
    second_most_common_words = ratios[0][second_rated_language]
    
    #print the probability
    print("\nThere is {0}% chances for this text to be writen in {1}\n" .format(calculate_probability(most_common_words, second_most_common_words), first_rated_language))


def calculate_probability(most, secode_most) :
    
    #calculate the probability of the language "most" to be the language in which the text is written
    proba = (float(most) /(most + secode_most) * 100)
    return round(proba)


def language_details(text, number):
    
    print("Text %d\n" %number)
    
    #  get text ratios and it's stopwords
    langlist=calculate_ratios(text)
    
    #sort the language list by ratio to print the most rated four languages 
    lang_list_sort=sorted(langlist[0].items(), key=lambda item: item[1], reverse=True)
    
    # print the ratio and the stopwords of the languages found
    for lang in lang_list_sort[0:4]:
        if lang[1] != 0 :
            print("\t{0} has {1} word(s)" .format(lang[0],lang[1]))
            print("\t\t{0} words list : {1}".format(lang[0],langlist[1][lang[0]]))
             
    detect_language(text)

    
    
if __name__=='__main__':

    #text snipet from http://latta.blog.lemonde.fr/2017/02/08/goal-line-technology-un-nouveau-bug-contre-son-camp/
    text1 = '''
    check if your able to understand the image bellow, it contains arabic text 
    that says "ماذا سيحدث لك إذا توقفت عن التدخين لمدة يوم؟".
    '''
    
    text2 = '''
    il faut utiliser l'article A devant un nom commençant par un son "consonne" et 'AN' devant un nom commençant par un son "voyelle".
    Exemples :
    - door (porte) > a door (une porte)
    /d/ est un son consonne
    - apple (pomme) > an apple (une pomme)
    /a/ est un son voyelle
    - kitchen (cuisine) > a kitchen (une cuisine)
    /k/ est un son consonne.
    '''
    
    text3 = '''
    ارتفعت حصيلة ضحايا فيروس كورونا في العالم إلى 600 ألف وفاة منذ ظهور الوباء في الصين في كانون الأول/ديسمبر 2019.
    وأحصيت 100 ألف وفاة جديدة خلال 21 يوما فقط أي منذ 28 حزيران/يونيو. أغلب هذه الوفيات  شهدتها أوروبا بـ205,065 وفا
    ة، تليها أمريكا اللاتينية بـ160 ألفا. فيما تم إحصاء أكثر من 14 مليون إصابة بالفيروس في 196 دولة ومنطقة.
    وتجدر الإشارة إلى أن هذه الأرقام لا تعكس إلا جزءا من العدد الحقيقي للإصابات.
    '''
    
    #*******************************************************
    print("Part1: Detect the probability of the language of a Text \n")
    language_details(text1, 1)
    language_details(text2, 2)
    language_details(text3, 3)
    
    
    
