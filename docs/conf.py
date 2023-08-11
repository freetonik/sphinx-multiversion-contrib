# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# Find the path to the source files we want to document, relative to the location of this file,
# convert it to an absolute path.
# Sphinx-multiversion checks out the repo at different ref points into tmp directory.
# We're using SPHINX_MULTIVERSION_SOURCEDIR in order to access each such directory.
# See https://github.com/Holzhaus/sphinx-multiversion/issues/42 for details.
default_py_root = os.path.join(os.getcwd(), os.path.dirname(__file__))
py_path = os.path.join(os.getenv('SPHINX_MULTIVERSION_SOURCEDIR', default=default_py_root), '../src')
sys.path.insert(0, os.path.abspath(py_path))

# -- Project information -----------------------------------------------------

project = 'sphinx-multiversion-contrib'
copyright = '2023, IQM Finland Oy'

# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''
try:
    from sphinx_multiversion import __version__ as version
except ImportError:
    pass
else:
    release = version

# -- General configuration ---------------------------------------------------

# Require a recent version of Sphinx
needs_sphinx = '4.5'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
    'sphinx_multiversion',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.*']

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%Y-%m-%d'

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# -- Options for HTML output -------------------------------------------------

import sphinx_book_theme

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [sphinx_book_theme.get_html_theme_path()]

html_context = dict(
    display_github=False
)

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'logo_only': True,
}

html_sidebars = {
    '**': [
        'sidebar-logo.html', 'search-field.html', 'sbt-sidebar-nav.html', 'versioning.html'
    ]
}

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/images/logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/images/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%Y-%m-%d'

# Output file base name for HTML help builder.
htmlhelp_basename = 'sphinx-multiversion-doc'

# -- MathJax options ----------------------------------------------------------

# Here we configure MathJax, mostly to define LaTeX macros.
mathjax3_config = {
    'tex': {
        'macros': {
            'vr': r'\vec{r}',  # no arguments
            'ket': [r'\left| #1 \right\rangle', 1],  # one argument
            'iprod': [r'\left\langle #1 | #2 \right\rangle', 2],  # two arguments
        }
    }
}

# -- External mapping ------------------------------------------------------------

python_version = '.'.join(map(str, sys.version_info[0:2]))
intersphinx_mapping = {
    'python': ('https://docs.python.org/' + python_version, None),
}

# -- Options for sphinx_multiversion --------------------------------------------------
smv_tag_whitelist = r'^[0-9]+\.[0-9]+$'  # Allow tags that match format "X.Y"
smv_branch_whitelist = '$-'  # Exclude all local branches in versions list by using unmatchable pattern
smv_remote_whitelist = '$-'  # Exclude all remote branches in versions list by using unmatchable pattern
smv_released_pattern = r'^refs/tags/.*$'  # Tags recognized as releases
smv_outputdir_format = 'versions/{ref.name}'  # Store versioned docs in a subdirectory
