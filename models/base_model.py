#!/usr/bin/python3
"""
Module: base_model.py
Methods included:
    - __init__
      * public instance attr:
          - created_at
          - updated_at
          - id
      * adding args and kwargs
          - if kwargs is not empty: update
          - if kwargs empty: init
    - __str__
    - save
    - to_dict
"""


from datetime import datetime
import uuid


class BaseModel:
    """
    create a base class
    """
    def __init__(self, *args, **kwargs):
        """
        initialize all public instances
        """
        if kwargs:
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass

                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

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
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        return a dictionary with new keys and updated class name
        """
        dictionary = self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        for key, val in dictionary.items():
            if isinstance(val, datetime):
                dictionary[key] = val.isoformat()
        dictionary[key] = val

        return dictionary
