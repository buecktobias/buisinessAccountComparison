class BankObjectSorter:
    @classmethod
    def sort_by_price(cls, bank_objects):
        return list(sorted(bank_objects, key=lambda x: x.price_per_year))
