# -*- coding: utf-8 -*-

import pkg_resources
import yaml

from jinja2 import Template
import click


@click.group()
def main():
    """Console script for pyresume.
    """
    pass


@main.command()
@click.argument('yaml_paths',
                nargs=-1,
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
    template_string = pkg_resources.resource_string(
        'pyresume', 'templates/standard.tex').decode()
    template = Template(template_string)

    resume_data = {}
    for path in yaml_paths:
        with open(path, "r") as f:
            yaml_data = yaml.load(f)
        resume_data.update(yaml_data)

    latex_string = template.render(**resume_data)
    click.echo(latex_string)


if __name__ == "__main__":
    main()
