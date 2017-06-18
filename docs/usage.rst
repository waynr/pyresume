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

Single Yaml Example
+++++++++++++++++++

Basic usage is pretty simple::

  pyresume create tex /path/to/attributes.yaml > my-resume.tex

Single Yaml Example
+++++++++++++++++++

Basic usage is pretty simple::

  pyresume create tex /path/to/attr1-1.yaml /path/to/attr1-2.yaml > my-resume.tex


Advanced
--------

Advance usage assumes that you have docker installed. If you don't have it
installed, then you should figure that out before continuing.

Generate PDF Using Docker Image
+++++++++++++++++++++++++++++++

This is considered "advanced" usage because it involves using programs other
than ``pyresume`` itself.

The following example will run a docker container that uses an image known to
have a complete installation of ``texlive``. Note that this assumes you have an
``attributes.yaml`` file in your current working directory::

  pyresume create tex /path/to/attributes.yaml > my-resume.tex
  docker run --rm -it -v $PWD:/doc/ thomasweise/texlive pdflatex.sh /doc/my-resume.tex

This should result in a ``my-resume.pdf`` file in your current working
directory. If it doesn't, then please feel free to :ref:`report-bugs`!


Generate PDF on Linux Using ``texlive``
+++++++++++++++++++++++++++++++++++++++

These instructions should vary depending on the specific distro you are using.
If your distro is not listed here but you happen to know how to do it, please
consider :ref:`contributing documentation <write-documentation>`.

Debian 9/Stretch
~~~~~~~~~~~~~~~~

You should install and ``texlive`` and ``latexmk`` if you haven't already::

  sudo apt-get install texlive latexmk

Once you have, the following will create your PDF resume::

  pyresume create tex /path/to/attributes.yaml > my-resume.tex
  latexmk -pdf my-resume.tex

This should result in a ``my-resume.pdf`` file in your current working
directory. If it doesn't, then please feel free to :ref:`report-bugs`!

Tips & Tricks
-------------

Version Control
+++++++++++++++

Create a git repository to version-control your resume::

  mkdir -p /home/me/projects/personal-resume
  cd /home/me/projects/personal-resume

  git init
  $EDITOR attributes.yaml # Fill it with all your secrets.
  git add attributes.yaml
  git commit -m "My very first version-controlled resume."

If you also consider pushing it to a public git repo be careful not to add
personal contact info that you wouldn't want everyone to see! One way to avoid
this is to keep your "basic" section out of the bulk of your resume attributes,
like so::

  $EDITOR attributes.yaml # Fill it your skills, education, work history, etc
  $EDITOR contact.yaml # Fill it your pyresume "basic" section.
  git add attributes.yaml
  echo "contact.yaml" >> .gitignore
  git add .gitignore
  git commit -m "My very first version-controlled resume."


Have your own tips & tricks? Consider :ref:`writing some documentation
<write-documentation>`!
