import dataclasses


class BaseDto:
    def asdict(self) -> dict:
        """
        Class instance method do return data as dict
        """
        if dataclasses.is_dataclass(self):
            return dataclasses.asdict(self)
        return self.__dict__

    @classmethod
    def make(cls, data):
        """
        Class method to convert 'dict like objects' into Dto
        This method works with classes as well as with dataclasses
        :param data: dict like object
        :return: Dto
        """
        if dataclasses.is_dataclass(cls):
            return cls._make_for_dataclass(data=data)
        return cls._make_for_class(data=data)

    @classmethod
    def _make_for_dataclass(cls, data):
        """
        Protected method to convert dict-like object into dataclass object
        :param data: dict-like object
        :return: dataclass object
        """
        fields_values = {}
        for field in dataclasses.fields(cls):
            if not isinstance(field.default, dataclasses._MISSING_TYPE):
                field_value = field.default
            elif not isinstance(field.default_factory, dataclasses._MISSING_TYPE):
                field_value = field.default_factory()
            else:
                field_value = None
            fields_values[field.name] = field_value
        input_data = {key: value for key, value in dict(data).items() if key in fields_values}
        return cls(**{**fields_values, **input_data})

    @classmethod
    def _make_for_class(cls, data):
        """
        Protected method to convert dict-like object into class object
        :param data: dict-like object
        :return: class object
        """
        return cls(**{key: value for key, value in dict(data).items() if hasattr(cls, key)})
