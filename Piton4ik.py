import csv
import random

search = str(input('Search for:'))
cb = 0
cb_over30 = 0
random_books = []
popular_downloads = ['0'] * 20
popular = ['0'] * 20
tegs = []

with open('books.csv', 'r') as file:
    N = file.readline() 
    table = csv.reader(file, delimiter=';')
    for row in table:
        cb += 1

        if len(row[1]) > 30:
         cb_over30 += 1
         
        author = row[3]
        author_sn = row[4]
        if author == search or author_sn == search:
            if int(row[7]) < 200:
             print(row[1])

        for i in range(len(popular_downloads)):  
            if int(row[8]) > int(popular_downloads[i]):
               popular_downloads[i] = row[8]
               popular[i] = str(i + 1) + '. ID - ' + str(row[0]) + '; Название - ' + str(row[1]) + '; Автор - ' + str(
                            row[4]) + '; Дата поступления - ' + str(row[6]) + '; Жанр - ' + str(row[12]) \
                                 + '; Выдано - ' + str(row[8]) + '; Цена - ' + str(row[7])
               break

        tgs_all = (row[12].rsplit("#"))[1:]  
        random_books.append('автор - ' + row[4] + '; название - ' + row[1] + '; год поступления - ' + row[6])

        for i in range(len(tgs_all)):  
            if (tgs_all[i][0]) == ' ':
                tgs_all[i] = tgs_all[i][1:]  
            if tgs_all[i] not in tegs:
                tegs.append(tgs_all[i])

book_random = list(x for x in random.sample(random_books, 20))

with open('results.txt', 'w') as f:
    for i in range(1, 21):
        f.write(str(i) + '.' + ' ' + book_random[i - 1] + '\n')

f.close()

print('Жанры:')
for i in range(len(tegs)):
    print(tegs[i])
print ('20 самых популярных книг:')
for i in range(0, 20):
    print(popular[i])

print('Количество книг в таблице = ' + str(cb) + '\n'  + str(cb_over30) + '\n')
