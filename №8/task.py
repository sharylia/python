import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget, QLabel, QSlider
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Видеоплеер")
        self.setGeometry(100, 100, 800, 500)

        self.video_widget = QWidget(self)
        self.setCentralWidget(self.video_widget)

        self.media_player = QMediaPlayer(self)
        
        self.create_interface()

        # Соединение сигналов
        self.media_player.positionChanged.connect(self.update_slider)
        self.media_player.durationChanged.connect(self.update_duration)
        
    def create_interface(self):
        layout = QVBoxLayout()

        self.file_button = QPushButton("Выбрать файл", self)
        self.file_button.clicked.connect(self.open_file)
        layout.addWidget(self.file_button)

        self.file_label = QLabel("Выберите видеофайл...", self)
        layout.addWidget(self.file_label)

        # Ползунок для регулировки времени
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.sliderMoved.connect(self.set_position)
        layout.addWidget(self.slider)

        # Кнопки управления
        self.play_button = QPushButton("Воспроизвести", self)
        self.play_button.clicked.connect(self.play_video)
        layout.addWidget(self.play_button)

        self.pause_button = QPushButton("Пауза", self)
        self.pause_button.clicked.connect(self.pause_video)
        layout.addWidget(self.pause_button)

        self.stop_button = QPushButton("Стоп", self)
        self.stop_button.clicked.connect(self.stop_video)
        layout.addWidget(self.stop_button)

        # Ползунок для регулировки громкости
        self.volume_slider = QSlider(Qt.Horizontal, self)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged.connect(self.set_volume)
        layout.addWidget(self.volume_slider)

        self.video_widget.setLayout(layout)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите видеофайл", "", "Video Files (*.mp4 *.avi *.mov *.mkv)")
        if file_name:
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
            self.file_label.setText(file_name)

    def play_video(self):
        self.media_player.play()

    def pause_video(self):
        self.media_player.pause()

    def stop_video(self):
        self.media_player.stop()

    def set_volume(self, value):
        self.media_player.setVolume(value)

    def set_position(self, position):
        self.media_player.setPosition(position)

    def update_slider(self, position):
        self.slider.setValue(position)

    def update_duration(self, duration):
        self.slider.setRange(0, duration)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = VideoPlayer()
    window.show()

    sys.exit(app.exec_())
