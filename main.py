# walk press a
def on_button_pressed_a():
    global num_balls
    num_balls += 1
    if num_balls >= 4:
        num_balls = 0
        basic.show_string('WALK', speed)
    else:
        basic.show_string("BALL", speed)
    basic.clear_screen()

input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global num_strikes, num_outs, num_balls, offense
    num_strikes += 1
    if num_strikes >= 3:
        num_strikes = 0
        num_outs += 1
        basic.show_string("OUT", speed)
        # 3 outs, switch team, clear all the variables
        if num_outs >= 3:
            num_outs = 0
            num_balls = 0
            num_strikes = 0
            basic.show_string("SWITCH", speed)
            # switch team
            offense ^= 1
    else:
        basic.show_string("STRIKE", speed)
    basic.clear_screen()
    
input.on_button_pressed(Button.B, on_button_pressed_b)

# add score for the attacking team
def on_button_pressed_ab():
    global a_score, b_score
    if offense == 0:
        a_score += 1
        basic.show_string("A",59)
        basic.show_number(a_score, 59)
    if offense == 1:
        b_score += 1
        basic.show_string("B", 59)
        basic.show_number(b_score, 59)
    basic.clear_screen()

input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

num_balls = 0
num_strikes = 0
num_outs = 0
b_score = 0
a_score = 0

# offense 0 means a is the attacking team, 1 means b is the attacking team
offense = 0

speed = 10