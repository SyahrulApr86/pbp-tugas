from django.test import TestCase
from katalog.models import CatalogItem

# Create your tests here.

# create test for katalog
class KatalogTest(TestCase):
    def setUp(self):
        CatalogItem.objects.create(
        item_name="ASUS ROG Zephyrus Duo",
        item_price=58999000,
        item_stock=1,
        description="Siapapun tolong beliin saya ini dong",
        rating=10,
        item_url="https://www.tokopedia.com/asus/asus-rog-zephyrus-duo-gx650rw-r97rm7t-o-black?extParam=ivf%3Dfalse&src=topads"
    )

    def testCatalog(self):
        laptop = CatalogItem.objects.get(
            item_name="ASUS ROG Zephyrus Duo",
            item_price=58999000,
            item_stock=1,
            description="Siapapun tolong beliin saya ini dong",
            rating=10,
            item_url="https://www.tokopedia.com/asus/asus-rog-zephyrus-duo-gx650rw-r97rm7t-o-black?extParam=ivf%3Dfalse&src=topads"
        )

        self.assertEqual(laptop.item_name, "ASUS ROG Zephyrus Duo")
        self.assertEqual(laptop.item_price, 58999000)
        self.assertEqual(laptop.item_stock, 1)
        self.assertEqual(laptop.description, "Siapapun tolong beliin saya ini dong")
        self.assertEqual(laptop.rating, 10)
        self.assertEqual(laptop.item_url, "https://www.tokopedia.com/asus/asus-rog-zephyrus-duo-gx650rw-r97rm7t-o-black?extParam=ivf%3Dfalse&src=topads")

