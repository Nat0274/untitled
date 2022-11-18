def on_forever():   
    def on_pin_pressed_p0():
    
        basic.show_leds("""
        . # . # .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        """)
    input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)
    def on_gesture_shake2():
        basic.show_leds("""
        . # . # .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        """)
    input.on_gesture(Gesture.SHAKE, on_gesture_shake2)    
basic.forever(on_forever)