def on_forever():
    pass
basic.forever(on_forever)

strip = grove.connect_to_ws2813_strip(DigitalPin.P0, 16)

strip.show_rainbow(1, 360)