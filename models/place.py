#!/usr/bin/python3
"""This is the place class"""
import models
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import ForeignKey, MetaData, Table
from sqlalchemy.orm import relationship


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id",
                             String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id",
                             String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))

class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        __tablename__: represents the table places
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if environ.get('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """Getter property for FileStorage
            """
            list_reviews = []
            place_reviews = models.storage.all(Review)
            for pl_review in place_reviews.values():
                if pl_review.place_id == self.id:
                    list_reviews.append(pl_review)
            return list_reviews

        @property
        def amenities(self):
            """amenities getter property for FileStorage
            """
            all_amenities = models.storage.all(models.Amenity)
            place_amenities = []
            for amenity_obj in all_amenities.values():
                for a_id in amenity_ids:
                    if a_id == amenity_obj.id:
                        all_amenities.append(amenity_ins)
            return place_amenities

        @amenities.setter
        def amenities(self, obj):
            """amenities setter property for FileStorage
            """
            if isinstance(obj, models.Amenity):
                self.amenity_ids.append(obj.id)
