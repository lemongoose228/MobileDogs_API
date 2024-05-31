from setuptools import setup, find_packages

setup(
   name='MobileDogs_API',
   version='1.0',
   description='For vector operations',
   license='MIT',
   author='Oksana Galiulina, Konova Ekaterina',
   author_email='oksana17.06@bk.ru',
   url='https://github.com/mgwoorl/my_project2',
   packages=find_packages(exclude=['test']), 
   install_requires=['numpy'],
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
