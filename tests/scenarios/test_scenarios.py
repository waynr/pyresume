#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""test_scenarios
----------------------------------

"Scenario" based testing that autodiscovers test scenarios from the adjacent
"fixtures" directory.

"""

import os
import pkg_resources
import pprint

from click.testing import CliRunner
import pytest


fixtures_top_dir = os.path.join(os.path.dirname(__file__), "fixtures")


def get_scenarios():
    scenarios = []
    for template in os.listdir(fixtures_top_dir):
        for scenario in os.listdir(os.path.join(fixtures_top_dir, template)):
            scenario_dir = os.path.join(fixtures_top_dir, template)
            scenario_path = os.path.join(fixtures_top_dir, template, scenario)
            scenario_id = "{0}-{1}".format(template, scenario)
            yaml_files = [n for n in os.listdir(scenario_path)
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

    @pytest.mark.xfail
    def test_scenario_exists(self, yaml_file_list, expected_output_file):
        pprint.pprint(yaml_file_list)
        print(expected_output_file)
        assert False
