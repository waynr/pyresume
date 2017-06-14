================
PyResume Builder
================


.. image:: https://img.shields.io/pypi/v/pyresume.svg
        :target: https://pypi.python.org/pypi/pyresume

.. image:: https://img.shields.io/travis/waynr/pyresume.svg
        :target: https://travis-ci.org/waynr/pyresume

.. image:: https://readthedocs.org/projects/pyresume/badge/?version=latest
        :target: https://pyresume.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/waynr/pyresume/shield.svg
     :target: https://pyup.io/repos/github/waynr/pyresume/
     :alt: Updates


Populate a predefined LaTeX template with contents defined in YAML to build your resume.


* Free software: GNU General Public License v3
* Documentation: https://pyresume.readthedocs.io.


Features
--------

Current
+++++++

* Generate LaTeX resume from simple YAML list of attributes.
* Uses single simple template for consistent look and feel between different
  combinations of information you might want to include in your resume.

Planned
+++++++

* Support externally-defined Jinja2 templates.
* Easily create new resume templates using cookiecutter.

Roadmap
-------

Version 0.1.0
+++++++++++++

* Meta

  * [ ] Consider different name for tool.
  * (last) Post link to repositories and readthedocs in public forums:

    * reddit
    * facebook
    * linkedin

* Documentation

  * [ ] Introduce problem being solved.
  * [ ] Refer to readthedocs for bulk of documentation.
  * [ ] Research and refer to similar tools/services.

  * Basic Usage instructions

    * [ ] Running from CLI on Linux
    * [ ] Running from CLI using Docker on any platform

  * Advanced Usage instructions

    * [ ] Generate scenario test fixtures
    * [ ] Describe workflow for storing resume in a repo as yaml and using
      pyresume to generate PDFs.

* Examples

  * [ ] Create Example resume repository

* Tests

  * scenario

    * docker/texlive integration tests to validate PDF generation

      * [ ] Find/create docker image to provide latex packages
      * [ ] Get docker integration test(s) running locally.
      * [ ] Research docker in Travis, figure out what kind of foolery is
        necessary to make docker tests run there.

* Templates

  * Initial templates packaged w/ pyresume

    * [x] Jinja2 template with basic layout
    * [x] stored as setuptools resource

* Command line

  * [x] change 'tex' subcommand to 'create'/'create tex'

Version 0.2.0
+++++++++++++

* Meta
  
  * [ ] Move this Roadmap elsewhere, maybe generate github or bitbucket issues
    and labels to track the work.

* User Input Validation

  * Use voluptuous to validate data structures passed in by users.

    * [ ] Implement validation in same directory as template.
    * [ ] Write tests for validation function to concretely define various
      corner cases (the exceptions and/or warnings producted by validation).
  
* External Templates

  * [ ] From local file
  * [ ] From git repo
  * [ ] Cookiecutter repo for new template repos

* Tests

  * scenario-based

    * [ ] external git repo template tests (http://)
    * [ ] external git repo template tests (https://)
    * [ ] external git repo template tests (git://)
    * [ ] external git repo template tests (ssh://)

* Command line

  * [ ] parameter to specify location of LaTeX templates
  * [ ] add 'create pdf' subcommand that uses docker (if available) to run texlive
    and generate a resume


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
