from setuptools import setup, find_packages

setup(
    name         = 'shannon_spider',
    version      = '${version}',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = shannon_spider.settings']},
)
