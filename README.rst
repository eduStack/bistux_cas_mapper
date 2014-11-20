bistux_cas_mapper
===============

Simple module for mapping cas attributes to django user models 

Example conf::

    EDXAPP_CAS_ATTRIBUTE_PACKAGE: "git+https://github.com/fmyzjs/bistux_cas_mapper"
    EDXAPP_CAS_ATTRIBUTE_CALLBACK:
      module: "bistux_cas_mapper"
      function: "populate_user"
