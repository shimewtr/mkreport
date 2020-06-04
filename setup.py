from setuptools import setup

setup(
    install_requires=["requests", "python-redmine"],
    entry_points={
        "console_scripts": [
            "mkreport = mkreport:main"
        ]
    }
)
