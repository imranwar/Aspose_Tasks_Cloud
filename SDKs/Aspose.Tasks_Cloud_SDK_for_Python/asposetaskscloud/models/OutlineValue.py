#!/usr/bin/env python

class OutlineValue(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            'ValueId': 'int',
            'FieldGuid': 'str',
            'Type': 'OutlineValueType',
            'ParentValueId': 'int',
            'Value': 'str',
            'Description': 'str',
            'IsCollapsed': 'bool'

        }

        self.attributeMap = {
            'ValueId': 'ValueId','FieldGuid': 'FieldGuid','Type': 'Type','ParentValueId': 'ParentValueId','Value': 'Value','Description': 'Description','IsCollapsed': 'IsCollapsed'}       

        self.ValueId = None # int
        self.FieldGuid = None # str
        self.Type = None # OutlineValueType
        self.ParentValueId = None # int
        self.Value = None # str
        self.Description = None # str
        self.IsCollapsed = None # bool
        
