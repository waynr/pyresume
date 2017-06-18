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


Do you like updating your resume? Are you satisfied with the layout and
formatting? Do you ever wish you could try different styles without going
through the trouble of manually reformatting each time? Well now you can!

PyResume Builder is a command line tool that populates a LaTeX template from
contents defined in a YAML file. By storing the contents of your resume in a
human-readable markup language and generating a LaTeX or PDF file from that you
are free to try alternative templates and generate resumes in different formats
without the tedium of manually reformatting.


* Free software: GNU General Public License v3
* Documentation: https://pyresume.readthedocs.io.


Features
--------

Current
+++++++

* Store resume contents (skills, experience, contact info, etc) in a YAML file
  for ease of updating and version control convenience.
* Templated LaTeX approach allows for consistent look and feel between different
  combinations of information you might want to include in your resume.
* Default LaTeX template includes support for:

  * Contact info
  * Education  
  * Experience
  * Skills (up to two levels of subcategories supported)
  * Activities
  * Education
  * References

Planned
+++++++

* Support externally-defined Jinja2 LaTeX templates.
* Support some kind of html output format.
* Create new resume templates using cookiecutter.

Roadmap
-------

Version 0.1.0
+++++++++++++

* Documentation

  * [x] Introduce problem being solved.
  * [x] Research and refer to similar tools/services.

  * Basic Usage instructions

    * [x] Running from CLI on Linux
    * [x] Running from CLI using Docker on any platform

  * Advanced Usage instructions

    * [x] Generate scenario test fixtures
    * [x] Describe workflow for storing resume in a repo as yaml and using
      pyresume+latex to generate PDFs.

* Tests

  * scenario

    * docker/texlive integration tests to validate PDF generation

      * [x] Find/create docker image to provide latex packages
      * [x] Get docker integration test(s) running locally.
      * [x] Research docker in Travis, figure out what kind of foolery is
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
  * Post link to repositories and readthedocs in public forums:

    * [ ] reddit
    * [ ] facebook
    * [ ] linkedin


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


Similar Projects
----------------

http://www.resumebuilder.org
  This site let's you sign in, enter your resume data in a series of web forms,
  and generate a resume from predefined templates. Also seems to include all
  kinds of helpful advice about resume layouts and being more of a rock star
  potential employee.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
