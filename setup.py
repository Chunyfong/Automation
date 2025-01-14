# from distutils.core import setup, Extension
from setuptools import setup, Extension  # 改用 setuptools
from Cython.Build import cythonize

ext = Extension(
    name='df_package',  
    sources=[' .pyx'],  
)

# python setup.py build_ext --inplace

setup(
    name='df_package',
    ext_modules=cythonize(ext, language_level=3),
    install_requires=[
        'pandas',
        'xlwings',
        'python-dotenv',
        'sqlalchemy',
        'pyodbc',
        'openpyxl',
    ]
)
