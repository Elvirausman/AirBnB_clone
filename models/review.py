#!/usr/bin/python3
"""This module creates a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for managing review objects
	    Desc:
	    place_id (str): The Place id
			    user_id (str): The User id
					   text (str): The text of the review"""

    place_id = ""
    user_id = ""
    text = ""
