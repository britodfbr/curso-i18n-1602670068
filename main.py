# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import this
import operation_dicts
# import example_tz_work
import translations_goo
import translations_i18n


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def run():
    print_hi('PyCharm')
    funcs = [
        translations_goo.example16,
        translations_i18n.example_i18n_pluralization,
        translations_i18n.example_i18n2,
        translations_i18n.all_zones_tz,
        translations_i18n.all_locales,
        translations_goo.example17,
    ]
    for i in funcs:
        print(f'\n---\n{i.__name__}\n---\ni.__doc__\n\n')
        i()
        print('---')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
