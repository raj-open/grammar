#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os;
import sys;
from pathlib import Path;
import platform;

import re;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MODIFICATIONS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def create_new_path_name(dir: str, nameinit: str = 'tmp', namescheme: str = 'tmp_{}') -> str:
    '''
    Creates a new path name. Uses template if path already exists.
    '''
    path = os.path.join(dir, nameinit);
    i = 0;
    while os.path.isdir(path):
        path = os.path.join(dir, namescheme.format(i));
        i += 1;
    return path;

def create_new_file_name(dir: str, nameinit: str = 'tmp', namescheme: str = 'tmp_{}') -> str:
    '''
    Creates a new file name. Uses template if file already exists.
    '''
    path = os.path.join(dir, nameinit);
    i = 0;
    while os.path.isfile(path):
        path = os.path.join(dir, namescheme.format(i));
        i += 1;
    return path;

def create_file_if_not_exists(path: str) -> None:
    '''
    Creates a file if it does not exist.
    '''
    if not os.path.exists(path):
        create_dir_if_not_exists(os.path.dirname(path));
        Path(path).touch(exist_ok=True);
    if not os.path.exists(path) or not os.path.isfile(path):
        raise FileExistsError(f'\033[93;1m{path}\033[0m could not be created!');
    return;

def create_dir_if_not_exists(path: str) -> None:
    '''
    Creates a directory if it does not exist.
    '''
    if path in [ '', '.', os.getcwd() ]:
        return;
    if not os.path.exists(path):
        Path(path).mkdir(parents=True, exist_ok=True);
    if not os.path.exists(path) or not os.path.isdir(path):
        raise FileExistsError(f'\033[93;1m{path}\033[0m could not be created!');
    return;

def read_text_file(path: str) -> str:
    '''
    Reads from text file.
    '''
    with open(path, 'r') as fp:
        return ''.join(fp.readlines());

def write_text_file(
    path: str,
    lines: str | list[str],
    force_create_path: bool = False,
    force_create_empty_line: bool = True
):
    '''
    Writes text to a file (overwrites if already exists).
    '''
    if force_create_path:
        create_dir_if_not_exists(os.path.dirname(path));
    if isinstance(lines, str):
        text = lines.rstrip('\r\n');
    else:
        while len(lines) > 0:
            if not re.match(pattern=r'^\s*$', string=lines[-1]):
                break;
            lines = lines[:-1];
        text = '\n'.join(lines);
    with open(path, 'w') as fp:
        fp.write(text);
        if force_create_empty_line:
            fp.write('\n');
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# EXPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__all__ = [
    'Path',
    'create_dir_if_not_exists',
    'create_file_if_not_exists',
    'create_new_file_name',
    'create_new_path_name',
    'os',
    'platform',
    'read_text_file',
    'sys',
    'write_text_file',
];
