import json
 import datetime

 #читаем заметки с открытием файла 
 def read_notebook():
     try:
         with open('notes.json', 'r') as f:
             notes = json.load(f)
     except FileNotFoundError:
         notes = []
     return notes

 #запись и сохранение данных в записную книжку
 def save_notebook(notes):
     with open('notes.json', 'w') as f:
         json.dump(notes, f, indent=4)

 #создание заметки в записной книжке
 def create_note():
     title = input('Введите заголовок заметки: ')
     body = input('Введите текст заметки: ')
     created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
     note = {
         'id': len(read_notebook()) + 1,
         'title': title,
         'body': body,
         'created_at': created_at,
         'updated_at': created_at
     }
     return note

 #добавление созданной заметки в записную книжку
 def add_note():
     notes = read_notebook()
     note = create_note()
     notes.append(note)
     save_notebook(notes)
     print('Заметка добавлена')

 #изменение заметки в записной книжке
 def edit_note():
     notes = read_notebook()
     note_id = int(input('Введите id заметки, которую хотите изменить: '))
     for note in notes:
         if note['id'] == note_id:
             title = input(f'Текущий заголовок: {note["title"]}. Введите новый заголовок или нажмите Enter, чтобы оставить прежний: ')
             if title:
                 note['title'] = title
             body = input(f'Текст заметки:\n{note["body"]}\nВведите новый текст или нажмите Enter, чтобы оставить прежний: ')
             if body:
                 note['body'] = body
             note['updated_at'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
             save_notebook(notes)
             print('Заметка изменена')
             break
     else:
         print('Заметка с таким id не найдена')

 #удаление заметки из записной книжки
 def delete_note():
     notes = read_notebook()
     note_id = int(input('Введите id заметки, которую хотите удалить: '))
     for note in notes:
         if note['id'] == note_id:
             notes.remove(note)
             save_notebook(notes)
             print('Заметка удалена')
             break
     else:
         print('Заметка с таким id не найдена')

 #просмотр всех заметок в записной книжке
 def list_notes():
     notes = read_notebook()
     if not notes:
         print('Заметок нет')
     else:
         for note in notes:
             print(f'id: {note["id"]}, заголовок: {note["title"]}, дата создания: {note["created_at"]}, дата изменения: {note["updated_at"]}')

 #просмотр нужной заметки в записной книжке
 def view_note():
     notes = read_notebook()
     note_id = int(input('Введите id заметки, которую хотите просмотреть: '))
     for note in notes:
         if note['id'] == note_id:
             print(f'Заголовок: {note["title"]}\nТекст заметки:\n{note["body"]}\nДата создания: {note["created_at"]}\nДата изменения: {note["updated_at"]}')
             break
     else:
         print('Заметка с таким id не найдена')