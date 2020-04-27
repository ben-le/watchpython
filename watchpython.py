# WatchPython
# By Al Sweigart al@inventwithpython.com

__version__ = '0.1.0'

import os
import subprocess
import sys
import time

import click

@click.command()
@click.version_option(version=__version__)
@click.option('-v', '--version', is_flag=True, help='Output version information and exit.')
@click.option('-n', '--interval', default=2, help='Seconds to wait between updates.', type=float)
@click.argument('command')
def main(command, interval, version):
    """Run the given command until Ctrl-C is pressed."""
    clearScreen()
    commandStdOuput = ''
    try:
        while True:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)

            if result.stdout != commandStdOuput:
                commandStdOuput = result.stdout
                clearScreen()
                click.echo(result.stdout)

            time.sleep(interval)
    except KeyboardInterrupt:
        sys.exit()


def clearScreen():
    if sys.platform == 'win32':
        os.system('cls')  # Windows uses the cls command.
    else:
        os.system('clear')  # macOS and Linux use the clear command.

if __name__ == '__main__':
    main()