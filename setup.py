"""
    Setup file
"""

import setuptools

setuptools.setup(
    name="latex-linter",
    version="0.0.1",
    author="Hamzeh Idris",
    author_email="idres981@gmail.com",
    description="A linter for LaTex",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    scripts=["main.py", "pages/functions.py"],
    setup_requires=["wheel"],
    entry_points={
        "console_scripts": [
            "latex-linter = main:main",
        ]
    }
)
