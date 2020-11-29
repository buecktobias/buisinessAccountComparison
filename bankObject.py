import dataclasses


@dataclasses.dataclass
class BankObject:
    bank_name: str
    package_name: str
    price_per_year: float
    description: str
    logo: str
    href: str
