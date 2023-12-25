import tkinter as tk
from tkinter import ttk

import numpy as np

app = tk.Tk()
app.title('CarotidTricoder')
app.geometry('300x600')
app.resizable(width=False, height=False)

# -----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------App Interface
# ---------------------------------------------------------Patient Section
# ----------Title
labelTitle = tk.Label(text='Пациент:', fg='#eee', bg='#333')
labelTitle.place(relwidth=1.0, relx=.5, rely=.02, anchor='c')

patientName = tk.StringVar()
patientNameLabel = tk.Label(text='ФИО:')
patientNameLabel.place(x=8, y=45, anchor='w')
patientName_entry = tk.Entry(textvariable=patientName)
patientName_entry.place(x=45, y=45, relwidth=.8, anchor='w')

patientDate = tk.StringVar()
patientDateLabel = tk.Label(text='Дата рождения:')
patientDateLabel.place(x=8, y=68, anchor='w')
patientDate_entry = tk.Entry(textvariable=patientDate)
patientDate_entry.place(x=101, y=68, relwidth=.612, anchor='w')

patientSexLabel = tk.Label(text='Пол:')
patientSexLabel.place(x=68, y=92, anchor='w')
patientSelectSex = ttk.Combobox(app, values=['мужской',
                                             'женский'])
patientSelectSex.place(x=101, y=92, relwidth=.25, anchor='w')

# ---------------------------------------------------------Parameters Section
# ----------Title
labelTitle = tk.Label(text='Анамнез:', fg='#eee', bg='#333')
labelTitle.place(relwidth=1.0, relx=.5, rely=.206, anchor='c')

# ----------Blood Select
bloodLabel = tk.Label(text='1. Количество эритроцитов')
bloodLabel.place(x=7, y=150, anchor='w')
bloodSelect = ttk.Combobox(app, values=['< 10^9/л',
                                        '10^9/л-3*10^12/л', '> 3*10^12/л'])
bloodSelect.place(x=11, y=177, relwidth=.40, anchor='w')

# ----------Pleositos Select
pleositosLabel = tk.Label(text='2. Плеоцитоз:')
pleositosLabel.place(x=162, y=150, anchor='w')
pleositosSelect = ttk.Combobox(app, values=['0.01-0.06*10^9/л',
                                           '0.01-0.2*10^9/л',
                                           '0.1-0.3*10^9/л',
                                           '1.0-2.0*10^9/л',
                                           '2.0-5.0*10^9/л'])
pleositosSelect.place(x=165, y=177, relwidth=.40, anchor='w')

# ----------Protein Select
proteinLabel = tk.Label(text='3. Концентрация белка:')
proteinLabel.place(x=8, y=227, anchor='w')
proteinSelect = ttk.Combobox(app, values=['0.16-2.88 г/л',
                                          '0.19-21.0 г/л',
                                          '0.21-22.0 г/л'])
proteinSelect.place(x=11, y=254, relwidth=.40, anchor='w')

# ----------Hearth Select
glucoseLabel = tk.Label(text='4. Уровень глюкозы:')
glucoseLabel.place(x=162, y=227, anchor='w')
glucoseSelect = ttk.Combobox(app, values=['4.7±1.9 ммоль/л',
                                         '2.94±0.44 ммоль/л',
                                         '1.38±0.58 ммоль/л'])
glucoseSelect.place(x=165, y=254, relwidth=.40, anchor='w')

# ---------------------------------------------------------Conclusion Section
# ----------Title
labelTitle = tk.Label(text='Заключение:', fg='#eee', bg='#333')
labelTitle.place(relwidth=1.0, relx=.5, rely=.68, anchor='c')


# --------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------App Engine
def clearPatientValues():
    patientName_entry.delete(0, tk.END)
    patientDate_entry.delete(0, tk.END)
    patientSelectSex.set('')


