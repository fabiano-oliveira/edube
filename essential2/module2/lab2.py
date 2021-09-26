"""
You've surely seen a seven-segment display.

It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit using a subset of seven segments. If you still don't know what it is, refer to the following Wikipedia article.

Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.
"""

d1 = """  #
  #
  #
  #
  #"""
d2 = """
###
  #
###
#  
###"""
d3 = """
###
  #
###
  #
###"""
d4 = """
# #
# #
###
  #
  #"""
d5 = """
###
#  
###
  #
###"""
d6 = """
###
#  
###
# #
###"""
d7 = """
###
  #
  #
  #
  #"""
d8 = """
###
# #
###
# #
###"""
d9 = """
###
# #
###
  #
###"""
d0 = """
###
# #
# #
# #
###"""
led_sep = "  "
leds = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]
leds = [d.strip("\n").split(sep="\n") for d in leds]

def parse_to_led(digit): 
    """
    Converte o digit em led
    """
    d = int(digit)
    return leds[d]

def join_leds(leds):
    """
    Junto todos os leds em um único display
    """
    display = ""

    for line in range(5):
        for led in leds: 
            display += led[line] + led_sep
        display += "\n"
    return display
    

def display_numbers(n):
    """
    Converte o número n em uma sequência de digitos e converte cada digito em um led
    """
    digits = str(n)
    leds = [parse_to_led(d) for d in digits]
    display = join_leds(leds)
    print(display)

display_numbers(123)
display_numbers(9081726354)
#print(leds[1])