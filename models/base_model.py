#!/usr/bin/python3
"""
Module: base_model.py
Methods included:
    - __init__
      * public instance attr:
          - created_at
          - updated_at
          - id
    - __str__
    - save
    - to_dict
"""


from datetime import datetime
import json
import uuid


class BaseModel:
    """
    create a base class
    """
    def __init__(self):
        """
        initialize all public instances
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        """
        return a string with classname, id, dictionary
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        updating the updated_at datetime
        """
        self.updated_at = datetime.now().isoformat()
        return self.updated_at

    def to_dict(self):
        """
        return a dictionary with new keys and updated class name
        """
        dictionary = self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        dictionary['updated_at'] = self.updated_at
        dictionary['created_at'] = self.created_at

        return dictionary
