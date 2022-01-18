#!/usr/bin/env python3

from pin_table_gen import generate_pin_map_svg_from_json
import os.path

targets = {
    'core_bus':       { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 60 }},
    'core2_bus':      { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 60 }},
    'coreink_bus':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 60 }},
    'stamppico_bus':  { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 60 }},
    'core_porta':     { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'core_portb':     { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'core_portc':     { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'core_portd':     { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'core_porte':     { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'core2_porta':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'core2_portb':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'core2_portc':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'core2_portd':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'core2_porte':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'paper_porta':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'paper_portb':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'paper_portc':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'station_porta':  { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'station_portb1': { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'station_portb2': { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'station_portc1': { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'station_portc2': { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'stickc_porta':   { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'atom_porta':     { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'stickc_hat':     { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'stickcplus_hat': { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'coreink_hat':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'atom_u':         { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'atom_lite':      { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'atom_matrix':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'atom_echo':      { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
    'atom_psram':     { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 28, 'pin_name_column_width': 36, 'usage_column_width': 52 }},
}

for target_name, target_defs in targets.items():
    pin_def_path = os.path.join('defs', f'pin_def_{target_name}.jsonc')
    color_def_path  = os.path.join('defs', f'{target_defs["colors"]}.jsonc')
    drawing = generate_pin_map_svg_from_json(pin_def_path, color_def_path, **target_defs['options'])
    output_path = os.path.join('outputs', f'pin_def_{target_name}.svg')
    drawing.saveas(output_path)
