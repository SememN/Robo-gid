def read_db(path):
    with open(path, encoding='utf-8') as to_read:
        db = to_read.readlines()
    print(db[7])
    return db


db = read_db('answer_databse.txt')
