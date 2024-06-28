class DictToClassUtility:
    def __new__(cls, input_class, **entries):
        # Create an instance of the input class
        instance = input_class.__new__(input_class)

        # Initialize the instance attributes
        instance.__dict__.update(entries)

        return instance
