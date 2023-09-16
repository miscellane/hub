"""
conf.py

Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

Project information
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""

import revitron_sphinx_theme

'''
Basic
'''
project = 'Hub'
copyright = '2023, greyhypotheses'
author = 'greyhypotheses'
release = '0.1'


'''
General configuration
https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
'''

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.githubpages',
    'revitron_sphinx_theme'
]
templates_path = ['_templates']
exclude_patterns = []


'''
Options for HTML output
https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
'''

html_theme = 'revitron_sphinx_theme'

html_static_path = ['_static']

html_css_files = []

html_js_files = ['https://code.jquery.com/jquery-3.7.0.min.js',
                 'https://code.highcharts.com/stock/highstock.js',
                 'https://code.highcharts.com/stock/modules/data.js',
                 'https://code.highcharts.com/stock/modules/exporting.js',
                 'https://code.highcharts.com/stock/modules/export-data.js',
                 'https://code.highcharts.com/stock/modules/accessibility.js',
                 'https://code.highcharts.com/highcharts.js',
                 'https://code.highcharts.com/modules/networkgraph.js',
                 'js/deflator.js']


html_theme_options = {
    'color_scheme': '',
    'canonical_url': 'https://thirdreading.github.io/hub/',
    'analytics_id': '',
    'style_external_links': False,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'github_url': 'https://www.github.com/greyhypotheses',
    'logo_mobile': '_static/logo.svg'
}

html_logo = '_static/logo.svg'

html_context = {
    'landing_page': {
        'menu': [
            {'title': 'Introduction',
             'url': 'introduction/introduction.html'},
            {'title': 'Data',
             'url': 'https://github.com/thirdreading/hub/tree/master/data'},
            {'title': 'Search',
             'url': 'search.html'}
        ]
    }
}
