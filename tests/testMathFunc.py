import pytest, sys
from pytest_in_60_minutes import mathFunc
from pytest_in_60_minutes.mathFunc import StudentDB 


################################################
#  Test the "add" function 
################################################
# skip only when python version is older than version 3.3
@pytest.mark.skipif(sys.version_info < (3,3), reason="do not run number add test")
def testAdd():
    assert mathFunc.add(7,3) == 10
    assert mathFunc.add(7) == 9
    assert mathFunc.add(10.5, 25.5) == 36.0

    print(">>>>>>>", mathFunc.add(7,3))

@pytest.mark.strings
def testAddStrings():
    result = mathFunc.add("Hello", " World!")
    assert result == "Hello World!"
    assert type(result) is str  # String type 
    assert "Heldo" not in result 

@pytest.mark.parametrize('value1, value2, result',
    [(7,3,10),
     ("Hello", " World!", "Hello World!"),
     (10.5, 25.5, 36)
    ])
def testAddByGroup(value1, value2, result):
    assert mathFunc.add(value1, value2) == result



################################################
#  Test the "multiply" function 
################################################
@pytest.mark.number 
def testMultiply():
    assert mathFunc.multiply(5,5) == 25
    assert mathFunc.multiply(5) == 10
    assert mathFunc.multiply(7) == 14

@pytest.mark.strings
def testMultiplyStrings():
    assert mathFunc.multiply("Hello ", 3) == "Hello Hello Hello "
    
    result = mathFunc.multiply("Hello ")
    assert result == "Hello Hello "
    assert type(result) is str  # String type 
    assert "Hello" in result 


################################################
#  Test for name matching in StudentDB json database 
#   using the pytest fixture 
################################################
# scope="module" allows setup and teardown to be executed only one time 
@pytest.fixture(scope="module") 
def db():
    print("----setup----")
    db = StudentDB()
    db.connect("data.json")
    yield db 

    print("----teardown----")
    db.close()

def testScottData(db):
    scottData = db.getData("Scott")

    assert scottData["id"] == 1
    assert scottData["name"] == "Scott"
    assert scottData["result"] == "pass"

def testMarkData(db):
    scottData = db.getData("Mark")

    assert scottData["id"] == 2
    assert scottData["name"] == "Mark"
    assert scottData["result"] == "fail"

