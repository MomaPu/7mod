import requests # импортируем для удачного входа на страницу
from bs4 import BeautifulSoup # парсер
import matplotlib.pyplot as plt # для создания таблицы

url = "https://cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=R01235&UniDbQuery.From=25.12.2023&UniDbQuery.To=24.01.2024"
req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 '
'Firefox/50.0'})

soup = BeautifulSoup(req.content, 'html.parser')  # берем инфу
dollars = soup.find_all('td') # записываем

course_and_time = [dollar.text for dollar in dollars] # получаем нужное
course_and_time.pop(0) # убираем лишнее
clear_course = [] # создаем для графика 2 таблицы с значениями из курса
date = []

for i in range(2,len(course_and_time),3): # получаем чистые значения
	clear_course.append(course_and_time[i])

for d in range(0,len(course_and_time),3):
	date.append(course_and_time[d])

plt.plot(date,clear_kurs,'ro') # создаем график
plt.title('Курс доллара')
plt.show()	