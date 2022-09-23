from setuptools import find_packages, setup

setup(
    name="mmof",
    version="22.0.1",
    description="Mathematical Modelling of Football",
    python_requires=">3.10.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "mplsoccer>=1.1.3",
        "numpy>=1.23.0",
        "pandas>=1.4.3",
        "requests>=2.28.1",  # required by mplsoccer
        # "statsbomb>=0.3.0",
        # "wyscoutapi>=0.0.2",
    ],
    extras_require={
        "dev": [
            "black>=22.6.0",
            "flake8>=5.0.4",
            "isort>=5.10.1",
            "matplotlib>=3.5.3",
            "mypy>=0.971",
            "pytest>=7.1.2",
            "pytest-cov>=3.0.0",
            "scikit-learn>=1.1.2",
            # "statsmodel>=0.13.2",  # not on Python 3.10?
        ]
    },
)
