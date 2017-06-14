#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""test_scenarios
----------------------------------

"Scenario" based testing that autodiscovers test scenarios from the adjacent
"fixtures" directory.

"""

import os
import pkg_resources

from click.testing import CliRunner
import pytest

from pyresume.cli import main


fixtures_top_dir = os.path.join(os.path.dirname(__file__), "fixtures")


def get_scenarios():
    scenarios = []
    for template in os.listdir(fixtures_top_dir):
        for scenario in os.listdir(os.path.join(fixtures_top_dir, template)):
            scenario_dir = os.path.join(fixtures_top_dir, template)
            scenario_path = os.path.join(fixtures_top_dir, template, scenario)
            scenario_id = "{0}-{1}".format(template, scenario)
            yaml_files = [os.path.join(scenario_path, n)
                          for n in os.listdir(scenario_path)
                          if n.endswith(".yaml")]
            output_file = os.path.join(scenario_path, "expected.tex")
            scenarios.append((scenario_id, yaml_files, output_file))
    return scenarios


def pytest_generate_tests(metafunc):
    idlist = []
    argvalues = []

    for scenario in get_scenarios():
        idlist.append(scenario[0])
        argnames = ["yaml_file_list", "expected_output_file"]
        argvalues.append((scenario[1], scenario[2]))

    metafunc.parametrize(argnames, argvalues, ids=idlist, scope="class")


class TestTemplateWithScenarios(object):
    scenarios = get_scenarios()

    def test_scenario_exists(self, yaml_file_list, expected_output_file):
        """ Validate that the files necessary to run tests for each scenaro
        exist.
        """
        for f in yaml_file_list:
            assert os.path.exists(f)
        assert os.path.exists(expected_output_file)

    def test_scenario_expected_output(self,
                                      yaml_file_list,
                                      expected_output_file):
        """ Validate that when the pyresume CLI is run with the given
        scenario's yaml file(s), the output produce is equivalent to that
        scenario's expected LaTeX output.
        """
        runner = CliRunner()
        result = runner.invoke(main, ["tex",] + yaml_file_list)
        assert result.exit_code == 0

        with open(expected_output_file, "r") as f:
            expected_output = f.read()

        assert result.output == expected_output
