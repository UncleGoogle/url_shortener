from setuptools import setup, find_packages


setup(
    name="yaus",
    version="0.1.0",
    description="Yet another url shortener",
    packages=find_packages("src"),
    package_dir={'': 'src'},
    install_requires=[
        "django==4.0",
        "djangorestframework==3.13.1",
    ],
    extras_require={
        "dev": [
            "pip-tools==6.6.2",
            "pytest==7.1.0",
        ]
    },
)