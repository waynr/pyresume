#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_templates
----------------------------------

Tests for jinja2 LaTeX resume template files.
"""

import pkg_resources

from jinja2 import Environment


def test_standard_template_exists():
    """
    Validate that the standard LaTeX template is available through pkg_resources
    at the expected location.
    """
    assert pkg_resources.resource_exists('pyresume',
                                         'templates/standard.tex')


def test_standard_template_is_valid_jinja2_format():
    """
    Validate that the standard LaTeX template is well-formed as far as Jinja2 is
    concerned.
    """
    env = Environment()
    template_string = pkg_resources.resource_string('pyresume',
                                                    'templates/standard.tex').decode()
    env.parse(template_string)
