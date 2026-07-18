from decimal import Decimal

from django.core.management.base import BaseCommand

from product_app.models import Brand, Category, Product, ProductDetail

SEED_DATA = [
    {
        'brand': 'Perfectil',
        'category': 'Health care',
        'name': 'Hair Tablet',
        'short_description': 'Cure your hair problem',
        'description': 'Advanced hair growth formula with biotin, zinc, and essential vitamins.',
        'price': Decimal('19.00'),
        'stock': 50,
        'badge': 'new',
        'detail_description': 'Supports healthy hair growth and reduces breakage.',
    },
    {
        'brand': 'MediCare',
        'category': 'Medicine',
        'name': 'Blood Pressure Monitor',
        'short_description': 'Accurate home blood pressure readings',
        'description': 'Large display monitor with voice broadcasting and 99 reading memory.',
        'price': Decimal('45.00'),
        'stock': 30,
        'badge': 'new',
        'detail_description': 'Clinically validated for reliable daily monitoring.',
    },
    {
        'brand': 'HealthPlus',
        'category': 'Health care',
        'name': 'Digital Thermometer',
        'short_description': 'Fast and precise temperature readings',
        'description': 'Contactless infrared thermometer with instant results.',
        'price': Decimal('22.00'),
        'stock': 40,
        'badge': 'discounted',
        'detail_description': 'Ideal for adults and children with fever alerts.',
    },
    {
        'brand': 'VitaLife',
        'category': 'Beauty care',
        'name': 'Omega-3 Capsules',
        'short_description': 'Daily support for skin and heart health',
        'description': 'High-potency fish oil capsules with EPA and DHA.',
        'price': Decimal('15.00'),
        'stock': 60,
        'badge': 'discounted',
        'detail_description': 'Promotes radiant skin and cardiovascular wellness.',
    },
    {
        'brand': 'Perfectil',
        'category': 'Fitness',
        'name': 'Swim Goggles',
        'short_description': 'Wide-view goggles for training sessions',
        'description': 'Anti-fog swim goggles with nose cover for comfort and clarity.',
        'price': Decimal('18.00'),
        'stock': 25,
        'badge': 'new',
        'detail_description': 'Designed for adults with a secure, leak-proof fit.',
    },
    {
        'brand': 'MediCare',
        'category': 'Medicine',
        'name': 'Nebulizer Mask Set',
        'short_description': 'Comfortable respiratory therapy mask',
        'description': 'Soft silicone mask compatible with most nebulizer devices.',
        'price': Decimal('12.00'),
        'stock': 35,
        'badge': 'new',
        'detail_description': 'Easy to clean and suitable for daily use.',
    },
    {
        'brand': 'HealthPlus',
        'category': 'Health care',
        'name': 'Vitamin D3 Drops',
        'short_description': 'Boost immunity and bone strength',
        'description': 'Liquid vitamin D3 drops for easy daily supplementation.',
        'price': Decimal('14.00'),
        'stock': 45,
        'badge': 'discounted',
        'detail_description': 'One dropper delivers your daily recommended dose.',
    },
    {
        'brand': 'VitaLife',
        'category': 'Beauty care',
        'name': 'Collagen Peptides',
        'short_description': 'Youthful skin and joint support',
        'description': 'Hydrolyzed collagen powder that mixes easily into drinks.',
        'price': Decimal('28.00'),
        'stock': 20,
        'badge': 'new',
        'detail_description': 'Unflavored formula with 10g collagen per serving.',
    },
    {
        'brand': 'Perfectil',
        'category': 'Fitness',
        'name': 'Resistance Bands Set',
        'short_description': 'Full-body workout at home',
        'description': 'Set of five latex bands with varying resistance levels.',
        'price': Decimal('24.00'),
        'stock': 55,
        'badge': 'discounted',
        'detail_description': 'Includes door anchor and carry pouch.',
    },
    {
        'brand': 'MediCare',
        'category': 'Medicine',
        'name': 'First Aid Kit',
        'short_description': 'Essential supplies for emergencies',
        'description': 'Compact kit with bandages, antiseptic wipes, and gauze.',
        'price': Decimal('32.00'),
        'stock': 15,
        'badge': 'new',
        'detail_description': 'Perfect for home, travel, and office use.',
    },
    {
        'brand': 'HealthPlus',
        'category': 'Medicine',
        'name': 'Pain Relief Gel',
        'short_description': 'Fast-acting topical pain relief',
        'description': 'Cooling gel for muscle and joint discomfort.',
        'price': Decimal('11.00'),
        'stock': 40,
        'badge': 'discounted',
        'detail_description': 'Non-greasy formula absorbs quickly.',
    },
    {
        'brand': 'VitaLife',
        'category': 'Health care',
        'name': 'Multivitamin Complex',
        'short_description': 'Complete daily vitamin support',
        'description': 'Balanced blend of essential vitamins and minerals.',
        'price': Decimal('20.00'),
        'stock': 50,
        'badge': 'new',
        'detail_description': 'One tablet covers your daily nutritional basics.',
    },
    {
        'brand': 'Perfectil',
        'category': 'Beauty care',
        'name': 'Hydrating Face Cream',
        'short_description': 'Deep moisture for dry skin',
        'description': 'Lightweight cream with hyaluronic acid and ceramides.',
        'price': Decimal('26.00'),
        'stock': 30,
        'badge': 'new',
        'detail_description': 'Suitable for sensitive and dry skin types.',
    },
    {
        'brand': 'MediCare',
        'category': 'Fitness',
        'name': 'Yoga Mat',
        'short_description': 'Non-slip mat for home workouts',
        'description': 'Extra-thick mat with carrying strap included.',
        'price': Decimal('35.00'),
        'stock': 25,
        'badge': 'discounted',
        'detail_description': 'Provides cushioning for joints during exercise.',
    },
    {
        'brand': 'HealthPlus',
        'category': 'Medicine',
        'name': 'Antiseptic Spray',
        'short_description': 'Clean wounds and prevent infection',
        'description': 'Alcohol-free antiseptic spray for minor cuts.',
        'price': Decimal('9.00'),
        'stock': 60,
        'badge': 'new',
        'detail_description': 'Gentle enough for family first aid use.',
    },
    {
        'brand': 'VitaLife',
        'category': 'Health care',
        'name': 'Probiotic Capsules',
        'short_description': 'Support digestive health daily',
        'description': '10 billion CFU probiotic blend for gut balance.',
        'price': Decimal('23.00'),
        'stock': 35,
        'badge': 'discounted',
        'detail_description': 'Take one capsule with breakfast.',
    },
    {
        'brand': 'Perfectil',
        'category': 'Medicine',
        'name': 'Hand Sanitizer 500ml',
        'short_description': 'Kills 99.9% of germs',
        'description': 'Moisturizing hand sanitizer with aloe vera.',
        'price': Decimal('8.00'),
        'stock': 80,
        'badge': 'new',
        'detail_description': 'Large bottle ideal for home and office.',
    },
    {
        'brand': 'MediCare',
        'category': 'Beauty care',
        'name': 'Sunscreen SPF 50',
        'short_description': 'Broad-spectrum UV protection',
        'description': 'Lightweight sunscreen for face and body.',
        'price': Decimal('17.00'),
        'stock': 45,
        'badge': 'new',
        'detail_description': 'Water-resistant for up to 80 minutes.',
    },
    {
        'brand': 'HealthPlus',
        'category': 'Fitness',
        'name': 'Foam Roller',
        'short_description': 'Release muscle tension after workouts',
        'description': 'High-density foam roller for recovery sessions.',
        'price': Decimal('21.00'),
        'stock': 20,
        'badge': 'discounted',
        'detail_description': 'Ideal for back, legs, and shoulders.',
    },
    {
        'brand': 'VitaLife',
        'category': 'Medicine',
        'name': 'Cough Syrup',
        'short_description': 'Soothe dry and chesty coughs',
        'description': 'Honey-based syrup for day and night relief.',
        'price': Decimal('13.00'),
        'stock': 55,
        'badge': 'new',
        'detail_description': 'Suitable for adults and children over 6.',
    },
    {
        'brand': 'Perfectil',
        'category': 'Health care',
        'name': 'Electrolyte Powder',
        'short_description': 'Rehydrate after exercise or illness',
        'description': 'Orange-flavored electrolyte mix with key minerals.',
        'price': Decimal('16.00'),
        'stock': 40,
        'badge': 'discounted',
        'detail_description': 'Dissolves instantly in cold water.',
    },
    {
        'brand': 'MediCare',
        'category': 'Beauty care',
        'name': 'Lip Balm Set',
        'short_description': 'Keep lips soft and protected',
        'description': 'Set of three nourishing lip balms with SPF.',
        'price': Decimal('10.00'),
        'stock': 70,
        'badge': 'new',
        'detail_description': 'Includes vanilla, berry, and mint flavors.',
    },
    {
        'brand': 'HealthPlus',
        'category': 'Medicine',
        'name': 'Allergy Relief Tablets',
        'short_description': '24-hour hay fever relief',
        'description': 'Non-drowsy antihistamine for seasonal allergies.',
        'price': Decimal('14.00'),
        'stock': 65,
        'badge': 'discounted',
        'detail_description': 'One tablet provides all-day symptom control.',
    },
    {
        'brand': 'VitaLife',
        'category': 'Fitness',
        'name': 'Jump Rope',
        'short_description': 'Cardio training anywhere',
        'description': 'Adjustable speed rope with comfortable grips.',
        'price': Decimal('12.00'),
        'stock': 35,
        'badge': 'new',
        'detail_description': 'Great for warm-ups and HIIT routines.',
    },
    {
        'brand': 'Perfectil',
        'category': 'Health care',
        'name': 'Sleep Support Melatonin',
        'short_description': 'Fall asleep faster naturally',
        'description': 'Melatonin tablets for occasional sleepless nights.',
        'price': Decimal('18.00'),
        'stock': 28,
        'badge': 'new',
        'detail_description': 'Take 30 minutes before bedtime.',
    },
    {
        'brand': 'MediCare',
        'category': 'Medicine',
        'name': 'Glucose Monitor Strips',
        'short_description': 'Accurate blood sugar testing',
        'description': 'Pack of 50 test strips for compatible monitors.',
        'price': Decimal('29.00'),
        'stock': 22,
        'badge': 'discounted',
        'detail_description': 'Results in five seconds with small sample size.',
    },
    {
        'brand': 'HealthPlus',
        'category': 'Beauty care',
        'name': 'Tea Tree Face Wash',
        'short_description': 'Clear skin without over-drying',
        'description': 'Gentle cleanser with tea tree oil for blemish-prone skin.',
        'price': Decimal('15.00'),
        'stock': 42,
        'badge': 'new',
        'detail_description': 'Use morning and evening for best results.',
    },
    {
        'brand': 'VitaLife',
        'category': 'Fitness',
        'name': 'Ankle Weights 2kg',
        'short_description': 'Add resistance to any workout',
        'description': 'Adjustable ankle weights with soft neoprene padding.',
        'price': Decimal('27.00'),
        'stock': 18,
        'badge': 'discounted',
        'detail_description': 'Secure Velcro straps for a comfortable fit.',
    },
    {
        'brand': 'Perfectil',
        'category': 'Medicine',
        'name': 'Eye Drops',
        'short_description': 'Relief for dry irritated eyes',
        'description': 'Preservative-free lubricating eye drops.',
        'price': Decimal('11.00'),
        'stock': 48,
        'badge': 'new',
        'detail_description': 'Safe for contact lens wearers.',
    },
    {
        'brand': 'MediCare',
        'category': 'Health care',
        'name': 'Iron Supplement',
        'short_description': 'Combat fatigue and low energy',
        'description': 'Gentle iron tablets with vitamin C for absorption.',
        'price': Decimal('19.00'),
        'stock': 33,
        'badge': 'discounted',
        'detail_description': 'Recommended for adults with iron deficiency.',
    },
]


