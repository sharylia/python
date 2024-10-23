import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QFileDialog, QMessageBox
from PyQt5.QtCore import QFileInfo

class NotesApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Заметки")
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.create_menu()

        self.current_file = None

    def create_menu(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("Файл")

        new_note_action = QAction("Новая заметка", self)
        new_note_action.setShortcut("Ctrl+N")
        new_note_action.triggered.connect(self.new_note)
        file_menu.addAction(new_note_action)

        save_note_action = QAction("Сохранить заметку", self)
        save_note_action.setShortcut("Ctrl+S")
        save_note_action.triggered.connect(self.save_note)
        file_menu.addAction(save_note_action)

    def new_note(self):
        # Очищаем текстовое поле для новой заметки
        self.text_edit.clear()
        self.current_file = None
        self.setWindowTitle("Новая заметка")

    def save_note(self):
        # Если файл не существует, открываем диалог для сохранения
        if not self.current_file:
            file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Text Files (*.txt);;All Files (*)")
            if file_path:
                self.current_file = file_path
                self.write_to_file(file_path)
            else:
                QMessageBox.warning(self, "Предупреждение", "Сохранение отменено.")
        else:
            # Если файл уже существует, перезаписываем его
            self.write_to_file(self.current_file)

    def write_to_file(self, file_path):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.text_edit.toPlainText())
            self.setWindowTitle(f"Заметка - {QFileInfo(file_path).fileName()}")
            QMessageBox.information(self, "Успех", "Заметка успешно сохранена!")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при сохранении файла: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = NotesApp()
    window.show()

    sys.exit(app.exec_())
