"""
This is used as an attribute mapper
callable for django-cas per the README at 
https://github.com/fmyzjs/django-cas.
""" 

VERSION = '0.0.1'


def populate_user(user, attributes):
    if attributes is not None:
        if attributes.has_key('is_superuser'):
            user.is_superuser = attributes['is_superuser']

        if attributes.has_key('is_staff'):
            user.is_staff = attributes['is_staff']

        if attributes.has_key('givenName'):
            user.first_name = attributes['givenName']

        if attributes.has_key('sn'):
            user.last_name = attributes['sn']

        if attributes.has_key('email'):
            user.email = attributes['email']

    pass
