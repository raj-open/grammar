#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from src.thirdparty.misc import *;
from src.thirdparty.config import *;
from src.thirdparty.code import *;
from src.thirdparty.types import *;
from src.thirdparty.system import *;

from src.models.config import *;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# EXPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__all__ = [
    'CONFIG',
    'PATHS',
    'GRAMMARS',
];

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CONSTANTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PATHS_CONFIG = 'src/config.yaml';

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# LAZY LOADED RESOURCES
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@make_lazy
def load_assets_config() -> ProgrammeConfig: # pragma: no cover
    with open(PATHS_CONFIG, 'r') as fp:
        assets = yaml_load(fp, Loader=yaml_FullLoader);
        assert isinstance(assets, dict);
        return ProgrammeConfig(**assets);

@make_lazy
def load_paths(config: ProgrammeConfig) -> ProgrammePaths: # pragma: no cover
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'));
    paths = config.paths;
    paths.root = root;
    return paths;

# use lazy loaing to ensure that values only loaded (once) when used
CONFIG = load_assets_config();
PATHS = load_paths();
GRAMMARS = lazy(lambda: CONFIG.grammars);
