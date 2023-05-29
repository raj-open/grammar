#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from ..thirdparty.io import *;
from ..thirdparty.misc import *;
from ..thirdparty.types import *;

from ..core.log import *;
from ..models.cli import *;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# EXPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__all__ = [
    'display_help',
    'display_usage',
    'get_arguments_from_cli',
];

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CONSTANTS/VARIABLES
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

parser = None;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_arguments_from_cli(*cli_args: str) -> ProgrammeArguments:
    '''
    Extracts CLI arguments.
    '''
    try:
        parser = get_argument_parser();
        args = vars(parser.parse_args(cli_args));
        return ProgrammeArguments(**{
            key: value
            for key, value in args.items()
            if value is not None
        });
    except Exception as e:
        display_usage();
        exit(1);

def display_help() -> None:
    '''
    Displays the usages of programme with CLI arguments.
    '''
    parser = get_argument_parser();
    parser.print_help();
    return;

def display_usage() -> None:
    '''
    Displays the full help file for CLI arguments for programme.
    '''
    parser = get_argument_parser();
    parser.print_usage();
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# AUXILIARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_argument_parser() -> argparse.ArgumentParser:
    '''
    Constructs parser for CLI-arguments, if not already defined.
    '''
    global parser;
    if not isinstance(parser, argparse.ArgumentParser):
        parser = argparse.ArgumentParser(
            prog='tests/cases.py',
            description=dedent('''
            An interface to run the test cases.
            '''),
            formatter_class=argparse.RawTextHelpFormatter,
        );
        parser.add_argument('mode',
            nargs='?',
            choices=['version', 'help', 'run'],
            help=dedent('''
            - help:     Display this help.
            - version:  Display version.
            - run:      Run the Phpytex transpiler.
            '''),
        );
        parser.add_argument('--quiet', action='store_true', default=False, help='Hide all but the most important console messages during transpilation.');
        parser.add_argument('--debug', action='store_true', default=False, help='Display debugging (for development only).');
        parser.add_argument('--plain', action='store_true', default=False, help='If set, console logging will be performed without special terminal fonts.');
        parser.add_argument('--inspect', action='store_true', default=False, help='Pause at end of test case before removing result.');
    return parser;
