from abc import ABC, abstractmethod


class Product(ABC):
    """Abstraction: share common attributes and require a delivery method."""

    def __init__(
        self,
        name,
        description,
        price,
        image,
        item_id=0,
        category_id="geral",
        category_name="Geral",
        stack=1,
        stat_label="Atributo",
        stat_value="Padrão",
        lore="",
        villager_id="armeiro",
        villager_name="Ferreiro Gorak",
        villager_role="Mestre Armeiro",
        dimension="overworld",
    ):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price  # Construction also goes through validation.
        self.image = image
        self.category_id = category_id
        self.category_name = category_name
        self.stack = stack
        self.stat_label = stat_label
        self.stat_value = stat_value
        self.lore = lore or description
        self.villager_id = villager_id
        self.villager_name = villager_name
        self.villager_role = villager_role
        self.dimension = dimension

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("The price cannot be negative.")
        # _price is internal by convention; the underscore does not block access.
        self._price = value

    def formatted_price(self):
        # Keep the activity's Brazilian real (BRL) display format.
        return f"R$ {self.price:.2f}".replace(".", ",")

    def emerald_price(self):
        return int(self.price)

    @abstractmethod
    def delivery(self):
        """Each product type must describe its delivery."""


class PhysicalProduct(Product):
    def __init__(self, name, description, price, image, pickup_location, **kwargs):
        super().__init__(name, description, price, image, **kwargs)
        self.pickup_location = pickup_location

    def delivery(self):
        # CUSTOMIZE HERE: delivery message for a physical product.
        return f"Pickup at: {self.pickup_location}."


class DigitalProduct(Product):
    def __init__(self, name, description, price, image, file_format, **kwargs):
        super().__init__(name, description, price, image, **kwargs)
        self.file_format = file_format

    def delivery(self):
        # CUSTOMIZE HERE: informational message, without automatic file delivery.
        return f"Digital delivery in {self.file_format} format."
