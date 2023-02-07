class Pawns():
    
    points = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1,
          "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1,
          "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
          }

    
    def __init__(self):
        self.letters = []
    
    
    def addPawn(self, c):
        """
        Añade la ficha c a la lista de fichas letters
        Args:
            c: str (ficha)
        """
        self.letters.append(c)
    
    def addPawns(self, c, n):
        """
        Añade la ficha c a la lista de fichas letters n veces
        Args:
            c: str (ficha)
            n: int
        """
        for i in range(n):
            self.addPawn(c)
    
    def createBag(self):
        """
        Crea el saco de fichas
        """
        import pandas as pd
        datos_fichas = pd.read_csv('/content/drive/MyDrive/CursoPythonDeLaA-Z/csv/bag_of_pawns.csv')
    
        for ficha in datos_fichas.itertuples():
            self.addPawns(ficha[1], ficha[2]) 
    
    
    def showPawns(self):
        """
        Muestra por pantalla las fichas de Pawn
        """
        fichas_freq = self.getFrequency()
        fichas_freq.showFrequency()
                
        
    def takeRandomPawn(self):
        """
        Toma una ficha del saco de fichas y la elimina de la lista letters
        """
        import random
        ficha = self.letters.pop(random.randint(0, len(self.letters) - 1))
        return ficha
            
    def getFrequency(self):
        """
        Obtiene la frecuencia de las fichas de Pawn y lo devuelve en formato clase TableFrequencie
        """
        freq = FrequencyTable()
        for l in self.letters:
            freq.update(l)
        return freq
        
    def takePawn(self, c):
        self.letters.remove(c)
        
    def getTotalPawns(self):
        """
        Obtenemos el total de fichas del objeto
        """
        return len(self.letters)    
        
    @staticmethod    
    def getPoints(c):
        """
        Devuelve los puntos de la ficha c
        """
        return Pawns.points[c]

    @staticmethod
    def showPawnsPoints():
        """
        Muestra por pantalla la puntuación de cada ficha
        """
        print("Puntos de cada ficha: ")
        count = 0
        end = "   "
        for key in Pawns.points:
            print("{}:{}{}".format(key, " " if Pawns.getPoints(key) < 9 else "", Pawns.getPoints(key)), end = end)
            count += 1
            end = "\n" if count % 3 == 2 else "   "
        
class Word():
    
    def __init__(self):
        self.word = []
    
    def __str__(self):
        """
        Imprime la palabra en formato string
        """
        palabra = ''
        for l in self.word:
            palabra += l
        return palabra
    
    
    def areEqual(self, w):
        """
        Chequea si la palabra por parametro y la que invoca son iguales
        """
        return w.__str__() == self.__str__()
    
    def isEmpty(self):
        """
        Chequea si la palabra es vacia
        """
        return self.word == []
    
    @classmethod
    def readWord(cls):
        """
        Lee una palabra por teclado y la devuelve como un objeto Word
        """
        input_word = input().strip()
        w = Word()
        for c in input_word.upper():
          w.word.append(c)
        return w
        
    @staticmethod
    def readWordFromLine(fichero):
        """
        Lee una palabra del fichero y la devuelve como un objeto de Word
        """
        palabra = Word()
        line = fichero.readline()
        for letra in line[:-1]:
            palabra.word.append(letra)
        return palabra
        
    def getFrequency(self):
        freq = FrequencyTable()
        for l in self.word:
            freq.update(l)
        return freq
        
    def getLengthWord():
        return len(self.word)
        
class Dictionary():
    
    file_path = '/content/drive/MyDrive/CursoPythonDeLaA-Z/modules/archivostxt/dictionary.txt'
    
    @staticmethod
    def validateWord(word):
        """
        Chequea si word pertenece al txt dictionary devolviendo True or False
        """
        with open(Dictionary.file_path, 'r') as dicc:
            w = Word.readWordFromLine(dicc)
            while not (w.isEmpty() or word.areEqual(w)):
                w = Word.readWordFromLine(dicc)
        if w.isEmpty() and not word.areEqual(w):
            return False
        else:
            return True
            
    @staticmethod
    def showWords(pawns):
        """
        Muestra todas las posibles palabras que se pueden formar con dichas letras.
        """
        tf_pawns = pawns.getFrequency()
        with open(Dictionary.filepath, "r") as f:
            word = Word.readWordFromFile(f)
            while (not word.isEmpty()):
                tf_word = word.getFrequency()
                if FrequencyTable.isSubset(tf_word, tf_pawns):
                    print(word)
                word = Word.readWordFromFile(f)
        

    @staticmethod
    def showWordsPlus(pawns, c):
        """
        Muestra todas las posibles palabras que contienen el caracter c y que se pueden formar las fichas de pawns.
        """
        tf_pawns = pawns.getFrequency()
        tf_pawns.update(c)
        with open(Dictionary.filepath, "r") as f:
            word = Word.readWordFromFile(f)
            while (not word.isEmpty()):
                if c in word.word:
                    tf_word = word.getFrequency()
                    if FrequencyTable.isSubset(tf_word, tf_pawns):
                        print(word)
                word = Word.readWordFromFile(f)
        
