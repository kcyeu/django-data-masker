===========
Data Masker
===========

Data Masker is a simple Django app to do data masking. It masks sensitive data
by name of form fields and is highly configurable. Currently `CharField <https://docs.djangoproject.com/en/dev/ref/forms/fields/#charfield>`_ and
`EmailField <https://docs.djangoproject.com/en/dev/ref/forms/fields/#emailfield>`_ are supported.

Quick start
-----------

1. Add ``data_masker`` to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'data_masker',
    ]

2. In template, pass the form which contains sensitive data to ``mask_form`` tag
   before any rendering tags.


Example template
----------------

  .. code:: Django

    {# Load the tag library #}
    {% load data_masker %}

    {# Display a form #}
    <form action="/url/to/submit/" method="post" class="form">
      {% csrf_token %}
      {# Mask the form #}
      {% mask_form form as masked_form %}
      {{ masked_form }}

      {# It also works well with django-bootstrap #}
      {% comment %}
      {% bootstrap_form masked_form %}
      {% endcomment %}
      
      <button type="submit">Submit</button>
    </form>
    
Settings
--------
django-data-masker has some pre-configured settings which can be modified by adding variables with ``DATA_MASKER_`` prefix in your ``settings.py`` and customizing the values you want.

+-----------------------------+---------------------------------------------------+---------------------------------------------+
| Variable                    | Usage                                             | Default                                     |
+=============================+===================================================+=============================================+
| DATA_MASKER_CLEAR_HEADING   | Number of heading characters to leave untouched   | 2                                           |
+-----------------------------+---------------------------------------------------+---------------------------------------------+
| DATA_MASKER_CLEAR_TAILING   | Number of tailing characters to leave untouched   | 2                                           |
+-----------------------------+---------------------------------------------------+---------------------------------------------+
| DATA_MASKER_MASK_FULL_EMAIL | Mask full email address including domainname part | False                                       |
+-----------------------------+---------------------------------------------------+---------------------------------------------+
| DATA_MASKER_FIELD_LIST      | List of field name to mask                        | ['account_name', 'account_number', 'email'] |
+-----------------------------+---------------------------------------------------+---------------------------------------------+

