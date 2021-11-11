from setuptools import setup, find_packages

setup(name="ld_code_exam",
      extra_requires=dict(tests=['pytest']),
      packages=find_packages('src'),
      package_dir={'': 'src'},
)
