def details(name, **kwargs):
    print(name)

    print(type(kwargs))
    print(kwargs)

    if "height" in kwargs:
        print("Height",kwargs["height"])

    for key in kwargs:
        print(key, kwargs[key])

details("AKD", height=5.6, age=38)