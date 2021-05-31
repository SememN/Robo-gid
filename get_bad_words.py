path_to_badwords = '' #enter your "bad" file name here

not_ok_list = []


def get_bad_words(path):
    bad_words = open(path, 'r', encoding='utf-8') #get the file
    s = bad_words.readlines()    # read the lines of file
    for i in range(len(s)):     #sorting lines
        s[i] = s[i].rstrip()
    bad_words.close()
    separate = ''.join(s)
    print(separate.split(','))
    return s


not_ok_list = get_bad_words(path_to_badwords)
