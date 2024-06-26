#!/usr/bin/python3
"""This module creates a User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing/representing city objects
	    Attributes:
        state_id (str): The state id.
        name (str): The name of the city
"""

    state_id = ""
    name = ""
