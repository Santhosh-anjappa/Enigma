import numpy as np

rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor1Notch = 'Q'
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor2Notch = 'E'
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
rotor3Notch = 'V'
rotor4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
rotor4Notch = 'J'
rotor5 = "VZBRGITYUPSDNHLXAWMJQOFECK"
rotor5Notch = 'Z'

rotors = {1:rotor1, 2: rotor2, 3: rotor3, 4: rotor4, 5: rotor5}
rotorsNotch = {1: rotor1Notch, 2: rotor2Notch, 3: rotor3Notch, 4: rotor4Notch, 5: rotor5Notch, }

reflectorB = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

ringSetting ="FVN"
PB = { 'A':'A', 'B':'J', 'C':'X', 'D':'D', 'E':'S', 'F':'Q', 'G':'O', 'H':'Y', 'I':'T', 'J':'B', 'K':'L', 'L':'K', 'M':'M', 'N':'P', 'O':'G', 'P':'N', 'Q':'F', 'R':'R', 'S':'E', 'T':'I', 'U':'U', 'V':'Z', 'W':'W', 'X':'C', 'Y':'H', 'Z':'V' }

initialSetting = "EHZ"
rotorSettiing = [1,2,5]

rotorA = rotors[rotorSettiing[0]]
rotorB = rotors[rotorSettiing[1]]
rotorC = rotors[rotorSettiing[2]]

rotorA = rotorA[( ord(ringSetting[0]) - ord('A') ) :] + rotorA[: ( ord(ringSetting[0]) - ord('A') )]
rotorB = rotorB[( ord(ringSetting[1]) - ord('A') ) :] + rotorB[: ( ord(ringSetting[1]) - ord('A') )]
rotorC = rotorC[( ord(ringSetting[2]) - ord('A') ) :] + rotorC[: ( ord(ringSetting[2]) - ord('A') )]

rotorA = np.array([ord(i) - ord('A') for i in rotorA])
rotorB = np.array([ord(i) - ord('A') for i in rotorB])
rotorC = np.array([ord(i) - ord('A') for i in rotorC])

reflec = np.array([ord(i)- ord('A') for i in reflectorB])

def rotate(rotor):
    ele = rotor[-1]
    rotor = np.delete(rotor,-1)
    rotor = np.insert(rotor,0,ele)
    rotor = (rotor + 1) % 26
    return rotor

# initial settings
for i in range(ord(initialSetting[0])-ord('A')):
    rotorA = rotate(rotorA)

for i in range(ord(initialSetting[1])-ord('A')):
    rotorB = rotate(rotorB)

for i in range(ord(initialSetting[2])-ord('A')):
    rotorC = rotate(rotorC)

displayLetters = initialSetting[:]
print(displayLetters)
inpu = 'IHKNMXFS'
rotateB = False
rotateC = False

for inp in inpu:

    if(displayLetters[0] == rotorsNotch[rotorSettiing[0]]):
        rotateB = True
    rotorA = rotate(rotorA)
    displayLetters = chr((((ord(displayLetters[0]) - ord('A')) + 1) % 26) + ord('A')) + displayLetters[1] + displayLetters[2]
    

    if(rotateB == True):
        if(displayLetters[1] == rotorsNotch[rotorSettiing[1]]):
            rotateC = True
        rotorB = rotate(rotorB)
        displayLetters = displayLetters[0] + chr((((ord(displayLetters[1]) - ord('A')) + 1) % 26) + ord('A')) + displayLetters[2]
        rotateB = False
        

    if(rotateC == True):
        rotorC = rotate(rotorC)
        displayLetters = displayLetters[0] + displayLetters[1] + chr((((ord(displayLetters[2]) - ord('A')) + 1) % 26) + ord('A'))
        rotateC = False

    inpPB = PB[inp]
    rAout = rotorA[ord(inpPB)-ord('A')]
    rBout = rotorB[rAout]
    rCout = rotorC[rBout]
    refOut = reflec[rCout]
    rCouti = np.where(rotorC==refOut)
    rBouti = np.where(rotorB==rCouti[0])
    rAouti = np.where(rotorA==rBouti[0])

    out = chr(rAouti[0]+65)
    print(inp,"<=>", PB[out])
