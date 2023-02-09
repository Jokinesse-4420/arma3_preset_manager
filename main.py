import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget
from file import extractor
from file import writer as write

LISTS_MODS = extractor.extract_mods()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Création de la barre de boutons
        button_layout = QHBoxLayout()
        self.union_button = QPushButton("Merge")
        self.difference_button = QPushButton("Difference")
        button_layout.addWidget(self.union_button)
        button_layout.addWidget(self.difference_button)

        # Ajout des boutons à la fenêtre principale
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Connexion des signaux aux fonctions
        self.union_button.clicked.connect(self.union_clicked)
        self.difference_button.clicked.connect(self.difference_clicked)

    def union_clicked(self):
        write.write_new_preset(LISTS_MODS[0] | LISTS_MODS[1])

    def difference_clicked(self):
        write.write_new_preset(LISTS_MODS[0] ^ LISTS_MODS[1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
