#!/usr/bin/env python
import os

# DO NOT CLEAN PDFS

aux_ext = ['.aux', '.bbl', '.blg', '.out', '.DS_Store', '.cb', '.cb2', '.log', '.synctex.gz', '.toc']

# Clean root source
for doc_filename in os.listdir('.'):
    for aux in aux_ext:
        if doc_filename.endswith(aux):
            os.remove(os.path.join('.', doc_filename))        

# Clean tex aux files from each issue
src_dir = 'author_source'
for author_dir in os.listdir(src_dir):
    if author_dir.startswith('.'):
        continue

    doc_types = ['.', 'openletter', 'article']
    for doc_type in doc_types:
        doc_dir = os.path.join(src_dir, author_dir, doc_type)
        if not os.path.isdir(doc_dir):
            continue

        for doc_filename in os.listdir(doc_dir):
            for aux in aux_ext:
                if doc_filename.endswith(aux):
                    os.remove(os.path.join(doc_dir, doc_filename))