class Command(BaseCommand):
    help = 'Seed the database with sample brands, categories, and products'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Delete existing product data before seeding',
        )

    def handle(self, *args, **options):
        if options['clear']:
            ProductDetail.objects.all().delete()
            Product.objects.all().delete()
            Category.objects.all().delete()
            Brand.objects.all().delete()
            self.stdout.write('Cleared existing product data.')

        brands = {}
        categories = {}

        for item in SEED_DATA:
            brands[item['brand']], _ = Brand.objects.get_or_create(name=item['brand'])
            categories[item['category']], _ = Category.objects.get_or_create(
                name=item['category'],
                defaults={'slug': item['category'].lower().replace(' ', '-')},
            )

        created_count = 0
        for item in SEED_DATA:
            product, created = Product.objects.get_or_create(
                name=item['name'],
                defaults={
                    'brand': brands[item['brand']],
                    'category': categories[item['category']],
                    'short_description': item['short_description'],
                    'description': item['description'],
                    'price': item['price'],
                    'stock': item['stock'],
                },
            )
            if created:
                created_count += 1

            ProductDetail.objects.update_or_create(
                product=product,
                defaults={
                    'description': item['detail_description'],
                    'badge': item['badge'],
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                f'Seed complete: {created_count} new products, '
                f'{Brand.objects.count()} brands, {Category.objects.count()} categories.'
            )
        )
