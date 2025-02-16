# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import mock

# MOCK_MODULES = ['matplotlib', 'matplotlib.pyplot', 'numpy', 'scipy', 'networkx']
# for mod_name in MOCK_MODULES:
# 	sys.modules[mod_name] = mock.Mock()

import os
import sys

# sys.path.insert(0, os.path.abspath('.'))
# sys.path.insert(0, os.path.abspath("../../"))
sys.path.insert(0, os.path.abspath("../.."))
for each_folder_name in os.listdir(os.path.abspath("../../src")):
    sys.path.insert(0, os.path.abspath("../../src/" + each_folder_name))
# sys.path.insert(0, os.path.abspath("../../src/openqaoa-core"))
# sys.path.insert(0, os.path.abspath("../../src/openqaoa-qiskit"))
# sys.path.insert(0, os.path.abspath("../../src/openqaoa-pyquil"))
# sys.path.insert(0, os.path.abspath("../../src/openqaoa-braket"))
# sys.path.insert(0, os.path.abspath("../../src/openqaoa-azure"))
print(sys.path)

# from openqaoa.qaoa_parameters.baseparams import shapedArray


# -- Project information -----------------------------------------------------

project = "OpenQAOA"
copyright = "2022, Entropica Labs"
author = "Entropica Labs"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.mathjax",
    "IPython.sphinxext.ipython_console_highlighting",
    "nbsphinx",
    "sphinx.ext.intersphinx",
]

autodoc_mock_imports = [
    "openqaoa.backends.plugin_finder",
    "botocore",
    "qiskit_aer",
    "pyquil",
    "azure",
    "boto3",
    "qcs_api_client",
    "qiskit_ibm_provider",
    "qiskit",
    "braket",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    ".docs/source/notebooks/community_tutorials/*",
    ".docs/source/notebooks/X_dumping_data.ipynb",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/1.23", None),
    "np": ("https://numpy.org/doc/1.23", None),
    "scipy": ("https://docs.scipy.org/doc/scipy-1.8.1", None),
}


# Exclude broken python docs
# see https://stackoverflow.com/questions/11417221/sphinx-autodoc-gives-warning-pyclass-reference-target-not-found-type-warning
nitpick_ignore = [("py:class", "type")]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_logo = "../../.github/images/Entropica_logo.png"
# html_favicon ='favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']


# -- More customizations ----------------------------------------------------
# Document __init__ and __call__ functions
# def skip(app, what, name, obj, would_skip, options):
#     if name == "__call__":
#         print("Documenting Call")
#         return False

#     if type(obj) == shapedArray:
#         return True
#     return would_skip


# def setup(app):
#     app.connect(skip)
