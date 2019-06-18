#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from distutils.core import setup

try:
    # 3.x
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    # 2.x
    from distutils.command.build_py import build_py

try:
    import os
    import argparse
    import argcomplete
    import re
    import libxml2
    import csv
    import lxml
    import unidecode
    import shutil
    import doctest
except ImportError, e:
    raise Exception("{}. You must install the missed python module to use csv2xml module.".format(e))

cmdclass = {'build_py': build_py}
command_options = {}

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

test_requirements = [
         # TODO: put package test requirements here
]

setup(
    name='CSV2XML',
    version='0.0.1',
    author='Vauxoo Team',
    author_email='info@vauxoo.com',
    packages=['csv2xml'],
    package_data={'csv2xml': [
        'data/openerp_key.json',
        'data/csv_template/__config__.py',
        'data/csv_template/account_account/*',
        'data/csv_template/account_account_type/*',
        'data/csv_template/account_fiscalyear/*',
        'data/csv_template/account_journal/*',
        'data/csv_template/account_analytic_account/*',
        'data/csv_template/account_analytic_journal/*',
        'data/csv_template/account_analytic_plan/*',
        'data/csv_template/account_analytic_group/*',
        'data/csv_template/account_tax/*',
        'data/csv_template/islr_wh_concept/*',
        'data/csv_template/product_category/*',
        'data/csv_template/product_product/*',
        'data/csv_template/product_uom/*',
        'data/csv_template/product_uom_categ/*',
        'data/csv_template/product_pricelist/*',
        'data/csv_template/res_bank/*',
        'data/csv_template/res_company/*',
        'data/csv_template/res_currency/*',
        'data/csv_template/sale_shop/*',
        'data/csv_template/stock_location/*',
        'data/csv_template/stock_warehouse/*',
        'data/csv_template/res_users/*',
        'data/csv_template/res_partner/*',
        'data/csv_template/res_country_state/*',
        'data/csv_template/payment_term/*',
        'data/csv_template/hr/*',
        'data/csv_template/stock_warehouse_orderpoint/*',
        'data/csv_template/ir_sequence/*',
        'data/csv_template/ir_config/*',
        'data/csv_template/ir_mail_server/*',
        'data/csv_template/fetchmail_server/*',
        'data/csv_template/res_groups/*',
        ]},
    scripts=['bin/csv2xml'],
    #~ url='http://pypi.python.org/pypi/.../',
    #~ license='LICENSE.txt',
    description='Updating odoo module xml data tool via csv files.',
    keywords= ['odoo', 'csv', 'xml'],
    long_description=open('README.rst').read(),
    #~ install_requires=[],
    cmdclass=cmdclass,
    command_options=command_options,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