def appAnalyse():
    bloodVar = bloodSelect.get()
    pleositosVar = pleositosSelect.get()
    proteinVar = proteinSelect.get()
    glucoseVar = glucoseSelect.get()

    if bloodVar == '< 10^9/л': #Ишемический инсульт
        bloodVar = int('1')
    elif bloodVar == '10^9/л-3*10^12/л':#геморрагический инсульт
        bloodVar = int('100')
    elif bloodVar == '> 3*10^12/л':#
        bloodVar = int('0')
    elif bloodVar == (''):
        bloodVar = str('')

    if pleositosVar == '0.01-0.06*10^9/л':#опухоли ЦНС
        pleositosVar = int('0')
    elif pleositosVar == '0.01-0.2*10^9/л':#ишемический инсульт
        pleositosVar = int("1")
    elif pleositosVar == '0.1-0.3*10^9/л':#серозный менингит
        pleositosVar = int('1000')
    elif pleositosVar == '1.0-2.0*10^9/л':#абсцесс мозга
        pleositosVar = int('10')
    elif pleositosVar == '2.0-5.0*10^9/л':#гнойный минигит
        pleositosVar = int('10000')
    elif pleositosVar == (''):
        pleositosVar = str('')

    if proteinVar == '0.16-2.88 г/л':#абсцесс мозга
        proteinVar = int('10')
    elif proteinVar == '0.19-21.0 г/л':#гемморагический инсульт
        proteinVar = int('100')
    elif proteinVar == '0.21-22.0 г/л':#гнойный минингит
        proteinVar = int('10000')
    elif proteinVar == (''):
        proteinVar = str('')

    if glucoseVar == '4.7±1.9 ммоль/л':#ишемический инсульт
        glucoseVar = int('1')
    elif glucoseVar == '2.94±0.44 ммоль/л':#серозный минингит
        glucoseVar = int('1000')
    elif glucoseVar == '1.38±0.58 ммоль/л':#гнойный минингит
        glucoseVar = int('10000')
    elif glucoseVar == (''):
        glucoseVar = str('')

    print(bloodVar, pleositosVar, proteinVar, glucoseVar)
    a = [bloodVar, pleositosVar, proteinVar, glucoseVar]
    SCORE = np.argmax((np.bincount(a)))
    print(SCORE)

    if SCORE == (''):
        conclusion.config(text=f'Выберите значения!')
    elif SCORE >= 0 and SCORE < 5:
        conclusion.config(
            text=f'Ишемический инсульт.\nОперативное лечение показано.\n\nРекомендовано:\nПостельный режим, диета, регулярный осмотр врачей\n')
    elif SCORE >= 170 and SCORE < 230:
        conclusion.config(
            text=f'Геморрагический инсульт.\nОперативное лечение показано.\n\nРекомендовано:\nПостельный режим, диета, регулярный осмотр врачей\n')
    elif SCORE >= 1750 and SCORE < 2250:
        conclusion.config(
            text=f'Серозный минингит.\nОперативное лечение показано.\n\nРекомендовано:\nПостельный режим, диета, регулярный осмотр врачей\n')
    elif SCORE >= 15 and SCORE <= 25:
        conclusion.config(
            text=f'Абсцесс мозга.\n\nРекомендовано:\nКонсультация нейроохирурга для решения\nвопроса о плановом оперативном лечении,\nчерез 1 месяц.\n')
    elif SCORE >= 27500 and SCORE < 32500:
        conclusion.config(
            text=f'Гнойный минигит.\n\nРекомендовано:\nПостельный режим, диета, регулярный осмотр врачей\n')


conclusion = ('')
conclusion = tk.Label(text=conclusion, anchor='c', height=10, width=41)
conclusion.place(relx=.012, rely=.835, anchor='w')




def clearComboboxValues():
    bloodSelect.set('')
    pleositosSelect.set('')
    proteinSelect.set('')
    glucoseSelect.set('')
    conclusion.config(text=f'')

def ResultsSaving():
    Row = [1, 1, 1, 1]
    with open('document.csv', 'a') as fd:
        fd.write(Row)

# ----------Buttons
message_button = tk.Button(text='X', command=clearPatientValues)
message_button.place(x=261, y=92, relheight=.035, relwidth=.08, anchor="w")

message_button = tk.Button(text='Анализ', command=appAnalyse)
message_button.place(x=165, y=370, relwidth=.40, anchor='w')

message_button = tk.Button(text='Сброс', command=clearComboboxValues)
message_button.place(x=11, y=370, relwidth=.40, anchor='w')

message_button = tk.Button(text='Сохранить', command=ResultsSaving)
message_button.place(x=165, y=565, relwidth=.40, anchor='w')

app.mainloop()
