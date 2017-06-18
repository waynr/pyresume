#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""test_scenarios
----------------------------------

"Scenario" based testing that autodiscovers test scenarios from the adjacent
"fixtures" directory.

"""

import os

from click.testing import CliRunner
import docker
import py

from pyresume.cli import main
from pyresume import utils


fixtures_top_dir = os.path.join(os.path.dirname(__file__), "fixtures")


def get_scenarios():
    scenarios = []
    for template in os.listdir(fixtures_top_dir):
        for scenario in os.listdir(os.path.join(fixtures_top_dir, template)):
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
        result = runner.invoke(main, ["create", "tex"] + yaml_file_list)
        assert result.exit_code == 0

        with open(expected_output_file, "r") as f:
            expected_output = f.read()

        assert result.output == expected_output

    def test_scenario_output_compiles(self,
                                      yaml_file_list,
                                      expected_output_file,
                                      tmpdir):
        """ Validate that the generated tex output can be used to produce a
        PDF using a known, publicly-available docker image.
        """
        docker_api_version = utils.get_subprocess_output(
            'docker version --format \'{{.Server.APIVersion}}\'')
        client = docker.from_env(version=docker_api_version)

        runner = CliRunner()
        result = runner.invoke(main, ["create", "tex"] + yaml_file_list)

        tmp_tex_file = tmpdir.join("expected.tex")
        tmp_tex_file.write(result.output)

        output = client.containers.run(
            "thomasweise/texlive",
            "pdflatex.sh /doc/expected.tex",
            volumes={
                str(tmpdir): "/doc/",
            },
            remove=True,
        ).decode()
        print(output)
        assert "compilation finished successfully" in output
