
from .validate import (
    List,
    Object,
    NullContract,
    EnumContract,
    FloatContract,
    RangeContract,
    RegExContract,
    LengthContract,
    StringContract,
    IntegerContract,
    BooleanContract,
    KeyMissingContract,
)


__all__ = ['String', 'Integer', 'Float', 'Boolean', 'Object', 'List']


class String(KeyMissingContract, NullContract, StringContract, RegExContract, LengthContract, EnumContract):
    """Composition/Mixins for String"""
    pass


class Integer(KeyMissingContract, NullContract, IntegerContract, RangeContract, EnumContract):
    """Composition/Mixins for Integer"""
    pass


class Float(KeyMissingContract, NullContract, FloatContract, RangeContract, EnumContract):
    """Composition/Mixins for Float"""
    pass


class Boolean(KeyMissingContract, NullContract, BooleanContract):
    """Composition/Mixins for Boolean"""
    pass