#!/usr/bin/env python3

from pin_table_common import *
import pin_table_gen

pin_definitions = {
    'GND': {'type': 'gnd'},
    '3V3': {'type': '3v3'},
    '5V':  {'type': '5v'},
    'BAT': {'type': 'bat'},
    'HPWR': {'type': 'hpwr'},

    # ADC pins
    'G35': {'type': 'input_only', 'usage': 'ADC' , 'usage_type': 'ADC'},
    'G36': {'type': 'input_only', 'usage': 'ADC' , 'usage_type': 'ADC'},
    # DAC pins
    'G25': {'type': 'normal',     'usage': 'DAC/SPK' , 'usage_type': 'DAC'},
    'G26': {'type': 'normal',     'usage': 'DAC'     , 'usage_type': 'DAC'},
    # SPI pins
    'G23': {'type': 'normal',     'usage': 'MOSI', 'usage_type': 'SPI'},
    'G19': {'type': 'normal',     'usage': 'MISO', 'usage_type': 'SPI'},
    'G18': {'type': 'normal',     'usage': 'SCK',  'usage_type': 'SPI'},
    # UART0 pins
    'G3':  {'type': 'normal',     'usage': 'RXD0', 'usage_type': 'UART'},
    'G1':  {'type': 'normal',     'usage': 'TXD0', 'usage_type': 'UART'},
    # UART2 pins
    'G16': {'type': 'normal',     'usage': 'RXD2', 'usage_type': 'UART'},
    'G17': {'type': 'normal',     'usage': 'TXD2', 'usage_type': 'UART'},
    # I2C pins (internal)
    'G21': {'type': 'normal',     'usage': 'SDA',  'usage_type': 'I2C'},
    'G22': {'type': 'normal',     'usage': 'SCL',  'usage_type': 'I2C'},
    # GPIO pins
    'G2':  {'type': 'normal',     'usage': 'GPIO', 'usage_type': 'GPIO'},
    'G5':  {'type': 'normal',     'usage': 'GPIO', 'usage_type': 'GPIO'},
    # I2S pins
    'G12': {'type': 'normal',     'usage': 'I2S SK', 'usage_type': 'I2S'},
    'G13': {'type': 'normal',     'usage': 'I2S WS', 'usage_type': 'I2S'},
    'G15': {'type': 'normal',     'usage': 'I2SOUT', 'usage_type': 'I2S'},
    'G0':  {'type': 'normal',     'usage': 'I2S MK', 'usage_type': 'I2S'},
    'G34': {'type': 'normal',     'usage': 'I2S IN', 'usage_type': 'I2S'},

    'EN':  {'type': 'misc', 'usage': 'RST', 'usage_type': 'RST'},
}

pin_map = (
    ('GND',  'G35'),
    ('GND',  'G36'),
    ('GND',  'EN'),
    ('G23',  'G25'),
    ('G19',  'G26'),
    ('G18',  '3V3'),
    ('G3',   'G1'),
    ('G16',  'G17'),
    ('G21',  'G22'),
    ('G2',   'G5'),
    ('G12',  'G13'),
    ('G15',  'G0'),
    ('HPWR', 'G34'),
    ('HPWR', '5V'),
    ('HPWR', 'BAT'),
)

drawing = pin_table_gen.generate_pin_map_svg(pin_map, pin_definitions, pin_type_colors, usage_type_colors)
drawing.saveas('pindef_core.svg')