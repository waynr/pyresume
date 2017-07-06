=====
Usage
=====

PyResume Builder is a command line tool that takes a path to a YAML file
containing resume data and produces a LaTeX document. The following is an
example of YAML that will produce a resume using all features of the basic
template.

.. literalinclude:: ../tests/scenarios/fixtures/standard/full_example/attributes.yaml
  :language: yaml
  :linenos:

Before you begin, please be sure to read :ref:`installation instructions
<inst-inst>`. If you have any trouble, please be sure that all the
:ref:`reqs-reqs` have been satisfied. Also consider :ref:`submitting feedback
<feedback>` if you encounter any issues (bug, problem with docs, deepfelt
yearning for existential meaning)

You will have the best chance of successfully using ``pyresume`` if you are
running either Linux or Mac.


Basic
-----

Basic usage is basic because it assumes that all you care about is generating
LaTeX. If you want to go further and produce a PDF or some other output format
supported by LaTeX, see the :ref:`Advanced section below <advanced>`.


Single Yaml -> LaTeX
+++++++++++++++++++

The following command assumes you have a file called ``./attributes.yaml`` in
the directory in which you are running commands. If you don't, feel free to copy
the contents of the full example shown above into a new file called
``./attributes.yaml``.

.. code-block:: bash

  $ pyresume create tex ./attributes.yaml > my-resume.tex

The result is a file called ``my-resume.tex``. You can open this file with a
text editor, but it will look like gibberish unless you are familiar with TeX,
LaTeX, or etc. To quote https://www-project.org/about/ ,

  LaTeX, which is pronounced «Lah-tech» or «Lay-tech» (to rhyme with «blech» or
  «Bertolt Brecht»), is a document preparation system for high-quality
  typesetting. It is most often used for medium-to-large technical or scientific
  documents but it can be used for almost any form of publishing.

Most people may not care about that so it will be left to the reader to decide
whether to `learn more about LaTeX<https://latex-project.org>`_. (You may need
to learn more if you aren't running a linux distro with either ``docker`` or
some kind of software that can read LaTeX and spit out PDFs.)


Multi Yaml -> LaTeX
++++++++++++++++++

What if you want to keep different types of attributes in their own file? See
below, where the ``./basic.yaml`` contains all the contact information that you
might (for example) want to keep out of a git repository, or in a more private
git repository.

.. code-block:: console

  $ pyresume create tex ./attributes.yaml ./basic.yaml > my-resume.tex

As with the single yaml to LaTeX use case, the result here is a file called
``my-resume.tex``.


Advanced
--------

These are considered "advanced" usage because it involves using programs other
than ``pyresume`` itself.


Generate PDF Using Docker Image
+++++++++++++++++++++++++++++++

This usage assumes that you have docker installed. If you don't have it
installed, then you should figure that out before continuing. The docker website
has some `good documentation for getting
started<https://docs.docker.com/get-started/>`_.

The following commands will run a docker container that uses an image known to
have a complete installation of ``texlive``. Note that this assumes you have an
``attributes.yaml`` file in your current working directory:

.. code-block:: console

  $ pyresume create tex /path/to/attributes.yaml > my-resume.tex
  $ docker run --rm -it -v $PWD:/doc/ thomasweise/texlive pdflatex.sh /doc/my-resume.tex

This should result in a ``my-resume.pdf`` file in your current working
directory. If it doesn't, then please feel free to :ref:`report-bugs`!


Generate PDF on Linux Using ``texlive``
+++++++++++++++++++++++++++++++++++++++

These instructions should vary depending on the specific distro you are using.
If your distro is not listed here but you happen to know how to adapt these
instructions for it, please consider :ref:`contributing documentation
<write-documentation>`.

Debian 9/Stretch
~~~~~~~~~~~~~~~~

You should install and ``texlive`` and ``latexmk`` if you haven't already:

.. code-block:: console

  $ sudo apt-get install texlive latexmk

Once you have, the following will create your PDF resume:

.. code-block:: console

  $ pyresume create tex /path/to/attributes.yaml > my-resume.tex
  $ latexmk -pdf my-resume.tex

This should result in a ``my-resume.pdf`` file in your current working
directory. If it doesn't, then please feel free to :ref:`report-bugs`!


Tips & Tricks
-------------


Version Control
+++++++++++++++

Create a git repository to version-control your resume:

.. code-block:: console

  $ mkdir -p /home/me/projects/personal-resume
  $ cd /home/me/projects/personal-resume

  $ git init

  $ $EDITOR attributes.yaml # Fill it with all your secrets.
  $ git add attributes.yaml
  $ git commit -m "My very first version-controlled resume."

If you also consider pushing it to a public git repo be careful not to add
personal contact info that you wouldn't want everyone to see! One way to avoid
this is to keep your "basic" section out of the bulk of your resume attributes,
like so:

.. code-block:: console

  $ $EDITOR attributes.yaml # Fill it your skills, education, work history, etc
  $ $EDITOR basic.yaml # Fill it your pyresume "basic" section.
  $ git add attributes.yaml
  $ echo "basic.yaml" >> .gitignore
  $ git add .gitignore
  $ git commit -m "My very first version-controlled resume."


Have your own tips & tricks? Consider :ref:`writing some documentation
<write-documentation>`!
