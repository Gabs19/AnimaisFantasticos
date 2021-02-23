from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QStringListModel
from animais import animais


def listAnimal():
    for i in range(len(animais)):
        nome = f'{animais[i]["nome"]}'
        window.listAnimals.addItem(nome)

def selectAnimal():
    item = window.listAnimals.currentIndex()
    print(str(item))
    


def description(id):
    window.textBrowser.clear()
    description = f'{animais[id]["descrição"]}'
    window.textBrowser.insertPlainText(description)


def naction():
    window.textBrowser.clear()
    nation = f'{animais[1]["nacionalidade"]}'
    window.textBrowser.insertPlainText(nation)


def risc():
    window.textBrowser.clear()
    risc = f'{animais[1]["risco"]}'
    window.textBrowser.insertPlainText(risc)


def defense():
    window.textBrowser.clear()
    defense = f'{animais[1]["proteção"]}'
    window.textBrowser.insertPlainText(defense)


def curio():
    window.textBrowser.clear()
    curio = f'{animais[1]["curiosidades"]}'
    window.textBrowser.insertPlainText(curio)


app = QtWidgets.QApplication([])
window = uic.loadUi('fantasticWindow.ui')


window.descriptionButton.clicked.connect(lambda: description(0))
window.nationButton.clicked.connect(naction)
window.riscButton.clicked.connect(risc)
window.defenseButton.clicked.connect(defense)
window.curioButton.clicked.connect(curio)
window.listAnimals.clicked.connect(selectAnimal)


listAnimal() #list all animals

window.show()
app.exec()
