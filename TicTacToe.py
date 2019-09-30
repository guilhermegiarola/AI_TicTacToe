import os
from copy import deepcopy
import time

class TicTacToe:
    def __init__(self):
        self.boardTable = []
        for i in range(0,3):
            self.boardTable.append([])
        self.turn = True
        self.setBoard()
        self.movesList = []

    def setBoard(self):    
        for i in range(0,3):
            for j in range(0,3):
                self.boardTable[i].append('-')
    
    def printBoard(self):
        print ("X")
        for i in range(0,3):
            print(str(i) + " " + self.boardTable[i][2] + " " 
            + self.boardTable[i][1]
            + " " + self.boardTable[i][0])
            print()
        print("  2 1 0 Y")
   
    def makePlay(self):
        numPlays = 0
        print("Número de jogadas: " + str(numPlays))
        self.printBoard()
        while numPlays < 9:
            while self.turn:
                print("Insira a posição em X: ")
                x = input()
                
                print("Insira a posição em Y: ")
                y = input()

                if self.boardTable[int(x)][int(y)] == '-' :
                    self.boardTable[int(x)][int(y)] = 'o'
                    os.system('clear')
                    
                    self.printBoard()

                    self.turn = False
                    numPlays += 1

                    if self.isFinal(self.boardTable):
                        print("Vitória!")
                        return 
                
                else:
                    print('Jogada inválida!')
                    
            while not self.turn:
                print("Número de jogadas: " + str(numPlays))                
                self.boardTable = self.MiniMax(self.boardTable, True)
                
                os.system('clear')
                self.printBoard()
                self.turn = True
                numPlays += 1 

                if self.isFinal(self.boardTable):
                    print("Derrota!")
                    return
        print("Empate!") 
    
    def MiniMax(self, table, isMaximizingPlayer):
        pontuationList = []
        
        #Se estiver maximizando a jogada:
        if isMaximizingPlayer:
            #Dentre as possíveis jogadas:
            for i in self.generateStates(True, table):
                self.movesList.append(i)
                #Retorna a melhor jogada dos filhos, para cada possível jogada.
                value = self.MiniMax(i, False)
                pontuationList.append(value)
            
            bestValue = -10000
            #Escolhe a melhor pior jogada:
            for i in range(0, len(self.movesList)):
                if(self.isFinal(self.movesList[i])):
                    table = self.movesList[i]
                    return table
                elif int(pontuationList[i]) > int(bestValue):
                    bestValue = pontuationList[i]    
                    table = self.movesList[i]
            
            self.movesList = []
            return table

        #Se estiver minimizando a jogada:
        if not isMaximizingPlayer:
            moves = []
            bestValue = 10000
            for i in self.generateStates(False, table):
                moves.append(i)
                print(i)
            
            for i in moves:
                if self.getPontuation(i) < bestValue:
                    print(bestValue)
                    bestValue = self.getPontuation(i)
                    print(table)
            return bestValue





    def generateStates(self, aux, table):
        statesGenerated = []

        if aux is True:
            for x in range(0,3):
                for y in range(0,3):
                    auxTable = deepcopy(table)
                    if auxTable[int(x)][int(y)] == '-':
                        auxTable[int(x)][int(y)] = 'x'
                        statesGenerated.append(auxTable)

        else:
            for x in range(0,3):
                for y in range(0,3):
                    auxTable = deepcopy(table)
                    if auxTable[int(x)][int(y)] == '-':
                        auxTable[int(x)][int(y)] = 'o'
                        statesGenerated.append(auxTable)
        return statesGenerated
                

    def isFinal(self, table):

        winCons = []
        for i in range(0,16):
            winCons.append(0)

        for i in range(0,3):
            if table[i][i] == 'o':
                winCons[0] += 1
            if table[(2-i)][(i)] == 'o':
                winCons[1] += 1
            if table[0][i] == 'o':
                winCons[2] += 1
            if table[1][i] == 'o':
                winCons[3] += 1
            if table[2][i] == 'o':
                winCons[4] += 1
            if table[i][0] == 'o':
                winCons[5] += 1
            if table[i][1] == 'o':
                winCons[6] += 1
            if table[i][2] == 'o':
                winCons[7] += 1

            if table[i][i] == 'x':
                winCons[8] += 1
            if table[(2-i)][(i)] == 'x':
                winCons[9] += 1
            if table[0][i] == 'x':
                winCons[10] += 1
            if table[1][i] == 'x':
                winCons[11] += 1
            if table[2][i] == 'x':
                winCons[12] += 1
            if table[i][0] == 'x':
                winCons[13] += 1
            if table[i][1] == 'x':
                winCons[14] += 1
            if table[i][2] == 'x':
                winCons[15] += 1
            
        for i in range(0,15):
            if winCons[i] == 3:
                return True
        return False
    
    def getPontuation(self, table):
        gameStatus = []
        pontuation = 0
        for i in range(0,16):
            gameStatus.append(0)

        for i in range(0,3):
            if table[i][i] == 'o':
                gameStatus[0] += 1
            if table[(2-i)][(i)] == 'o':
                gameStatus[1] += 1
            if table[0][i] == 'o':
                gameStatus[2] += 1
            if table[1][i] == 'o':
                gameStatus[3] += 1
            if table[2][i] == 'o':
                gameStatus[4] += 1
            if table[i][0] == 'o':
                gameStatus[5] += 1
            if table[i][1] == 'o':
                gameStatus[6] += 1
            if table[i][2] == 'o':
                gameStatus[7] += 1

            if table[i][i] == 'x':
                gameStatus[8] += 1
            if table[(2-i)][(i)] == 'x':
                gameStatus[9] += 1
            if table[0][i] == 'x':
                gameStatus[10] += 1
            if table[1][i] == 'x':
                gameStatus[11] += 1
            if table[2][i] == 'x':
                gameStatus[12] += 1
            if table[i][0] == 'x':
                gameStatus[13] += 1
            if table[i][1] == 'x':
                gameStatus[14] += 1
            if table[i][2] == 'x':
                gameStatus[15] += 1
            
        for i in range(0,7):
            if gameStatus[i] == 3:
                pontuation += -100
            elif gameStatus[i] == 2:
                pontuation += -10
            elif gameStatus[i] == 1:
                pontuation += -1
        for i in range(8,16):
            if gameStatus[i] == 3:
                pontuation += 100
            elif gameStatus[i] == 2:
                pontuation += 10
            elif gameStatus[i] == 1:
                pontuation += 1
        return int(pontuation)

if __name__ == '__main__':
    game = TicTacToe()
    isFirst = True
    test = game.makePlay()
            