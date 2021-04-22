import setuptools

with open('readme.md') as file:
    readme = file.read()

setuptools.setup(
    name='omegalul',
    version='1.0.0',
    author='pcranaway',
    author_email='prcanaway@tuta.io',
    description='A Python library for building omegle clients',
    url='https://github.com/pcranaway/omegalul',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    long_readme=readme
)
