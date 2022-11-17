def on_button_pressed_a():
    basic.show_leds("""
    . # . # .
    . # . # .
    . . . . .
    . # # # .
    # . . . #
    """)
    input.on_button_pressed(Button.A, on_button_pressed_a)
    def on_button_pressed_a2():
        basic.show_leds("""
        . # . # .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        """)
        input.on_button_pressed(on_button_pressed_b, on_button_pressed_a2)
