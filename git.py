import schedule
import time
import csv

def write_csv():
    name = input('Enter your name: ')
    age = input('Enter your age: ')
    with open('users.csv', 'a') as f:
        writer = csv.writer(f, delimiter = '/')
        writer.writerow(
            (name, age)
        )

    answer = input('Continue? yes or no: ')
    if answer == 'yes':
        write_csv()
    else:
        print('Stop!')

write_csv()


def mailing():
    with open('users.csv', 'r') as f:
        data = f.readlines()
        names = [i.replace('\n', '') for i in data]
        for i in names:
            name = i.split('/')
            if int(name[-1]) >= 18:
                print(f'Hello, {name[0]}. We have great discounts on alcohol today!')

schedule.every(3).seconds.do(mailing)

while True:
    schedule.run_pending()
    time.sleep(1)

# github - сервер, предоставляющий универсальное хранилище для кода
# git - система контроля версии
# удаленный репозиторий - папка гитхаба