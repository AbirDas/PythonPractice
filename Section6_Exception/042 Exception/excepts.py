try:
    d = {}
    d["Hello"]
    
    print(1/0)
except ZeroDivisionError as ex:
    print("Failed.", ex)
    print(type(ex))
except Exception as e:
    print("Caught in Exception.", e)
    print(type(e))
finally:
    print("Finally!")