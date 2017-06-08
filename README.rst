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

N/A

Planned
+++++++

* Generate LaTeX resume from simple YAML list of attributes
* Supports Jinja2 templates
* Easily create new resume templates using cookiecutter

Roadmap
-------

* Version 0.1.0

  * Tests

    * [x] default template tests
    * scenario-based

      * [ ] default template tests
      * [ ] exteranl git repo template tests (http://)
      * [ ] exteranl git repo template tests (https://)
      * [ ] exteranl git repo template tests (git://)
      * [ ] exteranl git repo template tests (ssh://)

    * unit tests

  * [ ] Find/create docker image to provide latex packages
  * Command line

    * [ ] parameter to specify location of LaTeX templates

  * LaTeX Templates

    * Initial templates packaged w/ pyresume

      * [x] Jinja2 template with basic layout
      * [x] stored as setuptools resource

    * External Templates

      * [ ] From local file
      * [ ] From git repo
      * [ ] Cookiecutter repo for new template repos

  * Examples

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

