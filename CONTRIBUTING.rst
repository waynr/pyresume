.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

.. _report-bugs:

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/waynr/pyresume/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
and "help wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

.. _write-documentation:

Write Documentation
~~~~~~~~~~~~~~~~~~~

PyResume Builder could always use more documentation, whether as part of the
official PyResume Builder docs, in docstrings, or even on the web in blog posts,
articles, and such.

.. _feedback:

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/waynr/pyresume/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `pyresume` for local development.

1. Fork the `pyresume` repo on GitHub.
2. Clone your fork locally:

.. code-block:: console

    $ git clone git@github.com:your_name_here/pyresume.git
    $ cd ./pyresume

3. Install your local copy using Docker:

.. code-block:: console

    $ docker build --build-arg setup=develop --tag 'wayfair/pyresume:latest' .

4. Create a branch for local development:

.. code-block:: console

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. Test that PyResume does what you expect:

.. code-block:: console

    # `attributes.yaml` should exist in the `/path/to/yaml/files` directory.
    $ docker run --volume $PWD:/src/pyresume --volume /path/to/yaml/files:/mnt/pyresume wayfair/pyresume:latest pyresume create tex attributes.yaml > attributes.tex

6. When you're done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox:

.. code-block:: console

    $ flake8 pyresume tests
    $ python setup.py test or py.test
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

7. Commit your changes and push your branch to GitHub:

.. code-block:: console

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

8. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.6. Check
   https://travis-ci.org/waynr/pyresume/pull_requests and make sure that the
   tests pass for all supported Python versions.

Testing Tips
------------

Run a Subset of tests
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console
  $ py.test tests.test_pyresume


Generate New Test Fixtures
~~~~~~~~~~~~~~~~~~~~~~~~~~

To generate fixtures that use the standard/default resume template

.. code-block:: console

   $ mkdir /path/to/pyresume/tests/scenarios/fixtures/standard/<new-scenario>/
   $ $EDITOR /path/to/pyresume/tests/scenarios/fixtures/standard/<new-scenario>/attributes.yaml
   $ pyresume create tex > /path/to/pyresume/tests/scenarios/fixtures/standard/<new-scenario>/attributes.tex

You can validate this works as expected by running the tests

.. code-block:: console

   $ py.test tests.scenarios.test_scenarios

Alternatively, you could just run the entire test suite

.. code-block:: console

   $ tox -e py36

Assuming there new resume templates are eventually added, creating the fixture
might look something like:

.. code-block:: console

   $ mkdir /path/to/pyresume/tests/scenarios/fixtures/<new-template-name>/<new-scenario>/
   $ $EDITOR /path/to/pyresume/tests/scenarios/fixtures/<new-template-name>/<new-scenario>/attributes.yaml
   $ pyresume create --template <new-template-name> tex > /path/to/pyresume/tests/scenarios/fixtures/<new-template-name>/<new-scenario>/attributes.tex

And of course you will want to commit these to the git repo

.. code-block:: console

   $ git add /path/to/pyresume/tests/scenarios/fixtures/<new-template-name>/<new-scenario>/
