from models.languageManager import LanguageManager

try:
    language = LanguageManager()

    # Gets languages
    languages = language.get_languages()
    print(languages)

except Exception as e:
    print(e)