class FrequencyTable():
    
    def __init__(self):
        self.letters = [chr(x) for x in range(ord("A"), ord("Z") + 1)]
        self.frequencies = [0]*len(self.letters)

    def showFrequency(self):
        for i in range(len(self.letters)):
            if self.frequencies[i] != 0:
                print('La frecuencia de la letra {} es {}'.format(self.letters[i], self.frequencies[i]))

    @staticmethod
    def isSubset(fq1, fq2):
        es_subconjunto = True
        for i in range(len(fq1.frequencies)):
            if fq1.frequencies[i] > fq2.frequencies[i]:
                es_subconjunto = False
                break
        return es_subconjunto

    def update(self, c):
        indice = self.letters.index(c)
        self.frequencies[indice] += 1
        
class Board():
    
    score = 0
    
    def __init__(self):
        self.board = [[" " for j in range(15)] for i in range(15)]
        self.totalWords = 0
        self.totalPawns = 0
    
    def showBoard(self):
        #print(self.board)
        print("\n ", end = " ")
        for n in range(len(self.board)):
          print("{}{} ".format(0 if n <= 9 else "", n), end = " ")
        print("\n+" + "---+" * len(self.board))
        for i in range(len(self.board)):
          print("|", end = " ")
          for j in range(len(self.board)):
            print(self.board[i][j] + " |", end = " ")
          print("{}{}".format(0 if i <= 9 else "", i), end = " ")
          print("\n+" + "---+" * len(self.board))
          
    
    def placeWord(self, player_pawns, word, x, y, direction):
        for letter in word.word:
            if letter != self.board[x][y]:
                player_pawns.takePawn(letter)
                self.totalPawns += 1
                self.board[x][y] = letter
                Board.score += Pawns.getPoints(letter)
                
            if direction == "V":
              x += 1
            if direction == "H":
              y += 1
                
        self.totalWords += 1   
        
    def isPossible(self, word, x, y, direction):
        message = ''
        x1 = x
        y1 = y
        
        #caso primer turno
        if self.totalWords == 0:
            message = 'Ninguna ficha pasa por la casilla central'
            if direction == 'V':
                if y != 7:
                    return (False, message)
                elif x + word.getLengthWord(word) - 1 < 7 or x > 7:
                    return (False, message)
            
            if direction == 'H':
                if x != 7:
                    return (False, message)
                elif y + word.getLengthWord(word) - 1 < 7 or y > 7:
                    return (False, message)
        
        #caso limites del tablero
        message = 'La palabra sobrepasa los limites del tablero'
        if direction == 'H' and x + word.getLengthWord(word) - 1 > 14:
            return (False, message)
        if direction == 'V' and y + word.getLengthWord(word) - 1 > 14:
            return (False, message)
        if x < 0 or y < 0 or x > 14 or y > 14:
            return (False, message)
            
        #caso se debe usar una ficha ya existente en el tablero
        if self.totalWords > 0:
            lugares = []
            for c in word.word:
                if self.board[x][y] == " ":
                    lugares.append(c)
                  
                if direction == "V":
                    x += 1
                if direction == "H":
                    y += 1
            
            if len(lugares) == word.getLengthWord():
                message = "No se está utilizando ninguna ficha del tablero"
                return (False, message)

        #caso casillas libres
        x = x1
        y = y1
        for l in word.word:
            if self.board[x][y] != " " and self.board[x][y] != c:
                message = "Hay una ficha diferente ocupando una posición"
                return (False, message)
            if direction == "V":
                x += 1
            if direction == "H":
                y += 1
        
        #caso una ficha por casilla
        x = x1
        y = y1
        palabra = []
        for l in word.word:
            if self.board[x][y] == l:
                palabra.append(l)
            if direction == "V":
                x += 1
            if direction == "H":
                y += 1
        
        if len(palabra) == word.getLengthWord():
            message = "Recuerde que debe usar una ficha nueva en el tablero"
            return (False, message)
          
        #caso fichas adicionales
        message = "Hay fichas adicionales a principio o final de palabra"
        x = x1
        y = y1
        if direction == "V" and ((x != 0 and self.board[x - 1][y] != " ") or (x + word.getLengthWord() != 14 and self.board[x + word.getLengthWord()][y] != " ")):
            return (False, message)
        if direction == "H" and ((y != 0 and self.board[x][y - 1] != " ") or (y + word.getLengthWord() != 14 and self.board[x][y + word.getLengthWord()] != " ")):
            return (False, message)
      
        message = "La palabra se puede agregar al tablero"
        return (True, message)
      
    def getPawns(self, word, x, y, direccion):
        letrasNec = Word()
        esPosible, message = self.isPossible(word, x, y, direccion)
        if not esPosible:
            print(message)
        else:
            for c in word.word:
                if self.board[x][y] != c:
                    letrasNec.word.append(c)
                if direccion == "V":
                    x += 1
                if direccion == "H":
                    y += 1
                    
        return letrasNec
        
    def showWordPlacement(self, player_pawns, word):
        for direction in ["V", "H"]:
        print("{}:".format("Direccion vertical" if direction == "V" else "Direccion horizontal"))
        for i in range(15):
            for j in range(15):
                if self.isPossible(word, i, j, direction)[0] == True:
                    needed_pawns = self.getPawns(word, i, j, direction)
                    if FrequencyTable.isSubset(needed_pawns.getFrequency(), player_pawns.getFrequency()):
                        print("(x = {}, y = {})".format(i, j))
                        
