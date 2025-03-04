import pygame as game
import random as rand

def run():
    """Main game code"""
    sentencedoc = open('sentences.txt', 'r', encoding='utf-8')
    sentences = sentencedoc.readlines()
    sentences = [line.lower().strip() for line in sentences]

    screen = game.display.set_mode((1000, 500))
    target = sentences[rand.randint(0,len(sentences)-1)]
    lettercounter = 0
    t1 = 0
    timerstart = False
    targetlist = [letter for letter in target]
    maxlen = len(targetlist)
    done = False
    game.display.set_caption('ENGRtype')
    exit = False

    font = game.font.SysFont('Consolas', 15)
    titlefont = game.font.SysFont('Consolas', 32)
    statfont = game.font.SysFont('Consolas', 22)
    bgcolor = (0, 0, 0)
    carcolor = (20, 200, 100)
    lines = []
    for i in range(maxlen//2):
        x = 75*i
        lines.append(game.Rect(x, screen.get_height()/2, 30, 6))
        if i == maxlen//2-1:
            lines.append(game.Rect(x + 80, screen.get_height()/2 - 50, 30, 100))
    while not exit: 
        for event in game.event.get(): 
            if event.type == game.QUIT: 
                exit = True
            if event.type == game.KEYDOWN:
                try:
                    print(event.key)
                    if event.key == game.K_RETURN:
                        run()
                    if keycodedict[event.key] == targetlist[0]:
                        if not timerstart:
                            t1 = game.time.get_ticks()
                            timerstart = True

                        del targetlist[0]

                        target = ''.join(targetlist)

                        lettercounter += 1
                        movelines(lines)
                    
                        
                        
                except Exception as e:
                    print('unsupported input :(')
        screen.fill(bgcolor)

        if len(targetlist) == 0:
            win = titlefont.render(f'done: {elapsedtime(t1):.0f}s with {calcwpm(lettercounter,t1):.0f} wpm', True, (255,255,255))
            screen.blit(win, (screen.get_width()/2 - win.get_width()/2, screen.get_height()/2- win.get_height()/2))
            if done == False:
                for line in lines:
                    game.draw.rect(screen, (255,255,255), line)
                game.draw.rect(screen, carcolor, car)
                game.display.update()
                done = True


        words = font.render(target, True, (255, 255, 255))
        title = titlefont.render('engrtype', True, (255, 255, 255))
        car = game.Rect(15, (screen.get_height()/2) - 45/2, 75, 45)
        instructions1 = font.render('Start typing text to begin', True, (255,255,255))
        instructions2 = font.render('Press ENTER to restart', True, (255,255,255))
                
        
        screen.blit(words, (screen.get_width() // 2 - words.get_width() // 2, screen.get_height() // 2 - (words.get_height() // 2 - 100)))
        screen.blit(checkwpm(timerstart, lettercounter, statfont,t1), (5, 0))
        screen.blit(checktime(timerstart,statfont,t1), (5, 20))
        screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, screen.get_height() // 2 - (title.get_height() // 2 + 200)))
        screen.blit(instructions1, (screen.get_width()-instructions1.get_width(),0))
        screen.blit(instructions2, (screen.get_width()-instructions2.get_width(),instructions1.get_height()))

        for line in lines:
            game.draw.rect(screen, (255,255,255), line)
        game.draw.rect(screen, carcolor, car)

        
        
        if done == False:
            game.display.update()

def elapsedtime(start):
    """Returns current elapsed time in seconds"""
    return ((game.time.get_ticks() - start)+.001) / 1000  
def movelines(lines):
    """Moves all streetlines to the left"""
    for line in lines:
        line.x -= 36
def checkwpm(timerstart, lettercounter, font, t1):
    """Displays real-time WPM when user starts typing, 0 otherwise"""
    if timerstart:
        
        wpm_text = font.render(f'WPM: {calcwpm(lettercounter,t1):.0f}', True, (255, 255, 255))
    else:
        wpm_text = font.render('WPM: 0', True, (255, 255, 255))
    return wpm_text
def calcwpm(lettercounter,t1):
    """Calculates WPM"""
    elapsed_seconds = elapsedtime(t1)
    wpm = (lettercounter / 5) / (elapsed_seconds / 60)
    return wpm
def checktime(timerstart, font, t1):
    """Displays real-time WPM when user starts typing, 0 otherwise"""
    if timerstart:
        elapsed_seconds = elapsedtime(t1)
        time = elapsed_seconds
        time_text = font.render(f'WPM: {time:.0f}s', True, (255, 255, 255))
    else:
        time_text = font.render('time: 0s', True, (255, 255, 255))
    return time_text

game.init()
keycodedict = {
    97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g',
    104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n',
    111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u',
    118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z', 48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6',
    55: '7', 56: '8', 57: '9', 32: ' ', 33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&',
    39: "'", 40: '(', 41: ')', 42: '*', 43: '+', 44: ',', 45: '-',
    46: '.', 47: '/', 58: ':', 59: ';', 60: '<', 61: '=', 62: '>',
    63: '?', 64: '@', 91: '[', 92: '\\', 93: ']', 94: '^', 95: '_',
    96: '`', 123: '{', 124: '|', 125: '}', 126: '~', 1073742049:''
}

run()
