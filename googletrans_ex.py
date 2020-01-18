from googletrans import Translator

dave = Translator()
word = dave.translate('스타킹 페티쉬', dest='en', src='ko')
print(word.text)