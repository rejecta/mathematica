Rejecta Mathematica Archive
===========

Getting LaTeX
-----------

This project has been tested with the MacTex 2014 distribution [https://tug.org/mactex/].
Please let us know if you are unable to compile this project with other versions
and supply a fix if possible.

To run the build scripts, you should be able to find binarys for the following:

    'which pdflatex' --> /usr/texbin/pdflatex
    'which pdftex' 
    'which bibtex'


Building the volumes
-----------

The volumes and all associated articles and letters should
build when executing 'build.py', e.g.,

    cd Journal/Volume1/Number1/
    ./build.py

Similarly, in the same directory you will find a 'clean.py' script
that removes most of the auxiliary LaTeX files.  PDF files are not removed
by this script since several source files are indeed PDFs.
