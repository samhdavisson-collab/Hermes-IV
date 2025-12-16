import pygame
from sys import exit
import random
import time

pygame.init()
pygame.display.set_caption("Escape the Terminal")
screen = pygame.display.set_mode((800, 620))
clock = pygame.time.Clock()

def iterate_nested_dict(d, i, t):
    for key, value in d.items():
        if key == i:
            #print(key, value)
            return find_files(value, t)
        elif isinstance(value, dict):
            # If the value is a dictionary, recursively call the function
            foundsomething = iterate_nested_dict(value, i, t)
            # try:
            #     if len(foundsomething) > 0:
            #         return foundsomething
            #     if len(foundsomething.keys()) > 0:
            #         return foundsomething
            # except:
            #     key = key
            if foundsomething:
                return foundsomething
            else:
                foundsomething = t

def find_files(d, t):
    if t == str:
        found = {}
    elif t == dict:
        found = []
    for key, value in d.items():
        if t == str:
            if isinstance(value, str):
                found[key] = value
        elif t == dict:
            if isinstance(value, dict):
                found.append(key)
    return found

#print(iterate_nested_dict({"0":{"1":"hi", "2":"hello", "2.3":{"1": "wassup", "2": "'sup"}, "3":{"3.1":"hi", "3.2":"hello"}}}, "2.3", str))
#print(iterate_nested_dict({"0":{"1":"hi", "2":"hello", "2.3":{"1": "wassup", "2": "'sup"}, "3":{"3.1":"hi", "3.2":"hello"}}}, "2.3", dict))
#print(iterate_nested_dict({"0":{"1":"hi", "2":"hello", "2.3":{"1": "wassup", "2": "'sup"}, "3":{"3.1":"hi", "3.2":"hello"}}, "50":{"1000":"676767", "200":{"greetings":"hi", "salutations":"hello"}}}, "200", str))
#print(iterate_nested_dict({"0":{"1":"hi", "2":"hello", "2.3":{"1": "wassup", "2": "'sup"}, "3":{"3.1":"hi", "3.2":"hello"}}, "50":{"1000":"676767", "200":{"greetings":"hi", "salutations":"hello"}}}, "50", dict))

img1 = pygame.transform.scale_by(pygame.image.load("cuts/image_part_001.jpg"), 0.5)
img2 = pygame.transform.scale_by(pygame.image.load("cuts/image_part_002.jpg"), 0.5)
img3 = pygame.transform.scale_by(pygame.image.load("cuts/image_part_003.jpg"), 0.5)
img4 = pygame.transform.scale_by(pygame.image.load("cuts/image_part_004.jpg"), 0.5)

badimg1 = pygame.transform.scale_by(pygame.image.load("blurrydash/image_part_001.jpg"), 0.5)
badimg2 = pygame.transform.scale_by(pygame.image.load("blurrydash/image_part_002.jpg"), 0.5)
badimg3 = pygame.transform.scale_by(pygame.image.load("blurrydash/image_part_003.jpg"), 0.5)
badimg4 = pygame.transform.scale_by(pygame.image.load("blurrydash/image_part_004.jpg"), 0.5)

