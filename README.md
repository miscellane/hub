<br>

**The Data Hub**

A repository of small data sets for conducting simple modelling, analysis, and pipeline architecture tests.

<br>
<br>

## GitHub Pages

Launch Sphinx:

```bash
mkdir docs
cd docs
sphinx-quickstart
```

Build:

```bash
sphinx-build -b html docs/source docs/build/html
```


<br>
<br>


## Sphinx

The compilation code is

```shell
  sphinx-build -b html docs/source/ docs/build/html
```

There are a few Sphinx [themes](https://sphinx-themes.org) types.  The `stanford` theme:

* A [demo](https://sphinx-themes.org/sample-sites/sphinx-theme/) of the ``stanford`` theme.
* Installing [`sphinx-theme`](https://sphinx-themes.org/sample-sites/sphinx-theme/#quickstart), the underlying library.
    * [`pip install sphinx-theme`](https://pypi.org/project/sphinx-theme/)

There are [settings for different languages](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language).  Perhaps one of its most important aspects of Sphinx is
[reStructuredText (reST)](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html), i.e.,  the plaintext markup language used by Sphinx.  References of import

* [installing `sphinx`](https://www.sphinx-doc.org/en/master/usage/installation.html)
* [getting started](https://www.sphinx-doc.org/en/master/tutorial/getting-started.html)
* [raw data pass through](https://docutils.sourceforge.io/docs/ref/rst/directives.html#raw-data-pass-through)
* [MathJax](https://docs.mathjax.org/en/latest/web/configuration.html#configuring-and-loading-in-one-script)
* [book theme](https://sphinx-book-theme.readthedocs.io/en/stable/customize/sidebar-secondary.html)
* [sphinx build](https://www.sphinx-doc.org/en/master/man/sphinx-build.html)
* [customising](https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html#adding-custom-css-or-javascript-to-sphinx-documentation)
* [`revitron`](https://github.com/revitron/revitron-sphinx-theme/blob/master/README.rst)
* [Special Characters](https://www.toptal.com/designers/htmlarrows/letters/)

<br>

### Instructions

Populate _``... the master file [docs\source\index.rst](/docs/source/index.rst) and create supplementary documentation
source files. Use the Makefile to build the docs, like so:_

> make builder

_where "builder" is one of the supported builders, e.g. html, latex or linkcheck.''_  Beware, in order to publish these pages via `GitHub Pages` $\rightarrow$

* Add [.nojekyll](/.nojekyll) to the root directory; the [/docs/build/html/.nojekyll](/docs/build/html/.nojekyll) file - automatically created by extension `sphinx.ext.githubpages`, if included in [conf.py](/docs/source/conf.py) -  is insufficient.
* Add an `index.html` file with redirections to the root directory.  The redirection is to the `index.html` built by Sphinx.

<br>

### `revitron` Theme Updates

At present, late 2023, the `revitron` sphinx theme might not render web pages without the hack described herein.  The hack applies
to the `default.html` file of site package `revitron_sphinx_theme`, which resides within the `\Lib\site-packages\` directory
of a python virtual environment.  For example, in the case of a virtual environment named *transcribing*, the `default.html` file
of `revitron_sphinx_theme` resides at

> ~\anaconda3\envs\transcribing\Lib\site-packages\revitron_sphinx_theme\default.html

Within `default.html` append

```text
{# Build sphinx_version_info tuple from sphinx_version string in pure Jinja #}
{%- set (_ver_major, _ver_minor) = (sphinx_version.split('.') | list)[:2] | map('int') -%}
{%- set sphinx_version_info = (_ver_major, _ver_minor, -1) -%}
```

to the template variables settings area, which is at the beginning of the file.  Next, and finally, **replace**

```text
{# CSS #}
<link rel="stylesheet" href="{{ pathto('_static/' + style, 1) }}" type="text/css" />
<link rel="stylesheet" href="{{ pathto('_static/pygments.css', 1) }}" type="text/css" />
```

**with**

```text
{#- CSS #}
{%- if sphinx_version_info < (4, 0) -%}
<link rel="stylesheet" href="{{ pathto('_static/' + style, 1) }}" type="text/css" />
<link rel="stylesheet" href="{{ pathto('_static/pygments.css', 1) }}" type="text/css" />
{%- endif %}
```

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>