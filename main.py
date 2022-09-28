from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from random import choices
import sys
import css


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.computerRandomChoice = None
        self.playerRandomChoice = None
        self.setGeometry(200, 200, 600, 400)
        self.setWindowTitle("Rock-Paper-Scissor")

        # Graphics
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.8)

        self.opacity_effect_name = QGraphicsOpacityEffect()
        self.opacity_effect_name.setOpacity(0.6)

        self.opacity_effect_name_ = QGraphicsOpacityEffect()
        self.opacity_effect_name_.setOpacity(0.6)


        # Constants
        self.computerScore = 0
        self.playerScore = 0
        self.noStart = 0
        self.running = False

        self.computerText = f""" Computer Score 
           {self.computerScore}"""
        
        self.playerText = f""" Player Score 
         {self.playerScore}"""

        # Widgets

        # Labels
        self.background = QLabel(self)
        self.scoreBanner = QLabel(self)
        self.computerScoreText = QLabel(self)
        self.playerScoreText = QLabel(self)
        self.computerScoreValue = QLabel(self)
        self.playerScoreValue = QLabel(self)

        #Play area 
        self.playAreaBg = QLabel(self)
        self.btnRock = QPushButton(self)
        self.btnScissor = QPushButton(self)
        self.btnPaper = QPushButton(self)
        self.btnStart = QPushButton(self)

        #Computer play area
        self.computerPlayArea = QLabel(self)
        self.computerNameTag = QLabel(self)
        self.computerChoice = QLabel(self)

        #Player play area 
        self.playerPlayArea = QLabel(self)
        self.playerNameTag = QLabel(self)
        self.playerChoice = QLabel(self)

        #QTimer 
        self.timer = QTimer(self)
        self.timer.setInterval(200)
        self.timer.timeout.connect(lambda: self.playGame())

        self.ui()
    
    def ui(self):

        # Background images
        self.background.resize(600,400)
        self.background.setStyleSheet(css.backgroundCSS)

        self.playAreaBg.setGeometry(50, 110, 500, 210)
        self.playAreaBg.setStyleSheet(css.playAreaCSS)

        self.scoreBanner.setStyleSheet(css.scoreBannerCSS)
        self.scoreBanner.setGeometry(50, 5 ,500, 70)
        self.scoreBanner.setGraphicsEffect(self.opacity_effect)


        self.computerScoreText.setText(self.computerText)
        self.computerScoreText.setObjectName("scoreBoard")
        self.computerScoreText.setGeometry(60, 13, 130, 50)

        self.playerScoreText.setText(self.playerText)
        self.playerScoreText.setGeometry(440, 13, 100, 50)
        self.playerScoreText.setObjectName("scoreBoard")

        self.computerPlayArea.setGeometry(70, 125, 150, 180)
        self.computerPlayArea.setStyleSheet(css.choicePlayAreaCSS)
        self.computerPlayArea.setGraphicsEffect(self.opacity_effect_name)

        self.playerPlayArea.setGeometry(380, 125, 150, 180)
        self.playerPlayArea.setStyleSheet(css.choicePlayAreaCSS)
        self.playerPlayArea.setGraphicsEffect(self.opacity_effect_name_)

        self.computerNameTag.setText("Computer")
        self.computerNameTag.setGeometry(95, 130, 95, 20)
        self.computerNameTag.setAlignment(Qt.AlignCenter)
        self.computerNameTag.setStyleSheet(css.nameTagCSS)

        self.playerNameTag.setText("player")
        self.playerNameTag.setGeometry(405, 130, 95, 20)
        self.playerNameTag.setAlignment(Qt.AlignCenter)
        self.playerNameTag.setStyleSheet(css.nameTagCSS)


        self.btnRock.setGeometry(100, 330, 50, 50)
        self.btnRock.setStyleSheet(css.btn.format(path= "icons8-rock-80.png"))
        self.btnRock.setObjectName("RockBtn")
        self.btnRock.clicked.connect(lambda: self.playGame(playerChoice="rock"))

        self.btnPaper.setGeometry(250, 330, 50, 50)
        self.btnPaper.setStyleSheet(css.btn.format(path="icons8-paper-100.png"))
        self.btnPaper.clicked.connect(lambda: self.playGame(playerChoice="paper"))

        self.btnScissor.setGeometry(400, 330, 50, 50)
        self.btnScissor.setStyleSheet(css.btn.format(path="icons8-scissor-64.png"))
        self.btnScissor.clicked.connect(lambda: self.playGame(playerChoice="scissor"))

        self.btnStart.setGeometry(520, 330, 50, 50)
        self.btnStart.setStyleSheet(css.btn.format(path= "play.png"))
        self.btnStart.setObjectName("start")
        self.btnStart.clicked.connect(self.startBtn)

        self.computerChoice.setGeometry(95, 180, 96, 96)
        self.computerChoice.setStyleSheet(css.choiceDefault.format(path="computer-rock.png"))

        self.playerChoice.setGeometry(405, 180 , 96, 96)
        self.playerChoice.setStyleSheet(css.choiceDefault.format(path= "player-rock.png"))

    def startBtn(self):
        if self.noStart % 2 == 0:
            self.running = True
            self.btnStart.setStyleSheet(css.btn.format(path="pause.png"))
            self.timer.start()
            self.noStart += 1
        else:
            self.stopBtn()


    def stopBtn(self):
        self.running = False
        self.btnStart.setStyleSheet(css.btn.format(path="play.png"))
        self.timer.stop()
        self.noStart += 1

    def playGame(self, playerChoice= None):
        playerOptions = {"rock":"player-rock.png", "paper":"player-paper.png", "scissor":"player-scissor.png"}
        computerOptions = {"rock":"computer-rock.png", "paper":"computer-paper.png", "scissor":"computer-scissor.png"}
        if self.running:
            self.computerRandomChoice = choices(list(computerOptions.keys()))
            if playerChoice:
                self.playerRandomChoice = playerChoice
                self.computerRandomChoice, self.playerRandomChoice = self.computerRandomChoice[0], self.playerRandomChoice
                self.playerChoice.setStyleSheet(css.choiceDefault.format(path=playerOptions[self.playerRandomChoice]))
                self.computerChoice.setStyleSheet(css.choiceDefault.format(path=computerOptions[self.computerRandomChoice]))
                self.stopBtn()
                self.gameLogic(self.computerRandomChoice, playerChoice)
                
                

            else:
                self.playerRandomChoice = choices(list(playerOptions.keys()))
                self.playerRandomChoice, self.computerRandomChoice = self.playerRandomChoice[0], self.computerRandomChoice[0]
                self.playerChoice.setStyleSheet(css.choiceDefault.format(path=playerOptions[self.playerRandomChoice]))
                self.computerChoice.setStyleSheet(css.choiceDefault.format(path=computerOptions[self.computerRandomChoice]))
        
    def round(self, result):
        win = 'You won | pc loses'
        lose = 'You lose | pc Won'
        tie = 'Its an Tie'
        if result == "win":
            self.playerScore += 1
            self.playerText = f""" Player Score 
         {self.playerScore}"""
            self.playerScoreText.setText(f"{self.playerText}")
            QMessageBox.information(self, "Result !", win)

        elif result == "lose":
            self.computerScore += 1
            self.computerText = f""" Computer Score 
            {self.computerScore}"""
            self.computerScoreText.setText(f"{self.computerText}")
            QMessageBox.information(self, "Result !", lose)

        else:
            QMessageBox.information(self, "Result !", tie)

    def gameLogic(self, computerChoice, playerChoice):
        if computerChoice == playerChoice:
            self.round("tie")
        elif computerChoice == "rock":
            if playerChoice == "paper":
                self.round("win")
            elif playerChoice == "scissor":
                self.round("lose")
        elif computerChoice == "paper":
            if playerChoice == "rock":
                self.round("lose")
            elif playerChoice == "scissor":
                self.round("win")
        elif computerChoice == "scissor":
            if playerChoice == "rock":
                self.round("win")
            elif playerChoice == "paper":
                self.round("lose")
        else:
            print("something isn't right ....")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    window.setStyleSheet(css.__doc__)

    QFontDatabase.addApplicationFont("K2D-Light.ttf")
    sys.exit(app.exec_())
