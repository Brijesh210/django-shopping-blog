import pytest

#  making own fixture, with decorater
#  fixture whenever are use they use, alphabetically,
#  instead of mark, we can use db fixture ,
@pytest.fixture(autouse=True)
def aaa_db(db):
    pass
