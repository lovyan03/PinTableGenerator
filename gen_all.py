#!/usr/bin/env python3

from pin_table_gen import generate_pin_map_svg_from_json
import os.path

targets = {
    'core_bus':       { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'core2_bus':      { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'coreink_bus':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'core_porta':     { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'core_portb':     { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'core_portc':     { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'core_portd':     { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'core_porte':     { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'core2_porta':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'core2_portb':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'core2_portc':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'core2_portd':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'core2_porte':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'paper_porta':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'paper_portb':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'paper_portc':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'station_porta':  { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'station_portb1': { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'station_portb2': { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'station_portc1': { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'station_portc2': { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'stickc_porta':   { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'atom_porta':     { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'atom_s3_porta':  { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'stickc_hat':     { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'stickcplus_hat': { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'coreink_hat':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'stamppico_bus':  { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'stampc3_bus':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'stampc3u_bus':   { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'atom_u':         { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': True , 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'atom_lite':      { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'atom_matrix':    { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'atom_echo':      { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'atom_psram':     { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
    'atom_s3':        { 'colors': 'pin_table_colors', 'options': {'span_pin_name_without_usage': False, 'row_height': 24, 'pin_name_column_width': 24, 'usage_column_width': 40 }},
}

for target_name, target_defs in targets.items():
    pin_def_path = os.path.join('defs', f'pin_def_{target_name}.jsonc')
    color_def_path  = os.path.join('defs', f'{target_defs["colors"]}.jsonc')
    drawing = generate_pin_map_svg_from_json(pin_def_path, color_def_path, **target_defs['options'])
    output_path = os.path.join('outputs', f'pin_def_{target_name}.svg')
    drawing.saveas(output_path)
