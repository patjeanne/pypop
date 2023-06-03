#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# WordCount documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  8 14:27:52 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../source'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosectionlabel', 'myst_parser', 'rst2pdf.pdfbuilder', 'sphinx_togglebutton']

#autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'PyPop: Python for Population Genomics'
copyright = '2023 PyPop contributors'
author = "Alexander K. Lancaster\\and Mark P. Nelson\\and Diogo Meyer\\and Richard M. Single\\and Owen D. Solberg"

guide_prefix = 'pypop-guide'
guide_name = 'PyPop User Guide'
guide_subtitle = 'User Guide for Python for Population Genomics'
guide_name_with_subtitle = "%s \\\\{\\LARGE %s}" % (guide_name, guide_subtitle)

# enable author directives
show_authors = True

# figures
numfig = True

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version = '0.1'
# The full version, including alpha/beta/rc tags.
# release = '0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
#language = english

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'README.md', 'reference', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'sphinx_rtd_theme'
#import sphinx_pdj_theme
#html_theme = 'sphinx_pdj_theme'
#html_theme_path = [sphinx_pdj_theme.get_html_theme_path()]
html_theme = 'piccolo_theme'

html_short_title = "PyPop"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = { # these are both piccolo theme-specific
    "source_url": 'https://github.com/alexlancaster/pypop/',
    "banner_text": 'PyPop v0.7.0 binaries are deprecated, please check the <a href="https://github.com/alexlancaster/pypop#readme">README</a> for compiling from source'
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# put all files that should be root of the pypop.org/ webserver into this directory
# and they will be included in the build directory (and therefore on the website)
html_extra_path = ['html_root']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
#html_sidebars = {
#    'index': [],
#    '**': [
#        'relations.html',  # needs 'show_related': True theme option to display
#        'searchbox.html',
#    ]
#}

#html_sidebars = { 'index': [], '**': ['localtoc.html'] } 


# -- Options for LaTeX output ---------------------------------------------

latex_show_urls = 'inline'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''\DeclareRobustCommand{\and}{%
\end{tabular}\kern-\tabcolsep\\\begin{tabular}[t]{c}%
}%''',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',

    'maketitle': r'\newcommand\sphinxbackoftitlepage{\sphinxstrong{%s}\\ \\Copyright © 2003-2009 Regents of the University of California.\\Copyright © %s \\ \\Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with no Invariant Sections no Front-Cover Texts and no Back-Cover Texts. A copy of the license is included in the License chapter.\\}\sphinxmaketitle' % (guide_name, copyright),

    # margins
    'sphinxsetup': 'hmargin=0.8in, vmargin={1in,0.9in}',

}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).

latex_documents = [('docs/index', guide_prefix+'.tex', guide_name, author, 'manual'),]
pdf_documents = [('docs/index', guide_prefix, guide_name, author),]
