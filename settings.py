# game setup
WIDTH     = 1280
HEIGHT    = 720
FPS       = 60
TILESIZE  = 64

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../Projet_Python_Zelda/graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui color
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'


#weapons

weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': '../Projet_Python_Zelda/graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 35, 'graphic': '../Projet_Python_Zelda/graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 25, 'graphic': '../Projet_Python_Zelda/graphics/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic': '../Projet_Python_Zelda/graphics/weapons/rapier/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'graphic': '../Projet_Python_Zelda/graphics/weapons/sai/full.png'},
}

WORLD_MAP = [
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ','X',' ',' ',' ',' ',' ','X','X','X','X','X',' ',' ',' ',' ',' ','X'],
['X',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ','X'],
['X',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ','X'],
['X',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ','X'],
['X',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ','X'],
['X',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ','X'],
['X',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ','X'],
['X',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ','X'],
['X',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ','X',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ','X','X','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
]