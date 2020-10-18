# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
"""https://under-linux.org/entry.php?b=1273"""
import time
import locale

numero = 154623.56
valor = 1123.5
sdate = "%A, %d %B %Y"

# default
print(f'{numero}; {valor}; {time.strftime(sdate)}')

# locale local
locale.setlocale(locale.LC_ALL, '')
print(f'{locale.format_string("%.2f", numero, True)}; {locale.currency(valor)}; {time.strftime(sdate)}')

# locale en
locale.setlocale(locale.LC_ALL, 'en_US')
print(f'{locale.format_string("%.2f", numero, True)}; {locale.currency(valor)}; {time.strftime(sdate)}')

# locale de-DE
locale.setlocale(locale.LC_ALL, 'de_DE')
print(f'{locale.format_string("%.2f", numero, True)}; {locale.currency(valor)}; {time.strftime(sdate)}')

# locale es-Es
locale.setlocale(locale.LC_ALL, 'es_ES')
print(f'{locale.format_string("%.2f", numero, True)}; {locale.currency(valor)}; {time.strftime(sdate)}')

# locale fr_FR
locale.setlocale(locale.LC_ALL, 'fr_FR')
print(f'{locale.format_string("%.2f", numero, True)}; {locale.currency(valor)}; {time.strftime(sdate)}')

# locale ar_LB
locale.setlocale(locale.LC_ALL, 'ar_LB')
print(f'{locale.format_string("%.2f", numero, True)}; {locale.currency(valor)}; {time.strftime(sdate)}')

# locale hi-IN
locale.setlocale(locale.LC_ALL, 'hi_IN')
print(f'{locale.format_string("%.2f", numero, True)}; {locale.currency(valor)}; {time.strftime(sdate)}')

# locale ja-JP
locale.setlocale(locale.LC_ALL, 'ja_JP')
print(f'{locale.format_string("%.2f", numero, True)}; {locale.currency(valor)}; {time.strftime(sdate)}')
