Rejecta Mathematica Archive
===========

Installing LaTeX
-----------

This project has been tested on Mac OS X 10.9.4 with the MacTex 2014 distribution [https://tug.org/mactex/].
This project should also build on linux systems, for example on Ubuntu or Debian try installing via

    sudo apt-get install pdflatex bibtex pdftex

To run the build scripts, you should be able to find the following installed binaries:

    which pdflatex --> /usr/texbin/pdflatex
    which pdftex
    which bibtex

Please let us know if you are unable to compile this project with other versions
and supply a fix if possible.

Building the Volumes
-----------

The volumes and all associated articles and letters should
build when executing `build.py`, e.g.,

    cd Journal/Volume1/Number1/
    ./build.py

The build file suppresses LaTeX's verbose output.  If you want verbose output,
manually remove `> /dev/null` from the system calls at the top of the file.

### Cleaning AUX Files

In the same directory as `build.py` you will find `clean.py`, a script
that removes most of the auxiliary LaTeX files.

PDF files are **not removed**
by `clean.py` since several original manuscript files are in this format.