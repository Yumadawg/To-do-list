from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox, QListWidget
)
from PyQt6.QtGui import QFont
import functions


app = QApplication([])

window = QWidget()
window.setWindowTitle("My To-Do list")
window.resize(400, 50)

layout = QVBoxLayout()
layout.setContentsMargins(10, 10, 10, 10)
layout.setSpacing(5)
font = QFont("Segoe UI", 13)

label = QLabel("Write a To-do")
label.setFont(font)
layout.addWidget(label)

input_field = QLineEdit()
input_field.setFont(font)

button = QPushButton("Add")
button.setFont(font)

input_layout = QHBoxLayout()
input_layout.addWidget(input_field)
input_layout.addWidget(button)

layout.addLayout(input_layout)

todo_list = QListWidget()
todo_list.setFont(font)
layout.addWidget(todo_list)

delete_button = QPushButton("Delete selected")
delete_button.setFont(font)
delete_button.setFixedWidth(150)
layout.addWidget(delete_button)

edit_button = QPushButton("Edit selected")
edit_button.setFont(font)
edit_button.setFixedWidth(150)
layout.addWidget(edit_button)

def refresh_list():
    todo_list.clear()
    todos = functions.get_todos()
    for item in todos:
        todo_list.addItem(item.strip())


def add_button_click():
    text = input_field.text()
    if not text.strip():
        QMessageBox.warning(window, "Empty input", "Please write something before adding.")
        return
    todos = functions.get_todos()
    todos.append(text + "\n")
    functions.write_todos(todos)
    print(f"Added: {text}")
    input_field.clear()
    refresh_list()


def delete_selected():
    selected_items = todo_list.selectedItems()
    if not selected_items:
        QMessageBox.information(window, "Nothing selected", "Please select a task to delete.")
        return
    for item in selected_items:
        todos = functions.get_todos()
        todos.remove(item.text() + "\n")
        functions.write_todos(todos)
    refresh_list()


def edit_selected():
    selected_items = todo_list.selectedItems()
    new_text = input_field.text().strip()

    if not selected_items:
        QMessageBox.information(window, "Nothing selected", "Please select a task to edit.")
        return

    if not new_text:
        QMessageBox.warning(window, "Empty input", "Please enter the new text.")
        return

    old_text = selected_items[0].text()
    todos = functions.get_todos()

    try:
        index = todos.index(old_text + "\n")
        todos[index] = new_text + "\n"
        functions.write_todos(todos)
        refresh_list()
        input_field.clear()
    except ValueError:
        QMessageBox.critical(window, "Error", "Selected task not found.")


def fill_input_on_select():
    selected_items = todo_list.selectedItems()
    if selected_items:
        input_field.setText(selected_items[0].text())


refresh_list()
button.clicked.connect(add_button_click)
delete_button.clicked.connect(delete_selected)
edit_button.clicked.connect(edit_selected)
todo_list.itemClicked.connect(lambda item: fill_input_on_select())

window.setLayout(layout)
window.show()

app.exec()