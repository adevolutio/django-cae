=====
Usage
=====

To use CAE app in a project, add it to your `INSTALLED_APPS`:

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
