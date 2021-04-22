import setuptools

setuptools.setup(
    name='omegalul',
    version='0.0.4',
    author='pcranaway',
    author_email='prcanaway@tuta.io',
    description='A Python library for building omegle clients',
    url='https://github.com/pcranaway/omegalul',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'}
)
