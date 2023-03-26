#!/usr/bin/env python3
"""Randomly changes iTerm color schemes on launch.

**Author: Jonathan Delgado**

"""
#======================== Imports ========================#
import os
import sys
import iterm2
import random
from pathlib import Path
#--- Custom imports ---#
from itermlink.tools.console import *
import itermlink
#======================== Fields ========================#
_PRESETS_FNAME = Path(__file__).parent / 'saved_presets.txt'
#======================== Functions ========================#


def _init_args():
    """ Elementary arg parser. """
    return {
        'auto': '--auto' in sys.argv,
        'del': '--del' in sys.argv,
        'clear': '--clear' in sys.argv,
        'num': '--num' in sys.argv,
    }


def save_preset(preset_name):
    """ Saves the preset to a list of liked presets. """
    with open(_PRESETS_FNAME, 'a') as f:
        f.write(preset_name + '\n')


async def get_presets_to_try(connection):
    """ Gets the color presets that haven't been used yet. """
    preset_names = set(await itermlink.get_presets(connection))
    # Load the approved presets
    with open(_PRESETS_FNAME, 'r') as f:
        saved_preset_names = set(f.read().splitlines())

    return list(preset_names - saved_preset_names)


async def random_preset(connection):
    # Get the preset names available
    preset_names = await get_presets_to_try(connection)
    
    if len(preset_names) == 0:
        print('[success]All presets explored![/]')
        sys.exit()
    
    # Pick a random unexplored preset.
    return random.choice(preset_names)


async def report_numbers(connection):
    """ Report the number of themes. """
    num_total = len(await itermlink.get_presets(connection))
    num_to_try = len(await get_presets_to_try(connection))
    print(
        f'There are {num_total} [emph]total[/] presets, and {num_to_try} '
        '[emph]to try[/].'
    )



#======================== Entry ========================#


async def main(connection):
    flags = _init_args()

    #--- Delete command run ---#
    if flags['del']:
        preset_name = await itermlink.get_current_preset(connection)
        print(f'[warning]Deleting[/] preset: [emph]{preset_name}[/].')
        itermlink.delete_preset(preset_name)
        # Auto flag cannot be true if theme is to be deleted
        flags['auto'] = False
        # Continue with running script to get a new preset


    if flags['clear']: os.system('clear')


    # Print the number of themes to try, if --num then do nothing more.
    await report_numbers(connection)
    if flags['num']: return
    
    app = await iterm2.async_get_app(connection)

    # Only run when this is the unique session if launched automatically.
    if flags['auto'] and not itermlink.has_unique_session(app.current_window):
        return

    # Main script loop as nested function to allow for continuous calls without
        # re-reporting numbers or any other processing.
    async def main_loop(connection):
        """ The main script loop. """
        preset_name = await random_preset(connection)
        await itermlink.change_preset(connection, preset_name)

        # Prompt user to see if scheme should be kept
        prompt = f'Keep new color preset: [emph]{preset_name}[/]?'
        if confirm(prompt, default=True):
            save_preset(preset_name)
        else:
            itermlink.delete_preset(preset_name)
            print('Color scheme deleted.')
            # Try again
            await main_loop(connection)


    # Run the main script loop.
    await main_loop(connection)



if __name__ == '__main__':
    try:
        iterm2.run_until_complete(main)
    except KeyboardInterrupt as e:
        print('Keyboard interrupt.')