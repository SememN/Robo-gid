from lemmatizer import prep_to_lemm, lemmatize


not_sorted = "/home/joker/Desktop/answerdatabase/answer_datebase1.txt"
shit_file = "/home/joker/Desktop/answerdatabase/badwords.txt"


def get_shit(file):
    shit_voc = []
    with open(file, 'r') as f:
        for line in f:
            for symb in line.split():
                shit_voc.append(symb)
    return shit_voc


def sort_db(file):
    """reading not sorted db and adding ok strings to list"""

    ok_list = []
    shit = get_shit(shit_file)
    with open(file, 'r') as f:
        for line in f:
            line = line.split('/', maxsplit=2)
            lemmed = lemmatize(prep_to_lemm(line[1]))  # lemmatized words
            flag = True

            for i in lemmed:
                if i in shit:
                    flag = False

            if flag:
                ok_list.append(line[1])

    return ok_list


def create_norm_db():
    unsorted = sort_db(not_sorted)
    with open('sorted_db', 'w', encoding='utf-8') as f:
        for line in unsorted:
            f.write(f'{line}\n')


create_norm_db()
