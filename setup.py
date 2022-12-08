from setuptools import find_packages, setup

setup(
    name='kgraph-lib',
    packages=find_packages(include = ['kgraph']),
    version='0.1.1',
    description='k-means reimagined for graphs',
    author='Visaj Nirav Shah',
    license='MIT',
    install_requires = ['networkx', 'pandas', 'numpy', 'scikit-learn', 'scipy==1.8.1']
)
