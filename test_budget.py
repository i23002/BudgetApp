from budget import Budget, write, refine

def test_Budget():
    assert Budget({"initial_deposit": 1000, "food":500, "coffee" : 20, "cloths":30}) == f"CURRENT BALANCE: {450}"
    assert Budget({"initial_deposit":500,"resuturant":500}) == f"CURRENT BALANCE: {0}"
    assert type(Budget({"initial_deposit": 1000, "food":500, "coffee" : 20, "cloths":30}, True)) == list
    assert len(Budget({"initial_deposit": 1000, "food":500, "coffee" : 20, "cloths":30}, True)) == 4

def test_write():
    assert len(write({"initial_deposit": 1000, "food":500, "coffee" : 20, "cloths":30})) == 4
    assert len(write({"initial_deposit":500,"resuturant":500})) == 2
    assert type(write({"initial_deposit": 1000, "food":500, "coffee" : 50, "cloths":30})) == list
    assert len(write({"initial_deposit": 500, "books": 100, "flight": 150})) == 3

def test_refine():
    assert refine({"initial_deposit": 1000, "food":500, "coffee" : 20, "cloths":30}) == (["food","coffee","cloths"],[500,20,30])
    assert refine({"initial_deposit":500,"resturant":500}) == (["resturant"],[500])
    assert refine({"initial_deposit": 1000, "food":500, "coffee" : 50, "cloths":30}) == (["food","coffee","cloths"],[500,50,30])
    assert refine({"initial_deposit": 1000, "food":600,"cloths":30}) == (["food","cloths"],[600,30])