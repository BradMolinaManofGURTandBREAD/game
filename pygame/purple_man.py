character = Actor('character')
character.pos = 100, 50

WIDTH = 500
HEIGHT = 300

def draw():
    screen.fill((255, 0, 0))
    character.draw()

def update():
    character.left = character.left + 2
    if character.left > WIDTH:
        character.right = 0

def reset_character():
    character.image = 'character'

def on_mouse_down(pos):
    if character.collidepoint(pos):
        character.image = 'character_clicked'
        clock.schedule_unique(reset_character, 1.0)
        print('never try that again')
    else:
        print('yuh')



