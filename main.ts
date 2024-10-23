namespace SpriteKind {
    export const obj = SpriteKind.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (true) {
        animation.runImageAnimation(
        mySprite,
        assets.animation`spr_jogadorcostas`,
        200,
        true
        )
    } else {
        animation.runImageAnimation(
        mySprite,
        assets.animation`spr_jogadorparadocostas`,
        200,
        false
        )
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite32, otherSprite32) {
    if (true) {
        sprites.destroy(mySprite)
        game.gameOver(false)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.obj, function (sprite3, otherSprite3) {
    controller.moveSprite(mySprite, 140, 140)
    sprites.destroy(mySprite2)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    assets.animation`spr_jogadoresquerda`,
    100,
    true
    )
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    assets.animation`spr_jogadordireita`,
    100,
    true
    )
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    assets.animation`spr_jogadorfrente`,
    200,
    true
    )
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite2, otherSprite2) {
    info.changeScoreBy(1)
    sprites.destroy(Rango)
    if (info.score() == 20) {
        game.gameOver(true)
    } else {
        Rango = sprites.create(assets.image`spr_sorvete2`, SpriteKind.Food)
        Rango.setPosition(randint(0, scene.screenWidth()), randint(0, scene.screenHeight()))
    }
})
let mySprite: Sprite = null
let Rango: Sprite = null
let mySprite2: Sprite = null
game.showLongText("BEM VINDO, PRESSIONE ESPAÇO PARA COMEÇAR", DialogLayout.Center)
game.showLongText("REGRAS: COLETAR 20 SORVETES; SE O INIMIGO ATINGIR VOCÊ, É GAME OVER; A GEMA AZUL AUMENTA SUA VELOCIDADE.", DialogLayout.Full)
let classe = game.askForString("Qual seu nome?")
game.splash("Bem vindo, " + classe)
scene.setBackgroundImage(assets.image`spr_cenario`)
mySprite2 = sprites.create(assets.image`spr_powerup`, SpriteKind.obj)
Rango = sprites.create(assets.image`spr_sorvete`, SpriteKind.Food)
mySprite = sprites.create(assets.image`spr_jogador`, SpriteKind.Player)
let myEnemy = sprites.create(assets.image`spr_inimigo`, SpriteKind.Enemy)
myEnemy.follow(mySprite, 70)
animation.runImageAnimation(
myEnemy,
assets.animation`spr_inimigo`,
200,
true
)
myEnemy.setPosition(6, 5)
mySprite2.setPosition(randint(0, scene.screenWidth()), randint(0, scene.screenHeight()))
controller.moveSprite(mySprite, 120, 120)
mySprite.setStayInScreen(true)
info.setScore(0)
