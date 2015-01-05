#!/usr/bin/env python
# encoding: utf-8

import random

def color_variant(brightness_offset=1):
    hex_color = "#%06x" % random.randint(0,0xFFFFFF)
    """ takes a color like #87c95f and produces a lighter or darker variant """
    if len(hex_color) != 7:
            raise Exception("Passed %s into color_variant(), needs to be in #87c95f format." % hex_color)
    rgb_hex = [hex_color[x:x+2] for x in [1, 3, 5]]
    new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]
    new_rgb_int = [min([255, max([0, i])]) for i in new_rgb_int] # make sure new values are between 0 and 255
    # hex() produces "0x88", we want just "88"
    return [hex_color, "#" + "".join([hex(i)[2:] for i in new_rgb_int])]
