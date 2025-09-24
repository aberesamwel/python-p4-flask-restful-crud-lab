#!/usr/bin/env python3

import pytest
from app import app
from models import db, Plant

@pytest.fixture(autouse=True)
def setup_database():
    with app.app_context():
        db.create_all()
        
        # Add test data
        aloe = Plant(
            id=1,
            name="Aloe",
            image="./images/aloe.jpg",
            price=11.50,
            is_in_stock=True,
        )
        db.session.add(aloe)
        db.session.commit()
        
        yield
        
        db.drop_all()

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))
