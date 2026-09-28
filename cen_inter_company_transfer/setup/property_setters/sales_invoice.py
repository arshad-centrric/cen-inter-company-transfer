from .utils import set_property


def apply():
    set_property("Sales Invoice", "is_internal_customer", "in_standard_filter", "1")
