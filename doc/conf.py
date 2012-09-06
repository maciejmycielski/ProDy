# -*- coding: utf-8 -*-
#
# ProDy documentation build configuration file, created by
# sphinx-quickstart on Wed Sep 15 21:31:37 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os, os.path, time

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.todo', 
              'sphinx.ext.autodoc', 
              'sphinx.ext.doctest', 
              'sphinx.ext.coverage', 
              'sphinx.ext.graphviz',
              'sphinx.ext.ifconfig', 
              'sphinx.ext.viewcode',
              'sphinx.ext.intersphinx', 
              'sphinx.ext.inheritance_diagram', 
              'matplotlib.sphinxext.mathmpl',
              'matplotlib.sphinxext.plot_directive',
              'matplotlib.sphinxext.only_directives',
              'sphinxcontrib.googleanalytics',
              'sphinxcontrib.googlechart',
              'sphinxcontrib.youtube',]#, 'sphinxcontrib.spelling']
               #'sphinx.ext.pngmath',

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = u'ProDy'
copyright = u'2010-2012, Ahmet Bakan'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
def getRevisionNumber():
    from subprocess import PIPE, Popen
    pipe = Popen('git log --summary'.split(), stdout=PIPE, stderr=PIPE)
    return str(pipe.stdout.read().count('Author:'))
version = '1.2.1'
# The full version, including alpha/beta/rc tags.
release =  version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['prody.']

doctest_global_setup = "from prody import *"

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

html_index = 'index.html'

# Custom sidebar templates, maps document names to template names.
# 'sourcelink.html'
generic_sidebars = ['docversion.html', 'howtocite.html', 'localtoc.html', 
                    'relations.html', 'searchbox.html']
html_sidebars = {
    'index': ['slideshow.html', 'docversion.html', 'howtocite.html', 
              'getprody.html', 'getintouch.html', 'searchbox.html',], 
    'genindex': ['searchbox.html'],  
    'py-modindex': ['searchbox.html'],  
    'search': [],
    'tutorial': ['docversion.html', 'howtocite.html', 'localtoc.html', 
                 'codesnippets.html', 'searchbox.html'],
    'bibliography': generic_sidebars,
    'changes': generic_sidebars,
    'contents': generic_sidebars,
    'credits': generic_sidebars,
    'features': generic_sidebars,
    'getprody': ['howtocite.html', 'localtoc.html', 'relations.html', 
                 'searchbox.html'],
    'license': generic_sidebars,
    'publications': generic_sidebars,
    'examples/index': generic_sidebars,
    'reference/index': generic_sidebars,
    'reports/index': generic_sidebars,
    'scripts/index': generic_sidebars,
    'todo': generic_sidebars,
    'plugins/index': ['slideshow.html'] + generic_sidebars,
    'plugins/getnmwiz': ['slideshow.html'] + generic_sidebars,
    '**': ['docversion.html', 'howtocite.html', 'localtoc.html', 
           'relations.html', 'codesnippets.html', 'searchbox.html']}
#html_sidebars = {'index': ['indexsidebar.html', 'searchbox.html']}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {'index': 'index.html'}

# If true, the reST sources are included in the HTML build as _sources/<name>.
html_copy_source = False

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'ProDydoc'

# Plot directive configuration
# ----------------------------

plot_basedir = os.path.join(os.getcwd(), '_build', 'plot_directive')
plot_working_directory = os.path.join(os.getcwd(), 'doctest')

plot_formats = [('png', 80), ('pdf', 80)]

plot_pre_code = """import numpy as np
from prody import *
from matplotlib import pyplot as plt
"""

plot_template = """
{{ source_code }}

{{ only_html }}


   {% for img in images %}
   .. figure:: {{ build_dir }}/{{ img.basename }}.png
      {%- for option in options %}
      {{ option }}
      {% endfor %}

      {{ caption }}
   {% endfor %}

{{ only_latex }}

   {% for img in images %}
   .. image:: {{ build_dir }}/{{ img.basename }}.pdf
   {% endfor %}

"""
plot_rcparams = {'font.size': 10,
                 'xtick.labelsize': 'small',
                 'ytick.labelsize': 'small',
                 'figure.figsize': [5., 4.],}
plot_apply_rcparams = True


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('contents', 'ProDy.tex', u'ProDy Documentation',
   u'Ahmet Bakan', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '_static/logo.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

latex_elements = {
    'fontpkg': '\\usepackage{palatino}',
}

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'prody', u'ProDy Documentation',
     [u'Ahmet Bakan'], 1)
]

autodoc_member_order = 'groupwise'
autodoc_default_flags = []# ['members', 'undoc-members', 'show-inheritance']
autoclass_content = 'both'
todo_include_todos = True

googleanalytics_enabled = True
googleanalytics_id = 'UA-19801227-1'

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'matplotlib': ('http://matplotlib.sourceforge.net/', None), 
    'python': ('http://docs.python.org/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
    'scipy': ('http://docs.scipy.org/doc/scipy/reference/', None)
}

rst_epilog = u"""

.. |pdf| image:: /_static/pdf.png

.. |more| image:: /_static/more.png

.. |example| image:: /_static/example.png

.. |bulb| image:: /_static/bulb.png

.. |new| image:: /_static/new.png

.. |nmwiz| replace:: http://www.csb.pitt.edu/NMWiz/

.. |vmd| replace:: http://www.ks.uiuc.edu/Research/vmd/

.. |pdb| replace:: http://www.pdb.org/

.. |mdanalysis| replace:: http://code.google.com/p/mdanalysis/

.. |pyparsing| replace:: http://pyparsing.wikispaces.com/

.. |matplotlib| replace:: http://matplotlib.sourceforge.net

.. |docrelease| replace:: Documentation release r{0:s}

.. |biopython| replace:: http://biopython.org/

.. |pypi| replace:: http://pypi.python.org/pypi/ProDy

.. |anm| replace:: http://ignmtest.ccbb.pitt.edu/cgi-bin/anm/anm1.cgi

.. |A2| replace:: Å\ :sup:`2`

.. |questions| replace:: To receive new release announcements, join our 
   ProDy-News Google Group: http://groups.google.com/group/prody-news
    
.. |suggestions| replace:: Suggestions, feature requests, or
   problems? Submit them to the GitHub issue tracker: 
   https://github.com/abakan/ProDy/issues

""".format(getRevisionNumber())
