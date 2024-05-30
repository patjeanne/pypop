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
sys.path.insert(0, os.path.abspath('../src'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosectionlabel',
              'myst_parser', 'rst2pdf.pdfbuilder',
              'sphinx_togglebutton', 'sphinxarg.ext', 'sphinx_copybutton',
              'sphinxcontrib.bibtex']

# override user-agent so that linkcheck works
# FIXME: disabled, doesn't currently have an effect
#user_agent= "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0"

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
copyright = '2024 PyPop contributors'

author_list = ["Alexander K. Lancaster", "Mark P. Nelson", "Diogo Meyer", "Richard M. Single", "Owen D. Solberg"]
author = "\\and ".join(author_list)
htmlauthor = ", ".join(author_list)

# enable author directives
show_authors = True

# figures
numfig = True

# override default text on toggle buttons (sphinx_togglebutton extension)
togglebutton_hint = "Click to show"
togglebutton_hint_hide = "Click to hide"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

from setuptools_scm import get_version

# The full version, including alpha/beta/rc tags, don't normalize for documentation
full_release = get_version('..', normalize=True, version_scheme="post-release")
# The version without the .post or .dev variants
version = full_release.split('.post')[0]
release = version # make the release and version be the same

guide_prefix = 'pypop-guide-' + release # include version in PDF filename
guide_name = 'PyPop User Guide'
guide_subtitle = 'User Guide for Python for Population Genomics'
guide_name_with_subtitle = "%s \\\\{\\LARGE %s}" % (guide_name, guide_subtitle)
guide_pdf_link = "`PDF <../%s.pdf>`__" % guide_prefix

#from PyPop import __pkgname__
# other substitutions
rst_epilog = """
.. |pkgname| replace:: %s
.. |htmlauthor| replace:: %s 
.. |full_release| replace:: %s
.. |guide_pdf_link| replace:: %s
""" % ("``pypop-genomics``", htmlauthor, full_release, guide_pdf_link)

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

# -- Bibligraphy output using sphinxcontrib-bibtex --------------------------------------

bibtex_bibfiles = ['pypop.bib']

## custom citation styles
## overwrite the default square brackets with round-brackets style

from dataclasses import dataclass, field
import sphinxcontrib.bibtex.plugin

from sphinxcontrib.bibtex.style.referencing import BracketStyle
from sphinxcontrib.bibtex.style.referencing.author_year \
    import AuthorYearReferenceStyle


def bracket_style() -> BracketStyle:
    return BracketStyle(
        left='(',
        right=')',
    )

@dataclass
class MyReferenceStyle(AuthorYearReferenceStyle):
    bracket_parenthetical: BracketStyle = field(default_factory=bracket_style)
    bracket_textual: BracketStyle = field(default_factory=bracket_style)
    bracket_author: BracketStyle = field(default_factory=bracket_style)
    bracket_label: BracketStyle = field(default_factory=bracket_style)
    bracket_year: BracketStyle = field(default_factory=bracket_style)

sphinxcontrib.bibtex.plugin.register_plugin(
    'sphinxcontrib.bibtex.style.referencing',
    'author_year_round', MyReferenceStyle)

bibtex_reference_style = 'author_year_round'

## custom bibligraphy style


import pybtex.plugin
from pybtex.style.formatting.alpha import Style as AlphaStyle
from pybtex.style.names import lastfirst
from pybtex.style.template import sentence, optional, field, words, first_of

class AlphaInitialsStyle(AlphaStyle):

    name = 'alpha-initials'
    default_name_style = 'lastfirst' # put the lastname first
    default_label_style = 'alpha' # 'number' or 'alpha'
    default_sorting_style = 'author_year_title'
    
    def __init__(self, **kwargs):
        super().__init__(abbreviate_names=True, **kwargs) # abbreviate initials

    def format_web_refs(self, e):
        # try for DOI, PubMed or EPrint first, only include URL if not present
        return first_of [
            sentence [
                optional [ self.format_eprint(e) ],
                optional [ self.format_pubmed(e) ],
                optional [ self.format_doi(e) ],
            ],
            optional [ self.format_url(e),
                       optional [ ' (accessed on ', field('urldate'), ')' ] ],
            ]
        
pybtex.plugin.register_plugin('pybtex.style.formatting', 'alpha-initials', AlphaInitialsStyle)

bibtex_default_style = 'alpha-initials'


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
    "banner_text": 'PyPop %s is released! Install: <b><code>pip install pypop-genomics</code></b>.<br/>More installation details in the <em><a href="http://pypop.org/docs/guide-chapter-install.html">User Guide</a></em>.<br/>' % release
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

from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter

# set size of code output in LaTeX backend
class CustomLatexFormatter(LatexFormatter):
    def __init__(self, **options):
        super(CustomLatexFormatter, self).__init__(**options)
        self.verboptions = r"formatcom=\footnotesize"

PygmentsBridge.latex_formatter = CustomLatexFormatter

#latex_show_urls = 'inline'
latex_show_urls = 'footnote'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # make PDF shorter by allowing chapters to start immediately
    'extraclassoptions': 'openany,oneside',
    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''\DeclareRobustCommand{\and}{%
\end{tabular}\kern-\tabcolsep\\\begin{tabular}[t]{c}%
}%
\setcounter{secnumdepth}{1}%

\usepackage{pagenote}
\makepagenote
% \renewcommand*{\notesname}{End Notes}    
\renewcommand*{\notedivision}{\subsubsection*{\notesname}}
\renewcommand*{\pagenotesubhead}[2]{}
    
\usepackage{environ}% http://ctan.org/pkg/environ

\newcommand{\OverwriteEnviron}[1]{%
  \expandafter\let\csname #1\endcsname\relax%
  \expandafter\let\csname end#1\endcsname\relax%
  \expandafter\let\csname env@#1@parse\endcsname\relax%
  \expandafter\let\csname env@#1@save@env\endcsname\relax%
  \expandafter\let\csname env@#1@process\endcsname\relax%
  \NewEnviron{#1}%
}

\usepackage{etoolbox}% http://ctan.org/pkg/etoolbox
\pretocmd{\chapter}{%
  % only print chapter endnotes if there is at least one footnote
  \ifnumcomp{\thepagenote}{>}{0}{ 
   \begingroup
   \scriptsize
   \linespread{0.5} %regulate line spacing
   \printnotes*
   \vfill
   \endgroup
  }{}
}{}{}''',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',

    'maketitle': r'\newcommand\sphinxbackoftitlepage{\sphinxstrong{%s}\\ \\Copyright © 2003-2009 Regents of the University of California.\\Copyright © %s \\ \\Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with no Invariant Sections no Front-Cover Texts and no Back-Cover Texts. A copy of the license is included in the License chapter.\\ \\\emph{Document revision}: %s}\sphinxmaketitle' % (guide_name, copyright, full_release),

    # margins
    'sphinxsetup': 'hmargin=0.8in, vmargin={1in,0.9in}',

}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).

latex_documents = [('docs/index', guide_prefix+'.tex', guide_name, author, 'manual'),]
pdf_documents = [('docs/index', guide_prefix, guide_name, author),]

# override the default literalinclude directive
# this sets the tab width only in LaTeX mode to make sure tab stops stay aligned
# not needed in HTML case, because we want to preserve the tabs for cut-and-paste

from sphinx.directives.code import LiteralInclude
class MyLiteralInclude(LiteralInclude):

    def run(self):
        if 'builder_latex' in tags.tags.keys():
            self.options['tab-width'] = 15  # set default tab-width only in LaTeX mode
            print("LaTeX literalinclude options:", self.options)

        node = LiteralInclude.run(self)[0]  # run original directive
        return [node]

def setup(app):
    app.add_directive('literalinclude', MyLiteralInclude, override=True)

        

        
