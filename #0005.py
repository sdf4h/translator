from translate import Translator
a = input()
translator= Translator(to_lang="Russian")
translation = translator.translate(a)
print (translation)