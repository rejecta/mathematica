#!/usr/bin/env python
import os

def pdflatex(filepath):
    os.system('pdflatex {0} > /dev/null'.format(filepath))

def plaintex(filepath):
    os.system('pdftex {0} > /dev/null'.format(filepath))

def bibtex(filepath):
    bibfilepath = '/'.join(filepath.split('.')[:-1])
    os.system('bibtex {0} > /dev/null'.format(bibfilepath))

def latexwithbib(filepath):
    pdflatex(filepath)
    bibtex(filepath)
    pdflatex(filepath)
    pdflatex(filepath)

class temp_cd():
    def __init__(self, temp_dir):
        self._temp_dir = temp_dir
        self._return_dir = os.path.dirname(os.path.realpath(__file__))
    def __enter__(self):
        os.chdir(self._temp_dir)
    def __exit__(self, type, value, traceback):
        os.chdir(self._return_dir)


# Compile each issue
src_dir = 'author_source'
for author_dir in os.listdir(src_dir):
    if author_dir == '.':
        continue

    doc_types = ['openletter', 'article']
    for doc_type in doc_types:
        doc_dir = os.path.join(src_dir, author_dir, doc_type)
        if not os.path.isdir(doc_dir):
            continue

        for filename in os.listdir(doc_dir):
            if filename.endswith('.tex'):
                print 'Compiling', doc_dir, filename, '...'
                with temp_cd(doc_dir):
                    latexwithbib(filename)
            if filename.endswith('.plaintex'):
                print 'Compiling', doc_dir, filename, '...'
                with temp_cd(doc_dir):
                    plaintex(filename)

# Build full journal volume
filename = 'RejectaMathematicaVol2No1.tex'
print 'Compiling full volume:', filename, '...'
latexwithbib(filename)

