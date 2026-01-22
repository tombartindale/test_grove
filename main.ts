basic.forever(function on_forever() {
    
})
let strip = grove.connectToWS2813Strip(DigitalPin.P0, 16)
strip.showRainbow(1, 360)
