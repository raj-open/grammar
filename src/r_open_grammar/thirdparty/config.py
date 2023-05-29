#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import json;
from yaml import add_constructor as yaml_add_constructor;
from yaml import add_path_resolver as yaml_add_path_resolver;
from yaml import load as yaml_load;
from yaml import FullLoader as yaml_FullLoader;

from typing import Any;
from typing import Callable;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MODIFICATIONS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def json_load_safe(
    text: Any,
    default_factory: Callable[[], dict] = dict
) -> dict[str, Any]:
    try:
        if isinstance(text, str):
            return json.loads(text);
    except:
        pass;
    return default_factory();

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# EXPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__all__ = [
    'json',
    'json_load_safe',
    'yaml_add_constructor',
    'yaml_FullLoader',
    'yaml_Loader',
    'yaml_add_path_resolver',
    'yaml_load',
];
