#!/usr/bin/env python
import os

# DO NOT CLEAN PDFS

# Clean root source
for doc_filename in os.listdir('.'):
    if doc_filename.endswith('.aux') or\
        doc_filename.endswith('.bbl') or\
        doc_filename.endswith('.blg') or\
        doc_filename.endswith('.out') or\
        doc_filename.endswith('.DS_Store') or\
        doc_filename.endswith('.log'):

        os.remove(os.path.join('.', doc_filename))

for doc_filename in os.listdir('author_source/coverletter'):
    if doc_filename.endswith('.aux') or\
        doc_filename.endswith('.bbl') or\
        doc_filename.endswith('.blg') or\
        doc_filename.endswith('.out') or\
        doc_filename.endswith('.DS_Store') or\
        doc_filename.endswith('.log'):

        os.remove(os.path.join('author_source/coverletter', doc_filename))


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
            if doc_filename.endswith('.aux') or\
                doc_filename.endswith('.bbl') or\
                doc_filename.endswith('.blg') or\
                doc_filename.endswith('.out') or\
                doc_filename.endswith('.DS_Store') or\
                doc_filename.endswith('.log'):

                os.remove(os.path.join(doc_dir, doc_filename))