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
