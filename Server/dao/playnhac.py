from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
import pygame  # Import pygame for audio playback

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize pygame mixer for audio
        pygame.mixer.init()

        # Create widget and layout
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # Create buttons and label
        button1 = QPushButton("Phát nhạc 1")
        button2 = QPushButton("Phát nhạc 2")
        self.label = QLabel("")

        # Add elements to layout
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(self.label)

        # Connect button clicks to functions
        button1.clicked.connect(self.play_song1)
        button2.clicked.connect(self.play_song2)

    def play_song1(self):
        # Replace 'path/to/song1.mp3' with your actual music file path
        song_path = "Server/dao/songs/khoalybiet.mp3"
        pygame.mixer.stop()

        try:
            # Load the song using pygame mixer
            song = pygame.mixer.Sound(song_path)
            song.play()
            self.label.setText("Đang phát: Nhạc 1")
        except Exception as e:
            print(f"Error playing song 1: {e}")
            self.label.setText("Có lỗi khi phát nhạc!")

    def play_song2(self):
        # Replace 'path/to/song2.mp3' with your actual music file path
        song_path = "Server/dao/songs/roiemsegapmotchangtraikhac.mp3"
        pygame.mixer.stop()

        try:
            # Load the song using pygame mixer
            song = pygame.mixer.Sound(song_path)
            song.play()
            self.label.setText("Đang phát: Nhạc 2")
        except Exception as e:
            print(f"Error playing song 2: {e}")
            self.label.setText("Có lỗi khi phát nhạc!")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
