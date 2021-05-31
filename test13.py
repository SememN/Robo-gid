test_list = ['привет', 'ежик', 'голубь1', 'один', 'два', 'три', 'четыре', 'пять']
not_ok_list = ['привет', 'ежик', 'один']
n = []


def srav():
    for i in range(len(test_list)):
        for g in range(len(not_ok_list)):
            if test_list[i] == not_ok_list[g]:
                n.append(i)
                print(n)
            else:
                print('ошибка')

srav()

n.reverse()
print(n)
for s in range(len(n)):
    del test_list[n[s]]
    print(test_list)




