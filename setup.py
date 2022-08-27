from setuptools import find_packages, setup

setup(
    name="mmof",
    version="22.0.1",
    description="Mathematical Modelling of Football",
    python_requires=">3.10.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.23.0",
        "pandas>=1.4.3",
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
        ]
    },
)
