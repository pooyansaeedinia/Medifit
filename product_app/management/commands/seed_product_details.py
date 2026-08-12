from django.core.management.base import BaseCommand

from product_app.models import Product, ProductBadge, ProductDescription

PRODUCT_DATA = {
    'Hair Tablet': {
        'badge': 'new',
        'descriptions': [
            'Supports healthy hair growth with biotin and zinc.',
            'Reduces breakage after 8 weeks of daily use.',
            'Suitable for men and women with thinning hair.',
            'One tablet per day with meals.',
        ],
    },
    'Blood Pressure Monitor': {
        'badge': 'new',
        'descriptions': [
            'Large display with voice broadcasting.',
            'Stores up to 99 readings for tracking.',
            'Clinically validated for home use.',
            'Includes power adapter and cuff.',
        ],
    },
    'Digital Thermometer': {
        'badge': 'discounted',
        'descriptions': [
            'Contactless infrared readings in one second.',
            'Fever alert for adults and children.',
            'Backlit screen for night-time use.',
        ],
    },
    'Omega-3 Capsules': {
        'badge': 'discounted',
        'descriptions': [
            'High-potency EPA and DHA fish oil.',
            'Supports heart and skin health.',
            'Easy-to-swallow softgel capsules.',
            'Take one capsule daily with food.',
        ],
    },
    'Swim Goggles': {
        'badge': 'new',
        'descriptions': [
            'Anti-fog wide-view lens design.',
            'Comfortable nose cover included.',
            'Secure fit for training sessions.',
        ],
    },
    'Nebulizer Mask Set': {
        'badge': None,
        'descriptions': [
            'Soft silicone for comfortable therapy.',
            'Compatible with most nebulizer devices.',
            'Easy to clean after each use.',
            'Suitable for daily respiratory care.',
        ],
    },
    'Vitamin D3 Drops': {
        'badge': 'discounted',
        'descriptions': [
            'Liquid drops for easy daily dosing.',
            'Supports bone strength and immunity.',
            'Unflavored formula for all ages.',
        ],
    },
    'Collagen Peptides': {
        'badge': 'new',
        'descriptions': [
            '10g hydrolyzed collagen per serving.',
            'Mixes easily into drinks or smoothies.',
            'Unflavored and dissolves quickly.',
            'Supports skin elasticity and joints.',
        ],
    },
    'Resistance Bands Set': {
        'badge': 'discounted',
        'descriptions': [
            'Five bands with varying resistance levels.',
            'Includes door anchor and carry pouch.',
            'Ideal for full-body home workouts.',
        ],
    },
    'First Aid Kit': {
        'badge': 'new',
        'descriptions': [
            'Compact kit for home and travel.',
            'Includes bandages, gauze, and antiseptic wipes.',
            'Organized compartments for quick access.',
        ],
    },
    'Pain Relief Gel': {
        'badge': 'discounted',
        'descriptions': [
            'Fast-acting cooling relief for sore muscles.',
            'Non-greasy formula absorbs quickly.',
            'Suitable for joints and back pain.',
            'Apply up to three times daily.',
        ],
    },
    'Multivitamin Complex': {
        'badge': 'new',
        'descriptions': [
            'Balanced blend of essential vitamins.',
            'Covers daily nutritional basics.',
            'One tablet per day with breakfast.',
        ],
    },
    'Hydrating Face Cream': {
        'badge': 'new',
        'descriptions': [
            'Hyaluronic acid and ceramides formula.',
            'Deep moisture for dry skin types.',
            'Lightweight and non-comedogenic.',
            'Use morning and evening.',
        ],
    },
    'Yoga Mat': {
        'badge': 'discounted',
        'descriptions': [
            'Extra-thick cushioning for joint support.',
            'Non-slip surface for stable poses.',
            'Includes carrying strap.',
        ],
    },
    'Antiseptic Spray': {
        'badge': None,
        'descriptions': [
            'Alcohol-free spray for minor cuts.',
            'Gentle enough for family first aid.',
            'Compact bottle for bags and kits.',
        ],
    },
    'Probiotic Capsules': {
        'badge': 'discounted',
        'descriptions': [
            '10 billion CFU probiotic blend.',
            'Supports digestive balance daily.',
            'Take one capsule with breakfast.',
            'Shelf-stable without refrigeration.',
        ],
    },
    'Hand Sanitizer 500ml': {
        'badge': 'new',
        'descriptions': [
            'Kills 99.9% of common germs.',
            'Moisturizing aloe vera formula.',
            'Large bottle for home or office.',
        ],
    },
    'Sunscreen SPF 50': {
        'badge': 'new',
        'descriptions': [
            'Broad-spectrum UVA and UVB protection.',
            'Water-resistant for up to 80 minutes.',
            'Lightweight finish for face and body.',
            'Dermatologist-tested formula.',
        ],
    },
    'Foam Roller': {
        'badge': 'discounted',
        'descriptions': [
            'High-density foam for muscle recovery.',
            'Ideal for back, legs, and shoulders.',
            'Compact size for gym or home use.',
        ],
    },
    'Cough Syrup': {
        'badge': 'new',
        'descriptions': [
            'Honey-based relief for dry coughs.',
            'Suitable for adults and children over 6.',
            'Day and night formula options.',
        ],
    },
    'Electrolyte Powder': {
        'badge': 'discounted',
        'descriptions': [
            'Replenishes minerals after exercise.',
            'Orange flavor dissolves instantly.',
            'Mix one scoop with cold water.',
            'Low sugar hydration support.',
        ],
    },
    'Lip Balm Set': {
        'badge': None,
        'descriptions': [
            'Set of three nourishing lip balms.',
            'Includes vanilla, berry, and mint.',
            'SPF protection for daily use.',
        ],
    },
    'Allergy Relief Tablets': {
        'badge': 'discounted',
        'descriptions': [
            'Non-drowsy 24-hour hay fever relief.',
            'One tablet covers all-day symptoms.',
            'Works on pollen and dust allergies.',
        ],
    },
    'Jump Rope': {
        'badge': None,
        'descriptions': [
            'Adjustable length speed rope.',
            'Comfortable grip handles.',
            'Great for cardio warm-ups.',
            'Lightweight and portable.',
        ],
    },
    'Sleep Support Melatonin': {
        'badge': 'new',
        'descriptions': [
            'Helps you fall asleep faster naturally.',
            'Take 30 minutes before bedtime.',
            'Non-habit forming formula.',
        ],
    },
    'Glucose Monitor Strips': {
        'badge': 'discounted',
        'descriptions': [
            'Pack of 50 compatible test strips.',
            'Results in five seconds.',
            'Requires only a small blood sample.',
            'For use with supported monitors.',
        ],
    },
    'Tea Tree Face Wash': {
        'badge': 'new',
        'descriptions': [
            'Gentle cleanser for blemish-prone skin.',
            'Tea tree oil helps clear pores.',
            'Use morning and evening.',
        ],
    },
    'Ankle Weights 2kg': {
        'badge': 'discounted',
        'descriptions': [
            'Adjustable neoprene ankle weights.',
            'Secure Velcro strap closure.',
            'Adds resistance to walks and workouts.',
        ],
    },
    'Eye Drops': {
        'badge': None,
        'descriptions': [
            'Preservative-free lubricating drops.',
            'Relief for dry irritated eyes.',
            'Safe for contact lens wearers.',
            'Use as needed throughout the day.',
        ],
    },
    'Iron Supplement': {
        'badge': 'discounted',
        'descriptions': [
            'Gentle iron with vitamin C for absorption.',
            'Helps combat fatigue and low energy.',
            'Recommended for iron deficiency.',
        ],
    },
}


class Command(BaseCommand):
    help = 'Add badges and short descriptions to products'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Remove existing badges and descriptions before seeding',
        )

    def handle(self, *args, **options):
        if options['clear']:
            ProductBadge.objects.all().delete()
            ProductDescription.objects.all().delete()
            self.stdout.write('Cleared existing badges and descriptions.')

        badge_count = 0
        description_count = 0
        no_badge_count = 0
        missing = []

        for product in Product.objects.all():
            data = PRODUCT_DATA.get(product.name)
            if not data:
                missing.append(product.name)
                continue

            ProductBadge.objects.filter(product=product).delete()
            if data['badge']:
                ProductBadge.objects.create(product=product, badge=data['badge'])
                badge_count += 1
            else:
                no_badge_count += 1

            ProductDescription.objects.filter(product=product).delete()
            for text in data['descriptions']:
                ProductDescription.objects.create(product=product, description=text)
                description_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Done: {badge_count} badges, {no_badge_count} products without badges, '
                f'{description_count} descriptions added.'
            )
        )
        if missing:
            self.stdout.write(
                self.style.WARNING(f'No seed data for: {", ".join(missing)}')
            )
