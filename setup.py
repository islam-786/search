from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="search",
    version="1.0.0",
    description="Search engine for Islamic content",
    long_description=long_description,
    long_description_content_type="text/markdown",

    # The project's main homepage.
    url="https://github.com/octabytes/search-api",

    # Author details
    author="OctaByte",
    author_email="dev@octabyte.io",

    # Choose your license
    license="Apache 2.0",

    # Packages information
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'}
)
