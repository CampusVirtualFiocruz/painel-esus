from ...entities.cbo import CboCollection

def test_cbo_singleton():
    
    cbo1 = CboCollection()
    print( cbo1.cbo_list[0]  )