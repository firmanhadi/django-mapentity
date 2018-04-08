import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

test_requires = [
    'mock',
    'factory_boy == 2.8.1',
]

setup(
    name='mapentity',
    version='4.3.4.dev0',
    author='Makina Corpus',
    author_email='geobi@makina-corpus.com',
    url='https://github.com/makinacorpus/django-mapentity',
    download_url="http://pypi.python.org/pypi/mapentity/",
    description="Generic CRUD with maps",
    long_description=(open(os.path.join(here, 'README.rst')).read() + '\n\n' +
                      open(os.path.join(here, 'CHANGES')).read()),
    license='BSD, see LICENSE file.',
    install_requires=[
        'Django>=1.9,<2',
        'GDAL>=1.9',
        'gpxpy',
        'BeautifulSoup4',
        'requests',
        'django-modeltranslation',
        'django-shapes',
        'django-floppyforms',
        'django-crispy-forms',
        'django-compressor',
        'django-filter',
        'easy-thumbnails',
        'django-tinymce',
        'djangorestframework',
        'djangorestframework-gis',
        'django-appypod>=0.0.2',
        'django-leaflet>=0.14',
        'django-geojson>=2',
        'paperclip',
        'WeasyPrint<0.42',  # 0.42 drops support of python 2.7,
        'django-weasyprint==0.1',  # 0.5.x API changed
    ] + test_requires,
    tests_requires=test_requires,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=['Topic :: Utilities',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Intended Audience :: Developers',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Development Status :: 5 - Production/Stable',
                 'Programming Language :: Python :: 2.7'],
)
