picnicItems = {'Sandwiches': 4, 'Apples': 12, 'Drinks': 8, 'Snacks': 8, }


def printPicnic(dict, justify):
    print('PICNIC ITEMS'.center(justify, '-'))

    for k, v in dict.items():
        print(k.ljust(justify - 5, '.') + str(v).rjust(5, ' '))


printPicnic(picnicItems, 20)
printPicnic(picnicItems, 36)
