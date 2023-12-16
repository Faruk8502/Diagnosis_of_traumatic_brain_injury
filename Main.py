import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title('CarotidTricoder')
app.geometry('300x600')
app.resizable(width=False, height=False)

#-----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------App Interface
#---------------------------------------------------------Patient Section
#----------Title
labelTitle = tk.Label(text = 'Пациент:', fg = '#eee', bg = '#333')
labelTitle.place(relwidth = 1.0, relx = .5, rely = .02, anchor = 'c')

patientName = tk.StringVar()
patientNameLabel = tk.Label(text = 'ФИО:')
patientNameLabel.place(x = 8, y = 45, anchor = 'w')
patientName_entry = tk.Entry(textvariable = patientName)
patientName_entry.place(x = 45, y = 45, relwidth = .8, anchor = 'w')

patientDate = tk.StringVar()
patientDateLabel = tk.Label(text = 'Дата рождения:')
patientDateLabel.place(x = 8, y = 68, anchor = 'w')
patientDate_entry = tk.Entry(textvariable = patientDate)
patientDate_entry.place(x = 101, y = 68, relwidth = .612, anchor = 'w')

patientSexLabel = tk.Label(text = 'Пол:')
patientSexLabel.place(x = 68, y = 92, anchor = 'w')
patientSelectSex = ttk.Combobox(app, values = ['мужской',
                                               'женский'])
patientSelectSex.place(x = 101, y = 92, relwidth = .25, anchor = 'w')

#---------------------------------------------------------Parameters Section
#----------Title
labelTitle = tk.Label(text = 'Анамнез:', fg = '#eee', bg = '#333')
labelTitle.place(relwidth = 1.0, relx = .5, rely = .206, anchor = 'c')

#----------Course Select
courseLabel = tk.Label(text = '1. Течение:')
courseLabel.place(x = 7, y = 150, anchor = 'w')
courseSelect = ttk.Combobox(app, values = ['бессимптомное',
                                           'симптомное'])
courseSelect.place(x = 11, y = 177, relwidth = .40, anchor = 'w')

#----------Stenosis Select
stenosisLabel = tk.Label(text = '2. Стеноз ВСА:')
stenosisLabel.place(x = 162, y = 150, anchor = 'w')
stenosisSelect = ttk.Combobox(app, values = ['нет',
                                             'менее 50%',
                                             'от 50 до 70%',
                                             'более 70%',
                                             'окклюзия'])
stenosisSelect.place(x = 165, y = 177, relwidth = .40, anchor = 'w')

#----------Plaque Select
plaqueLabel = tk.Label(text = '3. Бляшка:')
plaqueLabel.place(x = 8, y = 227, anchor = 'w')
plaqueSelect = ttk.Combobox(app, values = ['нет',
                                           'стабильная',
                                           'нестабильная'])
plaqueSelect.place(x = 11, y = 254, relwidth = .40, anchor = 'w')

#----------Hearth Select
hearthLabel = tk.Label(text = '4. Очаг ишемии:')
hearthLabel.place(x = 162, y = 227, anchor = 'w')
hearthSelect = ttk.Combobox(app, values = ['нет',
                                           'менее 2,5 см',
                                           '2,5 см',
                                           'более 2,5 см'])
hearthSelect.place(x = 165, y = 254, relwidth = .40, anchor = 'w')

#----------Transformation Select
transformationLabel = '5. Геморрагическая \n трансформация:'
transformationLabel = tk.Label(text = transformationLabel, justify = tk.LEFT)
transformationLabel.place(x = 7, y = 300, anchor = 'w')
transformationSelect = ttk.Combobox(app, values = ['нет',
                                                   'есть'])
transformationSelect.place(x = 11, y = 331, relwidth = .40, anchor = 'w')

#----------Deficit Select
deficitLabel = '6. Неврологический \n дефицит:'
deficitLabel = tk.Label(text = deficitLabel, justify = tk.LEFT)
deficitLabel.place(x = 162, y = 300, anchor = 'w')
deficitSelect = ttk.Combobox(app, values = ['нет',
                                            'Ренкин 1-3',
                                            'Ренкин 4-5'])
deficitSelect.place(x = 165, y = 331, relwidth = .40, anchor = 'w')

#---------------------------------------------------------Conclusion Section
#----------Title
labelTitle = tk.Label(text = 'Заключение:', fg = '#eee', bg = '#333')
labelTitle.place(relwidth = 1.0, relx = .5, rely = .68, anchor = 'c')

#--------------------------------------------------------------------------------------
#----------------------------------------------------------------------------App Engine
def clearPatientValues ():
    patientName_entry.delete(0, tk.END)
    patientDate_entry.delete(0, tk.END)
    patientSelectSex.set('')
    
