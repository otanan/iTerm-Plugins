#!/usr/bin/env python3
"""Deletes the existing wallpaper.

**Author: Jonathan Delgado**

"""
#------------- Imports -------------#
import os
import sys
import argparse
from pathlib import Path
import sqlite3
import PIL
from PIL import Image
#--- Custom imports ---#
from itermlink.tools.console import *
import itermlink
#------------- Fields -------------#
__version__ = 0.11
# Database holding current wallpaper filename
WALLPAPER_DB = Path.home() / 'Library/Application Support/Dock/desktoppicture.db'
WALLPAPER_FOLDER = Path.home() / 'Drive/Wallpapers'
#======================== Helper ========================#


def _init_arguments():
    """ Initializes the argument parser and returns the command line arguments.
    
        Returns:
            (argparse): the arguments
    
    """
    parser = argparse.ArgumentParser()
    # Delete the image with the provided path
    parser.add_argument(
        '-delete', help='Delete the provided wallpaper.',
        action='store_true'
    )
    parser.add_argument(
        '-res', help='Print the resolution of the provided wallpaper.',
        action='store_true'
    )
    parser.add_argument(
        '-reveal', help='Reveal the wallpaper file in Finder.',
        action='store_true'
    )
    # Provide an image path to prompt user for deletion
    parser.add_argument('--path', help='Absolute path to wallpaper file.')

    return parser.parse_args()


def _fname_to_abs_path(fname):
    """ Get absolute path to wallpaper. """
    return WALLPAPER_FOLDER / fname


def show_image_in_terminal(image_path):
    """ Show the image in the terminal window. """
    # Use iTerm2 imgcat to show the image
    options = '-W 1080px'
    command = f'imgcat {options} "{image_path}"\n'
    itermlink.run_command_on_active_sess(command)


def get_num_wallpapers():
    """ Count the number of wallpapers. """
    # Remove one for .DS_Store file
    return len(os.listdir(WALLPAPER_FOLDER)) - 1


def print_num_wallpapers():
    print(f'Number of wallpapers: [green]{get_num_wallpapers()}[/].')


def prompt_deletion(image_path):
    """ Prompt the user for deleting the wallpaper. """
    if confirm(
        f'[warning]Delete wallpaper[/]: "[emph]{image_path.name}[/]"?',
        default=False
    ):
        os.remove(image_path)
        print('[warning]Wallpaper deleted[/].')
    else:
        print('[success]Wallpaper deletion canceled[/].')


def current_wallpaper_path():
    """ Get the absolute path to the current wallpaper. """
    # Establish connection to database
    sql_connection = sqlite3.connect(WALLPAPER_DB)
    cursor = sql_connection.cursor()
    
    # Get the current wallpaper fname
    cursor.execute('SELECT * FROM data ORDER BY rowID DESC LIMIT 1;')
    fname = cursor.fetchall()[0][0]
    # Close the database connections
    cursor.close()
    sql_connection.close()

    return _fname_to_abs_path(fname)


def get_wallpaper_res(image_path):
    """ Returns the resolution of the wallpaper. """
    image = PIL.Image.open(image_path)
    return image.size


def reveal_file(path):
    """ Reveal the file in Finder. """
    import subprocess
    subprocess.call(['open', '-R', path])


#======================== Entry ========================#


def main():
    args = _init_arguments()
    # No path was provided, we must get it and show the image in reference
    if args.path is None:
        path = current_wallpaper_path()
        # Show wallpaper in consideration
        show_image_in_terminal(path)
        
        # iTerm took control to show image in terminal, we need to make 
            # recursive call, to relinquish control back to the script itself
        command = 'wallp '
        # Add flags
        command += '-res ' * args.res
        command += '-reveal ' * args.reveal
        command += '-delete ' * args.delete
        # Make call
        itermlink.run_command_on_active_sess(command + f' --path="{path}"')
        # The recursive call will take control of the script
        sys.exit()
    else:
        # A recursive call was made, proceed as normally
        path = Path(args.path)


    #------------- Wallpaper management -------------#
    #--- Wallpaper resolution requested ---#
    if args.res:
        # Requested resolution of image file
        res = get_wallpaper_res(path)
        print(f'[emph]Wallpaper resolution[/]: [green]{res[0]}x{res[1]}[/].')

    #--- Show wallpaper in Finder ---#
    if args.reveal:
        reveal_file(path)

    #--- Wallpaper deletion requested ---#
    if args.delete:
        prompt_deletion(path)

    # End script by printing number of remaining wallpapers.
    print_num_wallpapers()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print('Keyboard interrupt.')