/**
 * offense 0 means a is the attacking team, 1 means b is the attacking team
 */
// walk press a
input.onButtonPressed(Button.A, function () {
    num_balls += 1
    if (num_balls >= 4) {
        num_balls = 0
        basic.showString("WALK", speed)
    } else {
        basic.showString("BALL", speed)
    }
    basic.clearScreen()
})
// add score for the attacking team
input.onButtonPressed(Button.AB, function () {
    if (offense == 0) {
        a_score += 1
        basic.showString("A", 59)
basic.showNumber(a_score, 59)
    }
    if (offense == 1) {
        b_score += 1
        basic.showString("B", 59)
basic.showNumber(b_score, 59)
    }
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    num_strikes += 1
    if (num_strikes >= 3) {
        num_strikes = 0
        num_outs += 1
        basic.showString("OUT", speed)
// 3 outs, switch team, clear all the variables
        if (num_outs >= 3) {
            num_outs = 0
            num_balls = 0
            num_strikes = 0
            basic.showString("SWITCH", speed)
offense ^= 1
        }
    } else {
        basic.showString("STRIKE", speed)
    }
    basic.clearScreen()
})
input.onGesture(Gesture.Shake, function () {
	
})
let num_outs = 0
let num_strikes = 0
let num_balls = 0
let offense = 0
let a_score = 0
let b_score = 0
let speed = 10
