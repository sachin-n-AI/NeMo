#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# nemo documentation build configuration file, created by
# sphinx-quickstart on Sat Nov 17 15:55:54 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# infer to show the default.

import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("../../nemo"))

from package_info import __version__


autodoc_mock_imports = [
    'torch',
    'torch.nn',
    'torch.utils',
    'torch.optim',
    'torch.utils.data',
    'torch.utils.data.sampler',
    'torchvision',
    'torchvision.models',
    'torchtext',
    'torch_stft',
    'pytorch_lightning',
    'h5py',
    'kaldi_io',
    'transformers',
    'transformers.tokenization_bert',
    'apex',
    'ruamel',
    'frozendict',
    'inflect',
    'unidecode',
    'librosa',
    'soundfile',
    'sentencepiece',
    'youtokentome',
    'megatron-lm',
    'numpy',
    'dateutil',
    'wget',
    'scipy',
    'pandas',
    'matplotlib',
    'sklearn',
    'braceexpand',
    'webdataset',
    'tqdm',
    'numba',
    'hydra',
    'omegaconf',
    'onnx',
]

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.githubpages",
    "sphinxcontrib.bibtex",
    "sphinx.ext.inheritance_diagram",
]

# Set default flags for all classes.
autodoc_default_options = {'members': None, 'undoc-members': None, 'show-inheritance': True}

locale_dirs = ['locale/']  # path is example but recommended.
gettext_compact = False  # optional.

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "NVIDIA NeMo"
copyright = "2018-, NVIDIA CORPORATION"
author = "NVIDIA CORPORATION"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.


# The short X.Y version.
# version = "0.10.0"
version = __version__
# The full version, including alpha/beta/rc tags.
# release = "0.9.0"
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# NVIDIA Theme - work in progress.
html_theme = 'nvidia_theme'
html_theme_path = ["."]
html_theme_options = {
    'display_version': True,
    'project_version': __version__,
    'project_name': 'NVIDIA NeMo',
    'logo_path': None,
    'logo_only': True,
}

# Sphinx RTD theme.

# html_theme = "sphinx_rtd_theme"
# html_theme_options = {
#    "canonical_url": "",
#    "analytics_id": "",
#    "logo_only": False,
#    "display_version": True,
#    "prev_next_buttons_location": "bottom",
#    "style_external_links": False,
#    "vcs_pageview_mode": "",
#    # Toc options
#    "collapse_navigation": True,
#    "sticky_navigation": True,
#    "navigation_depth": 4,
#    "includehidden": True,
#    "titles_only": False,
# }

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {"**": ["relations.html", "searchbox.html",]}  # needs 'show_related': True theme option to display

html_theme_options = {
    "canonical_url": "",
    "analytics_id": "",
    "style_external_links": False,
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "nemodoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(master_doc, "nemo.tex", "NVIDIA NeMo Documentation", "AI Applications Team", "manual",)]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "nemo", "NVIDIA NeMo Documentation", [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "NVIDIA NeMo ",
        "NeMo Documentation",
        author,
        "NVIDIA Corporation",
        "One line description of project.",
        "Miscellaneous",
    )
]

autoclass_content = 'both'