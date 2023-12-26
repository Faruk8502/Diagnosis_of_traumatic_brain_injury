from tkinter import *
from tkinter import ttk
import numpy as np
import csv

def save_patient_data():
    # Получить значения из полей ввода пациента
    field1_val = field1.get()
    field2_val = field2.get()
    field3_val = field3.get()
    field4_val = field4.get()

    # Сохранить данные в файле csv
    with open('patient_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([field1_val, field2_val, field3_val, field4_val])

    print("Данные пациента успешно сохранены.")

def goto_diagnosis_window():
    top.destroy()
    diagnosis_window()

def goto_main():
    diagnosis_top.destroy()
    main()

def diagnosis_window():
    global diagnosis_top
    def save_diagnosis_data():
        # Получить значения из полей ввода результатов исследования
        result1_val = result1.get()
        result2_val = result2.get()
        result3_val = result3.get()
        result4_val = result4.get()

        # Сохранить данные в файле csv
        with open('diagnosis_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([result1_val, result2_val, result3_val, result4_val])

        print("Результаты диагностики успешно сохранены.")

    def show_help_window():
        help_window()


    def help_window():
        def close_help_window():
            help_top.destroy()

        help_top = Toplevel()
        help_top.title('Справка')

        help_text = Text(help_top, width=50, height=10)
        help_text.insert(END, 'Текст справки...')
        help_text.pack()

        close_button = Button(help_top, text='Закрыть', command=close_help_window)
        close_button.pack()

    def appAnalyse():
        bloodVar = result1.get()
        pleositosVar = result2.get()
        proteinVar = result3.get()
        glucoseVar = result4.get()

        if bloodVar == '< 10^9/л':  # Ишемический инсульт
            bloodVar = int('1')
        elif bloodVar == '10^9/л-3*10^12/л':  # геморрагический инсульт
            bloodVar = int('100')
        elif bloodVar == '> 3*10^12/л':  #
            bloodVar = int('0')
        elif bloodVar == (''):
            bloodVar = str('')

        if pleositosVar == '0.01-0.06*10^9/л':  # опухоли ЦНС
            pleositosVar = int('0')
        elif pleositosVar == '0.01-0.2*10^9/л':  # ишемический инсульт
            pleositosVar = int("1")
        elif pleositosVar == '0.1-0.3*10^9/л':  # серозный менингит
            pleositosVar = int('1000')
        elif pleositosVar == '1.0-2.0*10^9/л':  # абсцесс мозга
            pleositosVar = int('10')
        elif pleositosVar == '2.0-5.0*10^9/л':  # гнойный минигит
            pleositosVar = int('10000')
        elif pleositosVar == (''):
            pleositosVar = str('')

        if proteinVar == '0.16-2.88 г/л':  # абсцесс мозга
            proteinVar = int('10')
        elif proteinVar == '0.19-21.0 г/л':  # гемморагический инсульт
            proteinVar = int('100')
        elif proteinVar == '0.21-22.0 г/л':  # гнойный минингит
            proteinVar = int('10000')
        elif proteinVar == (''):
            proteinVar = str('')

        if glucoseVar == '4.7±1.9 ммоль/л':  # ишемический инсульт
            glucoseVar = int('1')
        elif glucoseVar == '2.94±0.44 ммоль/л':  # серозный минингит
            glucoseVar = int('1000')
        elif glucoseVar == '1.38±0.58 ммоль/л':  # гнойный минингит
            glucoseVar = int('10000')
        elif glucoseVar == (''):
            glucoseVar = str('')

        print(bloodVar, pleositosVar, proteinVar, glucoseVar)
        a = [bloodVar, pleositosVar, proteinVar, glucoseVar]
        SCORE = np.argmax((np.bincount(a)))
        print(SCORE)

        if SCORE == (''):
            diagnosis_label.config(text=f'Выберите значения!')
        elif SCORE >= 0 and SCORE < 5:
            diagnosis_label.config(
                text=f'Ишемический инсульт.\nОперативное лечение показано.\n\nРекомендовано:\nПостельный режим, диета,\n регулярный осмотр врачей\n')
        elif SCORE >= 170 and SCORE < 230:
            diagnosis_label.config(
                text=f'Геморрагический инсульт.\nОперативное лечение показано.\n\nРекомендовано:\nПостельный режим,\n диета, регулярный осмотр врачей\n')
        elif SCORE >= 1750 and SCORE < 2250:
            diagnosis_label.config(
                text=f'Серозный минингит.\nОперативное лечение показано.\n\nРекомендовано:\nПостельный режим, диета,\n регулярный осмотр врачей\n')
        elif SCORE >= 15 and SCORE <= 25:
            diagnosis_label.config(
                text=f'Абсцесс мозга.\n\nРекомендовано:\nКонсультация нейроохирурга для решения\nвопроса о плановом оперативном лечении,\nчерез 1 месяц.\n')
        elif SCORE >= 27500 and SCORE < 32500:
            diagnosis_label.config(
                text=f'Гнойный минигит.\n\nРекомендовано:\nПостельный режим, диета,\n регулярный осмотр врачей\n')

    diagnosis_top = Tk()
    diagnosis_top.geometry('300x600')
    diagnosis_top.resizable(width=False, height=False)
    diagnosis_top.title('Автоматическая диагностика')
    a = 20

    patient_label = Label(diagnosis_top, text=field1.get()+field2.get()+field3.get())
    patient_label.place(x=90, y=a, relwidth=.8, anchor='w')
    result_label1 = Label(diagnosis_top, text='К-во эритроцитов:')
    result_label1.place(x=10, y=45+a, relwidth=.4, anchor='w')
    result1 = ttk.Combobox(diagnosis_top, values=['< 10^9/л',
                                                  '10^9/л-3*10^12/л',
                                                  '> 3*10^12/л'])
    result1.place(x=135, y=45+a, relwidth=.4, anchor='w')

    result_label2 = Label(diagnosis_top, text='Плеоцитоз:')
    result_label2.place(x=10, y=90+a, relwidth=.4, anchor='w')
    result2 = ttk.Combobox(diagnosis_top, values=['0.01-0.06*10^9/л',
                                                  '0.01-0.2*10^9/л',
                                                  '0.1-0.3*10^9/л',
                                                  '1.0-2.0*10^9/л',
                                                  '2.0-5.0*10^9/л'])
    result2.place(x=135, y=90+a, relwidth=.4, anchor='w')

    result_label3 = Label(diagnosis_top, text='К-ция белка:')
    result_label3.place(x=10, y=135+a, relwidth=.4, anchor='w')
    result3 = ttk.Combobox(diagnosis_top, values=['0.16-2.88 г/л',
                                                  '0.19-21.0 г/л',
                                                  '0.21-22.0 г/л'])
    result3.place(x=135, y=135+a, relwidth=.4, anchor='w')

    result_label4 = Label(diagnosis_top, text='У-нь глюкозы:')
    result_label4.place(x=10, y=180+a, relwidth=.4, anchor='w')
    result4 = ttk.Combobox(diagnosis_top, values=['4.7±1.9 ммоль/л',
                                                  '2.94±0.44 ммоль/л',
                                                  '1.38±0.58 ммоль/л'])
    result4.place(x=135, y=180+a, relwidth=.4, anchor='w')

    save_button = Button(diagnosis_top, text='Сохранить', command=save_diagnosis_data)
    save_button.place(x=45, y=225+a, relwidth=.8, anchor='w')

    help_button = Button(diagnosis_top, text='Справка', command=show_help_window)
    help_button.place(x=45, y=315+a, relwidth=.8, anchor='w')

    help_button = Button(diagnosis_top, text='Назад', command=goto_main)
    help_button.place(x=45, y=550+a, relwidth=.8, anchor='w')

    diagnosis_label = Label(diagnosis_top, text='Введите данные для получения диагноза', height=10, width=20)
    diagnosis_label.place(x=150, y=415+a, relwidth=1, anchor='c')

    diagnosis_button = Button(diagnosis_top, text='Провести диагностику', command=appAnalyse)
    diagnosis_button.place(x=45, y=270+a, relwidth=.8, anchor='w')

def main():
    global top, field1, field2, field3, field4

    top = Tk()
    top.geometry('300x600')
    top.resizable(width=False, height=False)
    top.title('Ввод данных пациента')

    field1_label = Label(top, text='Фамилия:')
    field1_label.place(x=10, y=45, relwidth=.4, anchor='w')
    field1 = Entry(top)
    field1.place(x=135, y=45, relwidth=.4, anchor='w')

    field2_label = Label(top, text='Имя:')
    field2_label.place(x=10, y=90, relwidth=.4, anchor='w')
    field2 = Entry(top)
    field2.place(x=135, y=90, relwidth=.4, anchor='w')

    field3_label = Label(top, text='Отчество:')
    field3_label.place(x=10, y=135, relwidth=.4, anchor='w')
    field3 = Entry(top)
    field3.place(x=135, y=135, relwidth=.4, anchor='w')

    field4_label = Label(top, text='Дата рождения:')
    field4_label.place(x=10, y=180, relwidth=.4, anchor='w')
    field4 = Entry(top)
    field4.place(x=135, y=180, relwidth=.4, anchor='w')

    save_button = Button(top, text='Сохранить', command=save_patient_data)
    save_button.place(x=45, y=225, relwidth=.8, anchor='w')

    next_button = Button(top, text='Дальше', command=goto_diagnosis_window)

    next_button.place(x=45, y=270, relwidth=.8, anchor='w')

    top.mainloop()


if __name__ == "__main__":
    main()

