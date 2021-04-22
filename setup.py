import setuptools

with open('readme.md') as file:
    readme = file.read()

setuptools.setup(
    name='omegalul',
    version='1.0.2',
    author='pcranaway',
    author_email='pcranaway@tuta.io',
    description='A Python library for building omegle clients',
    url='https://github.com/pcranaway/omegalul',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    long_description=readme,
    long_description_content_type='text/markdown'
)
