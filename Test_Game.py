import os
import argparse
import subprocess
from time import sleep
from pywinauto.application import Application
import pyautogui as pag
import keyboard as key

def autobench():

    parser = argparse.ArgumentParser()#парсим аргументы из командной строки при вызове файла
    parser.add_argument('name')
    parser.add_argument('-o')
    args = parser.parse_args()
    maindir = args.name#Путь до игры
    dir = args.o#Путь до места назначения статистики

    Application().start(maindir+"pno0001.exe")#Запуск игры

    sleep(10)#Ждем загрузку
    start = pag.screenshot('startscreenshot.png')#Скриншот экрана после загрузки. Опционально выбор необходимой директории для сохранения

    key.press('o')#Запуск бенчмарка(Горячая клавиша в MSI Afterburner)

    pag.keyDown('SPACE')#Пропуск начальной катсцены. Нажимам 'SPACE'
    pag.keyUp('SPACE')#Отпускаем 'SPACE'

    pag.keyDown('ENTER')#Начало новой игры.
    pag.keyUp('ENTER')

    sleep(1)
    pag.keyDown('W')#Движение вперед
    sleep(5)#Пять секунд не отпускаем клавишу 'W'
    pag.keyUp('W')

    key.press('p')#Остановка бенчмарка(Горячая клавиша в MSI Afterburner)

    end = pag.screenshot('endscreenshot.png')#Скриншот экрана перед выходом

    subprocess.call(["taskkill","/F","/IM","pno0001.exe"])#Убиваем процесс pno0001.exe(игра). Правильнее, но дольше будет выйти через 'ESC' нажатиями клавиш

    with open('D:\Benchmark.txt','r') as result:#Открываем отчет по бенчмарку(сохраняется в выбранную папку настройкой в MSI Afterburner)
        lines = result.readlines()#Читаем построчно файл
    

    path = os.path.join(dir, 'start.png')#Путь к первому скрину
    path2 = os.path.join(dir, 'end.png')#Путь ко второму скрину
    start.save(path)#Сохраняем первый скрин
    end.save(path2)#Сохраняем второй скрин

    with open(dir+'ResultBenchmark.txt','w') as file:#Создаем файл по указанной ранее директории
        for line in lines:
             file.write(line + '\n')#Построчно записываем результаты бенчмарка в указанный файл

    file2 = open(dir+'AverageFPS.txt','w')#Создаем и записываем файл со средним FPS по указанной ранее директории
    file2.write(lines[1]) #Записываем результаты среднего FPS в указанный файл
    file2.close()

if __name__ == "__main__":
    autobench()
