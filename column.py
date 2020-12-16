import dataclasses


@dataclasses.dataclass
class Column:
    name: str
    can_be_sorted: bool
    sort_name: str
    currently_sorted: bool
    ascending_sorted: bool
