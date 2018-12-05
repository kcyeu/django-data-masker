===========
Data Masker
===========

Data Masker is a simple Django app to do data masking. It masks sensitive data
by ``field_name`` and is highly configurable. Currently ``CharField`` and
``EmailField`` are supported.

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
