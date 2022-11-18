basic.forever(function on_forever() {
    input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
        basic.showLeds(`
        . # . # .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        `)
    })
    input.onGesture(Gesture.Shake, function on_gesture_shake2() {
        basic.showLeds(`
        . # . # .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        `)
    })
})
