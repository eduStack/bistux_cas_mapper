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

        if attributes.has_key('yhlb') and attributes['yhlb'] == 'J0000':
            user.is_staff = True

        if attributes.has_key('xm'):
            user.profile.name = attributes['xm']
        
        if attributes.has_key('email') and attributes['email'] != 'null':
            user.email = attributes['email']
        else:
            if attributes['yhlb'] == 'J0000':
                user.email ='%s@bistu.edu.cn' % user.username
            else:
                user.email ='%s@mail.bistu.edu.cn' % user.username

    pass
