#!/usr/bin/env python
# encoding: utf-8
"""
interfaces.py

Created by Daniel Greenfeld on 2008-12-11.
Copyright (c) 2008. All rights reserved.
"""

from zope.interface import Interface

class IObject(Interface):
    pass
    
class IPloneSchemaObject(Interface):
    portal_type = ''
    portal_type_id = ''
    allowed_content_types = []
    fields = []