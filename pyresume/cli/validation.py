# -*- coding: utf-8 -*-

"""cli.validation
----------------------------------

Validation functions for CLI.

"""

import click


def validate_yaml_paths(ctx, param, value):
    if not value:
        raise click.BadParameter("Must provide at least one yaml path.")
    return value
