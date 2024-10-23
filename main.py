@namespace
class SpriteKind:
    obj = SpriteKind.create()

def on_up_pressed():
    if True:
        animation.run_image_animation(mySprite,
            assets.animation("""
                spr_jogadorcostas
            """),
            200,
            True)
    else:
        animation.run_image_animation(mySprite,
            assets.animation("""
                spr_jogadorparadocostas
            """),
            200,
            False)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_overlap(sprite3, otherSprite3):
    controller.move_sprite(mySprite, 140, 140)
    sprites.destroy(mySprite2)
sprites.on_overlap(SpriteKind.player, SpriteKind.obj, on_on_overlap)

def on_left_pressed():
    animation.run_image_animation(mySprite,
        assets.animation("""
            spr_jogadoresquerda
        """),
        100,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_overlap2(sprite32, otherSprite32):
    if True:
        sprites.destroy(mySprite)
        game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        assets.animation("""
            spr_jogadordireita
        """),
        100,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    animation.run_image_animation(mySprite,
        assets.animation("""
            spr_jogadorfrente
        """),
        200,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_on_overlap3(sprite2, otherSprite2):
    global Rango
    info.change_score_by(1)
    sprites.destroy(Rango)
    if info.score() == 20:
        game.game_over(True)
    else:
        Rango = sprites.create(assets.image("""
            spr_sorvete2
        """), SpriteKind.food)
        Rango.set_position(randint(0, scene.screen_width()),
            randint(0, scene.screen_height()))
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap3)

mySprite: Sprite = None
Rango: Sprite = None
mySprite2: Sprite = None
game.show_long_text("BEM VINDO, PRESSIONE ESPAÇO PARA COMEÇAR",
    DialogLayout.CENTER)
game.show_long_text("REGRAS: COLETAR 20 SORVETES; SE O INIMIGO ATINGIR VOCÊ, É GAME OVER; A GEMA AZUL AUMENTA SUA VELOCIDADE.",
    DialogLayout.FULL)
classe = game.ask_for_string("Qual seu nome?")
game.splash("Bem vindo, " + classe)
scene.set_background_image(assets.image("""
    spr_cenario
"""))
mySprite2 = sprites.create(assets.image("""
    spr_powerup
"""), SpriteKind.obj)
Rango = sprites.create(assets.image("""
    spr_sorvete
"""), SpriteKind.food)
mySprite = sprites.create(assets.image("""
    spr_jogador
"""), SpriteKind.player)
myEnemy = sprites.create(assets.image("""
    spr_inimigo
"""), SpriteKind.enemy)
myEnemy.follow(mySprite, 70)
animation.run_image_animation(myEnemy,
    assets.animation("""
        spr_inimigo
    """),
    200,
    True)
myEnemy.set_position(6, 5)
mySprite2.set_position(randint(0, scene.screen_width()),
    randint(0, scene.screen_height()))
controller.move_sprite(mySprite, 120, 120)
mySprite.set_stay_in_screen(True)
info.set_score(0)