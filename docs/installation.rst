.. highlight:: shell
.. _inst-inst:

============
Installation
============

.. _reqs-reqs:

Requirements
------------

Python >= 3.5
  The only tested version of python so far. 

For Generating PDFs
+++++++++++++++++++

One of the following tools should be sufficient to actually generate PDFs:

docker
  Provides full texlive installation for the sake of producing PDF output in
  tests. In the future there will be a ``pyresume create pdf`` command that uses
  this image to generate PDFs directly for users.
texlive (or some other LaTeX tool)
  A relatively minimal installation should take care of most resume-generating
  needs.

Installation steps for either of these will vary depending on the operating
system (ie windows, mac, linux, etc); in the case of linux, your OS's package
management tool (yum, apt, nix, pacman, emerge, etc); and on your OS version.
However, I would recommend trying docker first since that will open up other
avenues of computer usage for you.
  

Stable release
--------------

To install PyResume Builder, run this command in your terminal:

.. code-block:: console

    $ pip install pyresume

This is the preferred method to install PyResume Builder, as it will always install the most recent stable release. 

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for PyResume Builder can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/waynr/pyresume

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/waynr/pyresume/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/waynr/pyresume
.. _tarball: https://github.com/waynr/pyresume/tarball/master
