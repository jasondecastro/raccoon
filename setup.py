from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='raccoon',
    version='1.3',
    description='Raccoon is a language wrapper for SQL that makes it easier and more intuitive to write SQL code.',
    long_description="wow",
    author='Jason Decastro',
    author_email='jasonrdecastro@gmail.com',
    url='https://github.com/jasondecastro/raccoon',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    platforms='any',
    zip_safe=False,
    scripts=['bin/raccoon']
)