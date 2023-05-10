city = str(input('Em qual cidade você nasceu? ')).strip()
print('Você nasceu em {}.' .format(city))
print('A sua cidade possui "Santo" no nome? {}' .format(city[:5].upper() == 'SANTO'))
