from setuptools import setup, find_packages

setup(
    name="quantdash",
    version="0.0.1",
    description="Real-time trading dashboard framework for Python",
    author="Joe Gasewicz",
    author_email="contact@josef.digital",
    packages=find_packages(),  # finds `quantdash/` and submodules
    include_package_data=True,
    install_requires=[
        "tornado",
        "plotly",
        "pandas",
        "marshmallow",
        "jinja2",
        "sqlalchemy",
        "celery",
    ],
    python_requires=">=3.10",
)