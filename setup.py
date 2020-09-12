from setuptools import setup, find_packages

setup(
    name='analyse',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA analyse project package',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas'],
    url='https://github.com/sharonmaswai/edsa_analyse_project',
    author='sharonmaswai',
    author_email='chepsharonmaswai@gamil.com'
)