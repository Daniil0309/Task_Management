import tkinter as tk  # Импорт модуля tkinter и его псевдонима tk

def add_task():  # Объявление функции для добавления задачи
    task = task_entry.get()  # Получение текста из поля ввода
    if task:  # Проверка, есть ли текст в переменной task
        task_listBox.insert(tk.END, task)  # Добавление задачи в список задач
        task_entry.delete(0, tk.END)  # Очистка поля ввода после добавления задачи

def delete_task():  # Объявление функции для удаления задачи
    selected_task = task_listBox.curselection()  # Получение индекса выбранной задачи в списке
    if selected_task:  # Проверка, выбрана ли какая-то задача
        task_listBox.delete(selected_task)  # Удаление выбранной задачи из списка

def mark_task():  # Объявление функции для отметки выполненной задачи
    selected_task = task_listBox.curselection()  # Получение индекса выбранной задачи в списке
    if selected_task:  # Проверка, выбрана ли какая-то задача
        task_listBox.itemconfig(selected_task, bg="lightblue")  # Изменение цвета фона выбранной задачи на голубой

def clear_task(): # Объявление функции для очистки всего списка задач
    task_listBox.delete(0, tk.END)  # Очистка списка задач

root = tk.Tk()  # Создание главного окна
root.title("Task list")  # Установка заголовка окна
root.config(background="lightgray")  # Установка цвета фона для главного окна

text1 = tk.Label(root, text="Введите вашу задачу", bg="lightgray")  # Создание метки для ввода задачи
text1.pack(pady=5)  # Размещение метки в главном окне с небольшим отступом

task_entry = tk.Entry(root, width=30, bg="white", fg="black")  # Создание поля ввода для задачи
task_entry.pack(pady=10)  # Размещение поля ввода в главном окне с отступом

add_task_buton = tk.Button(root, text="Добавить задачу", command=add_task, bg="lightblue")  # Создание кнопки для добавления задачи
add_task_buton.pack(pady=5)  # Размещение кнопки в главном окне с небольшим отступом

delete_buton = tk.Button(root, text="Удалить задачу", command=delete_task, bg="lightcoral")  # Создание кнопки для удаления задачи
delete_buton.pack(pady=5)  # Размещение кнопки в главном окне с небольшим отступом

mark_buton = tk.Button(root, text="Отметить выполненую задачу", command=mark_task, bg="lightgreen")  # Создание кнопки для отметки выполненной задачи
mark_buton.pack(pady=5)  # Размещение кнопки в главном окне с небольшим отступом

clear_buton = tk.Button(root, text="Очистить список", command=clear_task) # Создание кнопки для очистки списка задач
clear_buton.pack(pady=5)    #Размещение кнопки в главном окне с небольшим отступом

text2 = tk.Label(root, text="Список задач", bg="lightgray")  # Создание метки для списка задач
text2.pack(pady=5)  # Размещение метки в главном окне с небольшим отступом

task_listBox = tk.Listbox(root, height=10, width=50, bg="white")  # Создание списка для задач
task_listBox.pack(pady=5)  # Размещение списка в главном окне с небольшим отступом

root.mainloop()  # Запуск главного цикла приложения



