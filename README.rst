=============================
CAE app
=============================

.. image:: https://badge.fury.io/py/django-cae.svg
    :target: https://badge.fury.io/py/django-cae

.. image:: https://travis-ci.org/adevolutio/django-cae.svg?branch=master
    :target: https://travis-ci.org/adevolutio/django-cae

.. image:: https://codecov.io/gh/adevolutio/django-cae/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/adevolutio/django-cae

Classificação Portuguesa das Actividades Económicas

Documentation
-------------

The full documentation is at https://django-cae.readthedocs.io.

Quickstart
----------

Install CAE app::

    pip install django-cae

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'cae.apps.CaeConfig',
        ...
    )

Add CAE app's URL patterns:

.. code-block:: python

    from cae import urls as cae_urls


    urlpatterns = [
        ...
        url(r'^', include(cae_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
