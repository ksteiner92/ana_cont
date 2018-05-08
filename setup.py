from setuptools import setup
from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

#def relScriptPath(script):
#    return os.path.join(rel, script)

#setup(name = 'precomp',\
#      version = '1.0',\
#      description = 'Precomputation of Maxent matrices.',\
#      ext_modules = [Extension('precomp', \
#                               sources = ['precomp.c'],\
#                               libraries=['m'],\
#                               include_dirs=[numpy.get_include()])])
cythonize("ana_cont/pade.pyx")
setup(
    name = "ana_cont",
    version = "0.1",
    author = "Klaus Steiner",
    description = ("An analytical continuation package"),
    license = "MIT",
    #keywords = "example documentation tutorial",
    #url = "http://packages.python.org/an_example_pypi_project",
    #packages=["${PYDQMC_MOD}"],
    #long_description=read(relScriptPath("README.md")),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    packages=["ana_cont"],
    ext_modules = [Extension('precomp', \
                             sources = ['ana_cont/precomp.c'], \
                             libraries=['m'], \
                             include_dirs=[numpy.get_include()]),
                   Extension('pade', \
                             sources = ['ana_cont/pade.c'], \
                             libraries=['m'], \
                             include_dirs=[numpy.get_include()])],
    install_requires=['numpy', 'scipy', 'Cython'],
    setup_requires=['Cython'],
    include_package_data=True,
    zip_safe=False)