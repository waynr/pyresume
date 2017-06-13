#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyresume
----------------------------------

Tests for `pyresume` module.
"""

from click.testing import CliRunner

from pyresume import cli


def test_command_line_interface():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'pyresume.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