letters = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890-=[]{}<>,./?`"
seq1 = ""
for i in range(random.randint(6, 10)):
    seq1 += letters[random.randint(0, len(letters)-1)]

puzzle1nums = ""
puzzle1val = ""
for i in range(len(seq1)):
    dist = random.randint(0, 7)
    puzzle1nums += str(dist)
    for j in range(dist):
        puzzle1val += letters[random.randint(0, len(letters)-1)]
    puzzle1val += seq1[i]
for i in range(random.randint(0, 7)):
    puzzle1val += letters[random.randint(0, len(letters) - 1)]
# print(puzzle1nums)
# print(puzzle1val)
# print(seq1)

puzzle1 = puzzle1nums + "~" + puzzle1val

seq2 = ""
for i in range(random.randint(8, 14)):
    seq2 += letters[random.randint(0, len(letters)-1)]
seq3 = ""
for i in range(random.randint(10, 18)):
    seq3 += letters[random.randint(0, len(letters)-1)]
seq4 = ""
for i in range(random.randint(10, 18)):
    seq4 += letters[random.randint(0, len(letters)-1)]

font = pygame.font.Font("Menlo-Regular.ttf", 25)
font.set_bold(True)
cursor = pygame.Surface((15, 25))
cursor.fill("green")
cursoroutline = pygame.Surface((13, 23))
cursoroutline.fill("black")

line = font.render("", True, "white")

currentline = 0
myinputs = []

mytext = ""
entered = False

startdirs = []
startfiles = {"puzzle.txt":puzzle1, "startup_diagram.png":"", "trap.txt":"§"}
directory = "~"
#directories = startdirs
# decoderdirs = []
# decodersfiles = {"decoder1.txt":"§", "decoder2.txt":"§", "decoder3.txt":"§", "decoder4.txt":"input " + seq1 + "to continue", "decoder5.txt":"§"}
files = startfiles
pastdirectory = ""

badwords = ["bad", "horrible", "evil", "horrific", "cataclysmic", "catastrophic", "disastrous", "diabolical", "dont"]
goodwords = ["good", "great", "wonderful", "fantastic", "amazing"]

word = ""
scrambled = ""
letters = []
letter = 0
badwordsinthis = []
for i in range(random.randint(4, 12)):
    word = badwords[random.randint(0, len(badwords)-1)]
    scrambled = ""
    letters = []
    for j in range(len(word)):
        letter = random.randint(0, len(word)-1)
        while letter in letters:
            letter = random.randint(0, len(word)-1)
        scrambled += word[letter]
        letters.append(letter)
    badwordsinthis.append(scrambled + ".txt")
#print(badwordsinthis)

word = goodwords[random.randint(0, len(goodwords)-1)]
letter = 0
letters = []
goodword = ""
for i in range(len(word)):
    while letter in letters:
        letter = random.randint(0, len(word)-1)
    goodword += word[letter]
    letters.append(letter)
goodword = goodword + ".txt"
#print(goodword)


crsabmlde = {}
for i in range(random.randint(2, len(badwordsinthis) - 2), 0, -1):
    crsabmlde[badwordsinthis[i]] = "§"
    del badwordsinthis[i]
crsabmlde[goodword] = "input " + seq3 + " to continue"
for i in range(len(badwordsinthis) - 1, 0, -1):
    crsabmlde[badwordsinthis[i]] = "§"
    del badwordsinthis[i]

#print(crsabmlde)
#print(badwordsinthis)
# downloads = {"B1.txt":"§", "B2.txt":"§", "B3.txt":"§", "B4.txt":"§", "B5.txt":"§", "B6.txt":"§", "B7.txt":"§", "B8.txt":"§", "89.txt":"input daaeeiancad to continue", "B10.txt":"§", "B11.txt":"§", "B12.txt":"§", "B13.txt":"§", "B14.txt":"§", "B15.txt":"§"}
# crsabmlde = {"dab.txt":"§", "dba.txt":"§", "raegt.txt":"input " + seq3 + " to continue", "veli.txt":"§", "roilrebh.txt":"§"}

puzzle2len = random.randint(40, 60)
puzzle2firstpartlen = random.randint(5, 20)
downloads = {"B"+str(i)+".txt":"§" for i in range(puzzle2firstpartlen)}

downloads["8"+str(puzzle2firstpartlen)+".txt"] = "input " + seq2 + " to continue"

for i in range(puzzle2firstpartlen + 1, puzzle2len):
    downloads["B"+str(i)+".txt"] = "§"
#print(downloads)

puzzle4 = str(random.randint(1, 3))
startup_txt = puzzle4 + "~"
puzzle4old = puzzle4
j = 0
for i in range(random.randint(3, 5)):
    puzzle4old = puzzle4
    puzzle4 = ""
    j = 0
    while j < len(puzzle4old):
        oldj = j
        while puzzle4old[j] == puzzle4old[oldj]:
            j += 1
            if j == len(puzzle4old):
                break
        puzzle4 += str(j - oldj)
        puzzle4 += puzzle4old[oldj]
        #j += 1
    startup_txt += puzzle4 + "~"
#print(startup_txt)
startup_files = {"README.txt":startup_txt+"~Find the pattern, then select the next one in \"options\""}
startup_dirs = ["options"]
startup_options = {}
for j in range(random.randint(1, 3)):
    i = ""
    for x in range(len(startup_txt)):
        i += str(random.randint(1, 4))
    startup_options[i+".txt"] = "§"
puzzle4old = puzzle4
puzzle4 = ""
j = 0
while j < len(puzzle4old):
    oldj = j
    while puzzle4old[j] == puzzle4old[oldj]:
        j += 1
        if j == len(puzzle4old):
            break
    puzzle4 += str(j - oldj)
    puzzle4 += puzzle4old[oldj]
startup_options[puzzle4+".txt"] = "input " + seq4 + " to continue"
for j in range(random.randint(1, 3)):
    i = ""
    for x in range(len(puzzle4)):
        i += str(random.randint(1, 4))
    startup_options[i+".txt"] = "§"
startup_values = startup_files
startup_values["options"] = startup_options
#print(startup_values)

filetree = {}
filetree["~"] = startfiles
#print(filetree)
files = iterate_nested_dict(filetree, directory, str)
directories = iterate_nested_dict(filetree, directory, dict)
#print(files)
#print(directories)

helped = False
asked = False
num1, num2 = 0, 0
todo = ""
solved1, solved2, solved3, solved4 = False, False, False, False

#print(seq1)

text = ["01/01 08:00: Successful launch", "01/02 08:00: Food days remaining: 30,", "             all systems correct",
        "01/02 08:00: Food days remaining: 29, ", "             all systems correct",
        "01/02 08:00: Food days remaining: 28, ", "             all systems correct",
        "01/03 08:00: Food days remaining: 27, ", "             all systems correct",
        "01/03 12:53: Asteroid approaching: 1km diameter.", "             Taking evasive maneuvers",
        "01/03 14:27: Unable to avoid asteroid. ", "             Crew in protected stasis",
        "01/03 14:30: Estimated collision time: 15:38", "01/03 15:38: Collision with asteroid, minor damage",
        "01/04 13:32: Crew not out of stasis. Waking Leader", "01/04 13:34: Leader available. Need to start engines.",
        "01/04 13:48: Unable to decompress startup diagram.", "             Decompress keywords scattered in files."]

pygame.display.set_caption("Hermes IV: Automated Logs")

for i in range(len(text)):
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    offset = len(text) - 20
    for j in range(len(text[0:i]), len(text[0:i])-20, -1):
        if not j < 0:
            try:
                screen.blit(font.render(text[j], True, "green"), (10, (j-1-offset)*30))
            except:
                i=i
    pygame.display.update()
    time.sleep(1)

time.sleep(5)

text = ["Initializing...", "Error decompressing file: ", "startup_diagram.png", "Retrying",
            "Error decompressing file: ", "startup_diagram.png", "Failed to decompress file",
            "Without startup, ship will crash in 10 minutes", "Input logs to view logs", "Input help for help",
            "You can use help at any time"]

pygame.display.set_caption("Hermes IV: Main Terminal")
stopped = False
lost = 0

#print(seq1, seq2, seq3, seq4)

while not stopped:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key not in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_BACKSPACE, pygame.K_RETURN]:
                mytext = mytext+event.unicode
            if event.key == pygame.K_BACKSPACE:
                mytext = mytext[0:len(mytext)-1]
            if event.key == pygame.K_RETURN:
                entered = True
            if event.key == pygame.K_DOWN:
                if not currentline >= len(myinputs) - 1:
                    mytext = myinputs[currentline + 1]
                    currentline += 1
                else:
                    mytext = ""
                    if not currentline > len(myinputs) - 1:
                        currentline += 1
            if event.key == pygame.K_UP:
                if not currentline <= 0:
                    mytext = myinputs[currentline - 1]
                    currentline -= 1
    if entered:
        text.append(directory + " % " + mytext)
        if asked:
            asked = False
            if mytext == "1":
                text.append("cd is change directory. Type the")
                text.append("name of a folder after \"cd\" to")
                text.append("change the folder. Type \"cd ..\"")
                text.append("to move back to the previous")
                text.append("folder.")
                text.append("")
                text.append("cat prints out the contents of a file.")
                text.append("Type the name of a file after \"cat\"")
                text.append("to view the contents of a file. Some")
                text.append("files are traps. ONLY WORKS ON .txt FILES.")
                text.append("")
                text.append("type tells you if something is a file")
                text.append("or folder. Type the name of someth-")
                text.append("ing and it will tell you if it is a")
                text.append("file or folder")
                text.append("")
                text.append("\u2193 This is your current directory.")
            elif mytext == "2":
                text.append("open is the same as cat but for .png files")
                text.append("")
                text.append("ls lists out the files and folders in the")
                text.append("current folder.")
                text.append("\u2193 This is your current directory")
            elif mytext == "3":
                if not solved1:
                    text.append("The numbers represent the number of")
                    text.append("dummy letters in between the message.")
                    text.append("For example, 14234 dHehxlEdsLdheLcvqpO")
                    text.append("is hello.")
                    text.append("Once you find the message, type it into")
                    text.append("the command line.")
                elif not solved2:
                    text.append("Each file in the downloads directory")
                    text.append("has a B and a number... except for one.")
                    text.append("Open it to continue.")
                elif not solved3:
                    text.append("The name of the file crsabmlde is simply")
                    text.append("\"scrambled\" but mixed up. Unscramble")
                    text.append("the letters to find what file to open.")
            else:
                asked = True
        elif mytext[0:4] == "cat ":
            t = ""
            if mytext[4:len(mytext)] in files.keys():
                for i in files[mytext[4:len(mytext)]]:
                    if i == "~":
                        text.append(t)
                        t = ""
                    elif i == "§":
                        stopped = True
                        lost = 1
                        filethatkilled = mytext[4:len(mytext)]
                    else:
                        t = t + i
                        if len(t) > 45:
                            text.append(t)
                            t = ""
                text.append(t)
            elif mytext[4:len(mytext)] in directories:
                text.append("cat: " + mytext[4:len(mytext)] + ": Is a folder")
            else:
                text.append("cat: " + mytext[4:len(mytext)] + ": No such file or folder")
        elif mytext == "ls":
            t = ""
            todo = []#"   ".join([",   ".join(directories), "   ".join(files.keys())])
            if directories:
                todo.append("   ".join(directories))
            if files:
                todo.append("   ".join(files.keys()))
            todo = "   ".join(todo)
            for i in todo:
                if i == "~":
                    text.append(t)
                    t = ""
                else:
                    t += i
                    if len(t) > 35:
                        text.append(t)
                        t = ""
            text.append(t)
            t = ""
        elif mytext == "pwd":
            text.append(directory)
        elif mytext[0:3] == "cd ":
            if mytext[3:len(mytext)] == ".." and directory != "~":
                directory = pastdirectory
            elif mytext[3:len(mytext)] in directories:
                pastdirectory = directory
                directory = mytext[3:len(mytext)]
            else:
                text.append("cd: no such file or folder: " + mytext[3:len(mytext)])
            # if directory == "decoders":
            #     directories = decoderdirs
            #     files = decodersfiles
            # if directory == "downloads":
            #     directories = []
            #     files = downloads
            # elif directory == "~":
            #     directories = filetree["~"]
            #     files = startfiles
            # elif directory == "crsabmlde":
            #     directories = []
            #     files = crsabmlde
            # elif directory == "startup_values":
            #     directories = startup_dirs
            #     files = startup_files
            # elif directory == "options":
            #     directories = []
            #     files = startup_options
            files = iterate_nested_dict(filetree, directory, str)
            directories = iterate_nested_dict(filetree, directory, dict)
            #print(files)
        elif mytext[0:5] == "open ":
            if mytext[5:len(mytext)] == "startup_diagram.png" and directory == "~":
                if solved1:
                    screen.blit(img1, (0, 0))
                else:
                    screen.blit(badimg1, (0, 0))
                if solved2:
                    screen.blit(img2, (300, 0))
                else:
                    screen.blit(badimg2, (300, 0))
                if solved3:
                    screen.blit(img3, (0, 300))
                else:
                    screen.blit(badimg3, (0, 300))
                if solved4:
                    screen.blit(img4, (300, 300))
                else:
                    screen.blit(badimg4, (300, 300))
                pygame.display.update()
                time.sleep(5)
        elif mytext == "help":
            text.append("What would you like help with?")
            text.append("1) commands")
            text.append("2) commands (cont)")
            text.append("3) puzzles")
            text.append("type the number of the item.")
            asked = True
        elif mytext[0:5] == "type ":
            if mytext[5:len(mytext)] in directories:
                text.append("type: is a directory: " + mytext[5:len(mytext)])
            elif mytext[5:len(mytext)] in files.keys():
                text.append("type: is a file: " + mytext[5:len(mytext)])
            else:
                text.append("type: no such file or directory: " + mytext[5:len(mytext)])
        elif mytext == seq1:
            if not solved1:
                solved1 = True
                filetree["~"]["downloads"] = downloads
                files = iterate_nested_dict(filetree, directory, str)
                directories = iterate_nested_dict(filetree, directory, dict)
                visible = text
                percent = 0
                loading = ""
                for b in range(30):
                    screen.fill("black")
                    percent += 1
                    loading = "["
                    for v in range(30):
                        if v < percent:
                            loading += "#"
                        else:
                            loading += "-"
                    loading += "]   " + str(round(percent/30*100)) + "%"
                    text = []
                    for z in range(len(visible)):
                        text.append(visible[z])
                    text.append(loading)
                    offset = len(text) - 20
                    for i in range(len(text), len(text) - 20, -1):
                        if not i < 0:
                            try:
                                screen.blit(font.render(text[i], True, "green"), (10, (i - 1 - offset) * 30))
                            except:
                                i = i
                    pygame.display.update()
                    time.sleep(0.25)
                text.append("First quadrant decoded successfully!")
                text.append("Open startup_diagram.png to see changes.")
        elif mytext == seq2:
            if not solved2:
                solved2 = True
                filetree["~"]["crsabmlde"] = crsabmlde
                files = iterate_nested_dict(filetree, directory, str)
                directories = iterate_nested_dict(filetree, directory, dict)
                visible = text
                percent = 0
                loading = ""
                for b in range(30):
                    screen.fill("black")
                    percent += 1
                    loading = "["
                    for v in range(30):
                        if v < percent:
                            loading += "#"
                        else:
                            loading += "-"
                    loading += "]   " + str(round(percent/30*100)) + "%"
                    text = []
                    for z in range(len(visible)):
                        text.append(visible[z])
                    text.append(loading)
                    offset = len(text) - 20
                    for i in range(len(text), len(text) - 20, -1):
                        if not i < 0:
                            try:
                                screen.blit(font.render(text[i], True, "green"), (10, (i - 1 - offset) * 30))
                            except:
                                i = i
                    pygame.display.update()
                    time.sleep(0.25)
                text.append("Second quadrant decoded successfully")
                text.append("Go to home directory and see changes")
        elif mytext == seq3:
            if not solved3:
                solved3 = True
                visible = text
                percent = 0
                loading = ""
                startdirs.append("startup_values")
                filetree["~"]["startup_values"] = startup_values
                #print(filetree)
                files = iterate_nested_dict(filetree, directory, str)
                directories = iterate_nested_dict(filetree, directory, dict)
                for b in range(30):
                    screen.fill("black")
                    percent += 1
                    loading = "["
                    for v in range(30):
                        if v < percent:
                            loading += "#"
                        else:
                            loading += "-"
                    loading += "]   " + str(round(percent/30*100)) + "%"
                    text = []
                    for z in range(len(visible)):
                        text.append(visible[z])
                    text.append(loading)
                    offset = len(text) - 20
                    for i in range(len(text), len(text) - 20, -1):
                        if not i < 0:
                            try:
                                screen.blit(font.render(text[i], True, "green"), (10, (i - 1 - offset) * 30))
                            except:
                                i = i
                    pygame.display.update()
                    time.sleep(0.25)
                text.append("Third quadrant decoded successfully")
                text.append("Go to home directory and see changes")
        elif mytext == seq4:
            if not solved4:
                solved4 = True
                visible = text
                percent = 0
                loading = ""
                for b in range(30):
                    screen.fill("black")
                    percent += 1
                    loading = "["
                    for v in range(30):
                        if v < percent:
                            loading += "#"
                        else:
                            loading += "-"
                    loading += "]   " + str(round(percent / 30 * 100)) + "%"
                    text = []
                    for z in range(len(visible)):
                        text.append(visible[z])
                    text.append(loading)
                    offset = len(text) - 20
                    for i in range(len(text), len(text) - 20, -1):
                        if not i < 0:
                            try:
                                screen.blit(font.render(text[i], True, "green"), (10, (i - 1 - offset) * 30))
                            except:
                                i = i
                    pygame.display.update()
                    time.sleep(0.25)
                text.append("Fourth quadrant decoded successfully")
                text.append("All quadrants decoded successfully!")
                text.append("Stopping Main Terminal view software.")
                stopped = True
        elif mytext == "logs":
            text.append("01/01 08:00: Successful launch")
            text.append("01/02 08:00: Food days remaining: 30,")
            text.append("             all systems correct")
            text.append("01/02 08:00: Food days remaining: 29, ")
            text.append("             all systems correct")
            text.append("01/02 08:00: Food days remaining: 28, ")
            text.append("             all systems correct")
            text.append("01/03 08:00: Food days remaining: 27")
            text.append("             all systems correct")
            text.append("01/03 12:53: Asteroid approaching: 1km diameter.")
            text.append("             Taking evasive maneuvers")
            text.append("01/03 14:27: Unable to avoid asteroid. ")
            text.append("Crew in protected stasis")
            text.append("01/03 14:30: Estimated collision time: 15:38")
            text.append("01/03 15:38: Collision with asteroid, minor damage")
            text.append("01/04 13:32: Crew not out of stasis. Waking Leader")
            text.append("01/04 13:34: Leader available. Need to start engines.")
            text.append("01/04 13:48: Unable to decode startup diagram.")
            text.append("             Decoders scattered in files.")
        else:
            text.append("zsh: command not found: " + mytext)
        myinputs.append(mytext)
        currentline += 1
        mytext = ""
        entered = False
    offset = len(text) - 20
    for i in range(len(text), len(text)-20, -1):
        if not i < 0:
            try:
                screen.blit(font.render(text[i], True, "green"), (10, (i-1-offset)*30))
            except:
                i=i
    screen.blit(font.render(directory + " % " + mytext, True, "green"), (10, (len(text)-1 - offset)*30))
    cursorrect = cursor.get_rect()
    cursorrect.x = ((len(directory + " % " + mytext)+1)*15)
    cursorrect.y = (len(text)-1 - offset)*30
    cursoroutlinerect = cursoroutline.get_rect(center=cursorrect.center)
    ticks = pygame.time.get_ticks()
    if ticks % 1200 > 600:
        cursoroutline.fill("green")
    else:
        cursoroutline.fill("black")
    screen.blit(cursor, cursorrect)
    screen.blit(cursoroutline, cursoroutlinerect)
    clock.tick(60)
    pygame.display.update()

static = pygame.transform.scale_by(pygame.image.load("staticnoise.jpg").convert_alpha(), 4)
pygame.display.set_caption("Hermes IV: Automated Logs")
if lost == 1:
    text = ["01/04 15:02: File opened: " + filethatkilled, "01/04 15:03: Unable to close file: " + filethatkilled, "01/04 15:06: code red: " + filethatkilled + " contains malware",
            "01/05 08:00: Unable to close file: " + filethatkilled, "01/06 15:52: " + filethatkilled + " malware reached mainframe", "01/06 16:03: Irreversible damage to mainframe. Abort", "ERR•¶§∞¢¶•º¶§¶§∞∞§¢£¢∞£ABOrt©˙∆©ƒ¥˙∆√ƒ©∆©",
            "∑®´ƒ©∫√©ç†˚©˙…˚˙ERR˙¨∆˙¨¥OR©˙ƒ†¥ƒç®∂çƒ∂ƒƒ", "∆˚˙˚©ƒ©ƒ∆µ˜∫√çƒ≈∂†ƒ˙∆∫˙√∆©çƒ®†∂®ß®†", "n∆˚˙∫¥¥†∂©∆ƒ¥©˙ø¨¶•£™£¢£¶ª•º••ª§¶®∞§ƒƒ©∂√√√√µ√º"]
    for i in range(len(text)):
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        offset = len(text) - 20
        for j in range(len(text[0:i]), len(text[0:i]) - 20, -1):
            if not j < 0:
                try:
                    screen.blit(font.render(text[j], True, "green"), (10, (j - 1 - offset) * 30))
                except:
                    i = i
        pygame.display.update()
        time.sleep(2)

    for j in range(1000):
        screen.fill("black")
        offset = len(text) - 20
        for i in range(len(text), len(text) - 20, -1):
            if not i < 0:
                try:
                    screen.blit(font.render(text[i], True, "green"), (10, (i - 1 - offset) * 30))
                except:
                    i = i
        if random.randint(0, j) > 60:
        # static.set_alpha(i)
            static = pygame.transform.rotate(static, 90)
            screen.blit(static, (0-random.randint(0, 50), 0-random.randint(0, 50)))
        pygame.display.update()
    for i in range(100):
        #if random.randint(0, i) > 50:
        # static.set_alpha(i)
        static = pygame.transform.rotate(static, 90)
        screen.blit(static, (0-random.randint(0, 50), 0-random.randint(0, 50)))
        pygame.display.update()
else:
    text = ["01/04 15:02: All quadrants decoded successfully", "01/04 15:04: Initialization sequence entered",
            "01/04 15:05: Engine online, all systems go", "01/04 15:06: Course set to: original destination: ",
            "                           Proxima Centauri b"]
    for i in range(len(text)):
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        offset = len(text) - 20
        for j in range(len(text[0:i]), len(text[0:i]) - 20, -1):
            if not j < 0:
                try:
                    screen.blit(font.render(text[j], True, "green"), (10, (j - 1 - offset) * 30))
                except:
                    i = i
        pygame.display.update()
        time.sleep(2)
    time.sleep(3)
    ship = pygame.transform.scale_by(pygame.image.load("ship.png").convert_alpha(), 0.1)
    shiprect = ship.get_rect()
    shipoff = pygame.transform.scale_by(pygame.image.load("shipoff.png").convert_alpha(), 0.09)
    shipoffrect = shipoff.get_rect(midbottom=(400, 610))
    bg = pygame.transform.scale_by(pygame.image.load("stars.jpeg"), 2)
    for i in range(400):
        screen.blit(bg, (0, 0))
        screen.blit(shipoff, shipoffrect)
        clock.tick(120)
        pygame.display.update()
    for i in range(620 * 10):
        screen.blit(bg, (0, 0))
        shiprect.midbottom = (400, 620 - 5 * (i * i) / 3000)
        screen.blit(ship, shiprect)
        clock.tick(120)
        pygame.display.update()
