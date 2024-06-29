def single_root_words(root_word, *other_words):
    same_words = []


    for i in range(len(other_words)):
        if len(root_word) < len(other_words[i]): #

            if root_word.lower() in other_words[i].lower():
                same_words.append(other_words[i])

        if len(root_word) > len(other_words[i]):
            if other_words[i].lower() in root_word.lower():
                same_words.append(other_words[i])
    print(f'однокоренные слову {root_word}: {same_words}')

single_root_words('rich', 'richiest', 'orichalcam', 'cheers', 'richies,')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')


