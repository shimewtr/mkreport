from setuptools import setup


setup(
    name='mkreport',
    version='0.0.19',
    description='Make daily report and create time entry at redmine',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='wawawatataru',
    author_email='wawawatataru@gmail.com',
    url='https://github.com/wawawatataru/mkreport',
    packages=['mkreport'],
    license='MIT',
    install_requires=["requests", "python-redmine"],
    entry_points={
        "console_scripts": [
            "mkreport = mkreport:main"
        ]
    },
    include_package_data=True
)