def appAnalyse ():
    courseVar = courseSelect.get()
    stenosisVar = stenosisSelect.get()
    plaqueVar = plaqueSelect.get()
    hearthVar = hearthSelect.get()
    transformationVar = transformationSelect.get()
    deficitVar = deficitSelect.get()

    if courseVar == 'бессимптомное':
       courseVar = int('1')
    elif courseVar == 'симптомное':
       courseVar = int('3')
    elif courseVar == (''):
       courseVar = str('')

    if stenosisVar == 'нет':
       stenosisVar = int('0')
    elif stenosisVar == 'менее 50%':
       stenosisVar = int("2")
    elif stenosisVar == 'от 50 до 70%':
       stenosisVar = int('5')
    elif stenosisVar == 'более 70%':
       stenosisVar = int('8')
    elif stenosisVar == 'окклюзия':
       stenosisVar = int('25')
    elif stenosisVar == (''):
       stenosisVar = str('')

    if plaqueVar == 'нет':
       plaqueVar = int('0')
    elif plaqueVar == 'стабильная':
       plaqueVar = int('2')
    elif plaqueVar == 'нестабильная':
       plaqueVar = int('5')
    elif plaqueVar == (''):
       plaqueVar = str('')

    if hearthVar == 'нет':
       hearthVar = int('0')
    elif hearthVar == 'менее 2,5 см':
       hearthVar = int('1')
    elif hearthVar == '2,5 см':
       hearthVar = int('2')
    elif hearthVar == 'более 2,5 см':
       hearthVar = int('15')
    elif hearthVar == (''):
       hearthVar = str('')

    if transformationVar == 'нет':
       transformationVar = int('0')
    elif transformationVar == 'есть':
       transformationVar = int('15')
    elif transformationVar == (''):
       transformationVar = str('')

    if deficitVar == 'нет':
       deficitVar = int('0')
    elif deficitVar == 'Ренкин 1-3':
       deficitVar = int('2')
    elif deficitVar == 'Ренкин 4-5':
       deficitVar = int('15')
    elif deficitVar == (''):
       deficitVar = str('')

    print(courseVar, stenosisVar, plaqueVar, hearthVar, transformationVar, deficitVar)

    SCORE = courseVar + stenosisVar + plaqueVar + hearthVar + transformationVar + deficitVar
    print(SCORE)

    if SCORE == (''):
       conclusion.config(text = f'Выберите значения!')
    elif SCORE >= 0 and SCORE < 7:
       conclusion.config(text = f'Риск ОНМК низкий.\nОперативное лечение не показано.\n\nРекомендовано:\nОсмотр ангиохирурга с контрольным УЗАС\nсонных артерий 1 раз в год.\n')
    elif SCORE >= 7 and SCORE < 10:
       conclusion.config(text = f'Риск ОНМК незначительный.\nОперативное лечение не показано.\n\nРекомендовано:\nОсмотр ангиохирурга с контрольным УЗАС\nсонных артерий 2 раза в год.\n')
    elif SCORE >= 10 and SCORE < 15:
       conclusion.config(text = f'Риск ОНМК высокий.\nОперативное лечение показано.\n\nРекомендовано:\nКонсультация ангиохирурга для решения\nвопроса о плановом оперативном лечении.\n')
    elif SCORE >= 15 and SCORE <= 27:
       conclusion.config(text = f'Оперативное лечение не показано.\n\nРекомендовано:\nКонсультация ангиохирурга для решения\nвопроса о плановом оперативном лечении,\nчерез 1 месяц.\n')
    elif SCORE >= 28:
       conclusion.config(text = f'Оперативное лечение не показано.\n\nРекомендовано:\nОсмотр ангиохирурга с контрольным УЗАС\nсонных артерий 2 раза в год.\n')
       
conclusion = ('')
conclusion = tk.Label(text = conclusion, anchor = 'c', height = 10, width = 41)
conclusion.place(relx = .012, rely = .835, anchor = 'w')
        
def clearComboboxValues ():
    courseSelect.set('')
    stenosisSelect.set('')
    plaqueSelect.set('')
    hearthSelect.set('')
    transformationSelect.set('')
    deficitSelect.set('')
    conclusion.config(text = f'')

#----------Buttons
message_button = tk.Button(text = 'X', command = clearPatientValues)
message_button.place(x = 261, y = 92, relheight = .035, relwidth = .08, anchor = "w")
    
message_button = tk.Button(text = 'Анализ', command = appAnalyse)
message_button.place(x = 165, y = 370, relwidth = .40, anchor = 'w')

message_button = tk.Button(text = 'Сброс', command = clearComboboxValues)
message_button.place(x = 11, y = 370, relwidth = .40, anchor = 'w')
    
app.mainloop()
