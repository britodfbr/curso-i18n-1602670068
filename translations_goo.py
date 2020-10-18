# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
"""https://www.thepythoncode.com/article/translate-text-in-python"""
import yaml
from googletrans import Translator, constants
from pprint import pprint
from pathlib import Path
# init the Google API translator
translator = Translator()


def example1():
    """
    # translate a spanish text to english text (by default)
    """
    translation = translator.translate("Hola Mundo")
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


def example2():
    """
    # translate a spanish text to arabic for instance
    :return:
    """
    translation = translator.translate("Hola Mundo", dest="ar")
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


def example3():
    """
    # specify source language
    :return:
    """
    translation = translator.translate("Wie gehts ?", src="de")
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


def example4():
    """
    # print all translations and other data

    :return:
    """
    translation = translator.translate("Wie gehts ?", src="de")
    pprint(translation.extra_data)


def example5():
    """
    # translate more than a phrase
    :return:
    """
    sentences = [
        "Hello everyone",
        "How are you ?",
        "Do you speak english ?",
        "Good bye!"
    ]
    translations = translator.translate(sentences, dest="tr")
    for translation in translations:
        print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


def example6():
    """
    # detect a language
    :return:
    """
    detection = translator.detect("नमस्ते दुनिया")
    print("Language code:", detection.lang)
    print("Confidence:", detection.confidence)
    return detection


def example7():
    """
    This will return the language code, to get the full language name,
     you can use the LANGUAGES dictionary provided by Googletrans
    :return:
    """
    detection = example6()
    # detection = translator.detect("नमस्ते दुनिया")
    print("Language:", constants.LANGUAGES[detection.lang])


def example8():
    """
    Supported Languages
    # print all available languages
    :return:
    """
    print("Total supported languages:", len(constants.LANGUAGES))
    print("Languages:")
    pprint(constants.LANGUAGES)


def t():
    return translator.translate(text="Wie gehts ?", src="de", dest="ar")


def example9():
    """
    :return:
    """
    print(f'{t()}'
          f'{translator.translate("नमस्ते दुनिया", dest="pt")}')


def example10():
    """"""
    file = Path('.locale')/'foo.pt.yml'
    data = file.read_text()
    tdata = translator.translate(data, dest='he', src='pt')
    print(f'{tdata.origin}/{tdata.src}\n{tdata.text}/{tdata.dest}')


def example11():
    """
    translate only content from file yalm
    :return:
    """
    file = Path('.locale')/'foo.en.yml'
    with file.open() as f:
        content = yaml.load_all(f, Loader=yaml.FullLoader)

        for doc in content:
            for k, v in doc.items():
                print(k, "->", v)


def example12():
    """
    :return:
    """
    file = Path('.locale')/'foo.en.yml'
    with file.open() as f:
        d = yaml.load(f, Loader=yaml.FullLoader)
        print(type(d), d)


def example13():
    """
    :return:
    """
    d = None
    file = Path('.locale')/'foo.en.yml'
    with file.open() as f:
        d = yaml.load(f, Loader=yaml.FullLoader)
    print(type(d), d)


def example14():
    """
    :return:
    """
    d = None
    e = {}
    t = {}
    file = Path('.locale')/'foo.en.yml'
    with file.open() as f:
        d = yaml.load(f, Loader=yaml.FullLoader)
    # print(type(d), d)
    for k, v in d['en'].items():
        t[k] = translator.translate(v, dest='he', src='pt').text
    e['he'] = t
    print(e)


def example15():
    """
    :return:
    """
    d = None
    e = {}
    t = {}
    file = Path('.locale')/'foo.en.yml'
    with file.open() as f:
        d = yaml.load(f, Loader=yaml.FullLoader)
    # print(type(d), d)
    for k, v in d['en'].items():
        t[k] = translator.translate(v, dest='he', src='pt').text
    e['he'] = t
    print(e)
    with Path('.locale/i18n.he.yaml').open('w') as f:
        yaml.dump(e, f)


def example16():
    """
    translate only content from file yalm
    :return:
    """
    d = None
    e = None
    t = {}
    file = Path('.locale')/'foo.en.yml'
    with file.open() as f:
        d = yaml.load(f, Loader=yaml.FullLoader)
    # languages = ['pt', 'en', 'ge', 'hi', 'ar', 'he', 'ja', 'es', 'it', 'fr']
    languages = ['pt', 'en', 'es', 'it', 'fr', 'de', 'ru', 'eo', 'hi', 'ar', 'he', 'ja', 'zh-cn']
    for lang in languages:
        e = {}
        print(lang)
        for k, v in d['en'].items():
            t[k] = translator.translate(v, dest=lang).text
        e[lang] = t
        print(e)
        with Path(f'.locale/i18n.{lang}.yml').open('w') as f:
            yaml.dump(e, f)


def run():
    for i in range(16, 20):
        func = f'example{i}'
        try:
            print(f'-- {func} --')
            print(eval(func).__doc__)
            eval(func)()
        except NameError:
            pass
        finally:
            print('\n\n')


if __name__ == '__main__':
    run()
