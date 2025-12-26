"""
Setup script for LinkBio - backward compatibility with older pip versions.
"""

from setuptools import setup

# Read the contents of README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="linkbio",
    version="1.0.0",
    description="A modern, brutalist-designed static site generator for link bio pages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Rafnix Guzmán",
    author_email="rafnixg@gmail.com",
    url="https://github.com/rafnixg/linkbio",
    packages=["linkbio"],
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "jinja2>=3.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "isort>=5.10.0",
            "flake8>=4.0.0",
            "mypy>=1.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.2.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "linkbio=linkbio.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    keywords="static-site-generator link-bio jinja2 brutalist-design",
    python_requires=">=3.8",
    project_urls={
        "Homepage": "https://github.com/rafnixg/linkbio",
        "Documentation": "https://linkbio.readthedocs.io/",
        "Repository": "https://github.com/rafnixg/linkbio",
        "Issues": "https://github.com/rafnixg/linkbio/issues",
        "Changelog": "https://github.com/rafnixg/linkbio/blob/main/CHANGELOG.md",
    },
)