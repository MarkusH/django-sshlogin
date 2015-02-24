===============
django-sshlogin
===============

.. warning::

    THIS PROJECT IS JUST A PROOF OF CONCEPT AND SHOULD NOT BE USED IN
    PRODUCTION!

Login via SSH generates a token valid for 10 seconds and can be used to
authenticate on a website.

Idea by @RonnyPfannschmidt:
https://twitter.com/ossronny/status/569967507077013505


Usage
=====

.. code-block:: bash

    $ mkdir ~/.ssh
    $ echo 'command="/path/to/bin/python /path/to/manage.py genkey markus",no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty ssh-rsa AAAAB3....WfY9in markus' >> ~/.ssh/authorized_keys
    $ /path/to/bin/python manage.py migrate
    $ /path/to/bin/python manage.py createsuperuser
    Username (leave blank to use 'markus'): 
    Email address: 
    Password:
    Password (again): 
    Superuser created successfully.
    $ /path/to/bin/python manage.py runserver

Login and you should be see:

.. code-block:: bash

    $ ssh sshuser@localhost
    PTY allocation request failed
    Login at

        http://localhost:8000/sshlogin/QVCH0sn7hkxS7k0ITXLQeZozNeba3UM5kLqyUkA1Tq8i9gOvSZeubgr7NIOKd9mzDGy2AUqBQGbYbl6dOeAWeQAzuqqiNzOmx0LvUNNl650j5nvwmTDPDxXiifCfOLP6o0Hpi4Oee14wNEmsYZ3JyOcVQ3FaoQTzqcoDb5KjtkUUOcAW3hCD28ff4c7Nc3oIdRJHqBJL8HPasTUun1WktEZsB1cQ2G7Yvx4DPCVvu3KBrtJ5OIcRQUuv8YiAy3

    Shared connection to localhost closed.
