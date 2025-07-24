from setuptools import setup, find_packages

setup(
    name="snrublist3r",
    version="1.0.0",
    packages=find_packages(),
    py_modules=["snrublist3r"],
    install_requires=[ "aiodns", "beautifulsoup4", "colorama", "lxml", "requests", "tldextract", "tqdm" ],
    entry_points={ "console_scripts": [ "snrublist3r=snrublist3r:main" ] }
)

