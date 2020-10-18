# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
import gettext
import i18n
import locale
import pytz
import time
from datetime import datetime
from pprint import pprint
from pytz import timezone


def example_gettext():
    # Import gettext module

    # Set the local directory
    localedir = './locale'

    # Set up your magic function
    translate = gettext.translation('appname', localedir, fallback=True)
    _ = translate.gettext

    # Translate message
    print(_("Hello World"))


def example_tz():
    format = "%Y-%m-%d %H:%M:%S %Z%z"
    timezones = ['America/Los_Angeles', 'Europe/Madrid', 'America/Puerto_Rico', 'America/Sao_Paulo']
    for zone in timezones:
        now_time = datetime.now(timezone(zone))
        zone_time = now_time.strftime(format)
        print(zone_time)


def example_i18n_translate0():
    i18n.add_translation('String in Language 1', 'String in Language 2')
    r = i18n.t('String in Language 1')  # String in Language 2
    print(r)


def example_i18n_translate1():
    """ this uses translate.en.yml """
    i18n.load_path.append('.')
    return i18n.t('translate.str1')  # String in Language 1


def exampla_i18n_pluralization():
    i18n.add_translation('unread_number', {
        'zero': 'You do not have any unread mail.',
        'one': 'You have a new unread mail.',
        'few': 'You only have %{count} unread mails.',
        'many': 'You have %{count} unread mails.'
    })
    print(f"""{i18n.t('unread_number', count=0)}  # You do not have any unread mail.
{i18n.t('unread_number', count=1)}  # You have a new unread mail.
{i18n.t('unread_number', count=2)}  # You only have 2 unread mails.
{i18n.t('unread_number', count=15)}  # You have 15 unread mails.""")


def example_i18n_switch_lang():
    LOCALES = ['en-uk', 'en-in', 'pt-br']

    TIMEZONES = {
        'en-uk': 'Europe/London',
        'en-in': 'Asia/Kolkata',
        'pt-br': 'America/Sao_Paulo',
    }

    def change_locale(locale):
        if locale not in LOCALES:
            raise NameError
        LOCALE = locale
        TIMEZONE = TIMEZONES[LOCALE]
        return TIMEZONE

    print(change_locale('pt-br'))


def example_i18n_switch_lang1():
    TIMEZONES = {
        'en-uk': 'Europe/London',
        'en-in': 'Asia/Kolkata',
        'pt-br': 'America/Sao_Paulo',
    }

    def change_locale(locale):
        LOCALE = locale.lower()
        return TIMEZONES.get(LOCALE, 'UTC')

    print(change_locale('pt'))


def all_zones_tz():
    for tz in pytz.all_timezones:
        print(tz)

    # print(pytz.all_timezones_set)
    # print(pytz.all_timezones)
    # print(pytz.country_timezones)
    # print(pytz.country_names)
    print()


def all_locales():
    return locale.locale_alias


def example_i18n_switch_lang2():
    numero = 154623.56
    valor = 1123.5
    TIMEZONES = {
        'pt_BR': 'America/Sao_Paulo',
        'de_DE': 'Europe/Dublin',
        'en_US': 'UTC',
        'ru_RU': 'Europe/Moscow',
        'es_ES': 'Europe/Madrid',
        'fr_FR': 'Europe/Paris',
        'it_IT': 'Europa/Rome',
        'he_IL': 'Hebrew',
        'ar_LB': 'Asia/Istanbul',
        'hi_IN': 'Asia/Kolkata',
        'ja_JP': 'Japan',
    }

    def change_locale(locale):
        return TIMEZONES.get(locale, 'C')

    for l in TIMEZONES:
        locale.setlocale(locale.LC_ALL, l)
        print(change_locale(l))
        print(f'{l}-{TIMEZONES[l]}: {locale.format_string("%.2f", numero, True)}; {locale.currency(valor)}; {time.strftime("%A, %d %B %Y")}')


def example_gettext1():
    # Set the local directory
    localedir = './locale'
    current_locale = locale.getlocale()[0]
    # print(current_locale)
    # Set up your magic function
    translate = gettext.translation('Wednesday', localedir, languages=[current_locale], fallback=True)
    _ = translate.gettext

    # Translate message
    print(_("Hello World"))


def example_i18n(lang='pt'):
    i18n.load_path.append('.locale')
    i18n.set('fallback', 'en')
    i18n.set('locale', lang)
    return f"""{i18n.t('foo.hi')}"""


def example_i18n1(lang='pt', param='sat'):
    i18n.load_path.append('.locale')
    i18n.set('fallback', 'en')
    i18n.set('locale', lang)
    return f"""{i18n.t(f'i18n.{param}')}"""


def run():
    # example_gettext()
    # example_tz()
    # print(example_i18n_translate0())
    # print(example_i18n_translate1())
    # exampla_i18n_pluralization()
    # example_i18n_switch_lang()
    # example_i18n_switch_lang1()
    # all_zones_tz()
    # pprint(all_locales())
    # example_i18n_switch_lang2()
    # example_gettext1()
    for i in ['pt', 'en', 'de', 'hi', 'ar', 'he', 'ja', 'es', 'it', 'fr', 'eo']:
        print(f'{i}: ', end='')
        # print(example_i18n(i))
        for x in ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']:
            print(example_i18n1(i, x), end=' ')
        print()


if __name__ == '__main__':
    run()
