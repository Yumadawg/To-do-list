from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox, QListWidget
)
from PyQt6.QtCore import QTimer, QTime, QDateTime
from PyQt6.QtGui import QFont
import functions
import themes
from datetime import datetime


app = QApplication([])
app.setStyleSheet(themes.light_theme)
current_theme = "light"

window = QWidget()
window.setWindowTitle("My To-Do list")
window.resize(500, 70)

top_bar_layout = QHBoxLayout()
top_bar_layout.addStretch()

light_button = QPushButton("N/L")
light_button.setFont(QFont("Segoe UI", 6))
light_button.setFixedSize(25, 20)
top_bar_layout.addWidget(light_button)

layout = QVBoxLayout()
layout.setContentsMargins(10, 10, 10, 10)
layout.setSpacing(5)
font = QFont("Segoe UI", 13)

layout.addLayout(top_bar_layout)

datetime_label = QLabel()
datetime_label.setFont(font)
layout.addWidget(datetime_label)

label = QLabel("Write a To-do")
label.setFont(font)
layout.addWidget(label)

input_field = QLineEdit()
input_field.setFont(font)

button = QPushButton("Add")
button.setFont(font)
button.setFixedWidth(70)

input_layout = QHBoxLayout()
input_layout.addWidget(input_field)
input_layout.addWidget(button)

layout.addLayout(input_layout)

todo_list = QListWidget()
todo_list.setFont(font)

delete_button = QPushButton("Complete")
delete_button.setFont(font)
delete_button.setFixedWidth(70)

edit_button = QPushButton("Edit")
edit_button.setFont(font)
edit_button.setFixedWidth(70)

buttons_layout = QVBoxLayout()
buttons_layout.addWidget(edit_button)
buttons_layout.addWidget(delete_button)

work_layout = QHBoxLayout()
work_layout.addWidget(todo_list)
work_layout.addLayout(buttons_layout)

layout.addLayout(work_layout)

def add_button_click():
    text = input_field.text()
    if not text.strip():
        QMessageBox.warning(window, "Empty input", "Please write something before adding.")
        return
    todos = functions.get_todos()
    todos.append(text + "\n")
    functions.write_todos(todos)
    input_field.clear()
    functions.refresh_list(todo_list)


def delete_selected():
    selected_items = todo_list.selectedItems()
    if not selected_items:
        QMessageBox.information(window, "Nothing selected", "Please select a task to delete.")
        return
    for item in selected_items:
        todos = functions.get_todos()
        todos.remove(item.text() + "\n")
        functions.write_todos(todos)
    functions.refresh_list(todo_list)


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
        functions.refresh_list(todo_list)
        input_field.clear()
    except ValueError:
        QMessageBox.critical(window, "Error", "Selected task not found.")


def fill_input_on_select():
    selected_items = todo_list.selectedItems()
    if selected_items:
        input_field.setText(selected_items[0].text())


def toggle_theme():
    global current_theme
    if current_theme == "dark":
        app.setStyleSheet(themes.light_theme)
        current_theme = "light"
    else:
        app.setStyleSheet(themes.dark_theme)
        current_theme = "dark"


def update_datetime():
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    datetime_label.setText(f"Current time: {now}")

timer = QTimer()
timer.timeout.connect(update_datetime)
timer.start(1000)

update_datetime()
functions.refresh_list(todo_list)
button.clicked.connect(add_button_click)
delete_button.clicked.connect(delete_selected)
edit_button.clicked.connect(edit_selected)
light_button.clicked.connect(toggle_theme)
todo_list.itemClicked.connect(lambda item: fill_input_on_select())

window.setLayout(layout)
window.show()

app.exec()