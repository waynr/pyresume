# -*- coding: utf-8 -*-

import yaml

from jinja2 import Environment
from jinja2 import PackageLoader
import click

from pyresume.cli.validation import validate_yaml_paths


@click.group()
def main():
    """ Console script for pyresume.
    """
    pass


@main.group()
def create():
    """ Create a resume of the specified type. The type is either "tex" by
    default or whatever is specified as the next subcommand.
    """
    pass


@create.command()
@click.argument('yaml_paths',
                nargs=-1,
                callback=validate_yaml_paths,
                type=click.Path(exists=True,
                                file_okay=True,
                                dir_okay=False,
                                readable=True,
                                resolve_path=True))
def tex(yaml_paths):
    """Generate LaTeX output.

    Using the resume data contained within the given yaml files, generate LaTeX
    output on stdout. Note that resume data in successive yaml files overrides
    that specified in earlier files.
    """
    env = Environment(
        trim_blocks=True,
        lstrip_blocks=True,
        loader=PackageLoader('pyresume', 'templates'),
    )
    template = env.get_template('standard.tex')

    resume_data = {}
    for path in yaml_paths:
        with open(path, "r") as f:
            yaml_data = yaml.load(f)
        resume_data.update(yaml_data)

    latex_string = template.render(**resume_data)
    click.echo(latex_string)


if __name__ == "__main__":
    main()
