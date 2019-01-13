from setuptools import setup, find_packages

setup(
    name="mdx-pmwiki-tables",
    version="0.1",
    packages=['mdx_pmwiki_tables',],
    install_requires=['Markdown>=2.6.11'],
    author="John David Pressman",
    author_email="jd@jdpressman.com",
    description=("Markdown extension that implements PmWiki table syntax. See "
                 "http://www.pmwiki.org/wiki/PmWiki/Tables for more information."),
    license="MIT",
    url="https://github.com/JD-P/mdx_pmwiki_tables")
