import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from product_app.models import Comments, Product

USERS = [
    {'username': 'sara_j', 'first_name': 'Sara', 'last_name': 'Johnson'},
    {'username': 'ali_r', 'first_name': 'Ali', 'last_name': 'Rezaei'},
    {'username': 'mike_t', 'first_name': 'Mike', 'last_name': 'Thompson'},
    {'username': 'nina_p', 'first_name': 'Nina', 'last_name': 'Patel'},
    {'username': 'omar_h', 'first_name': 'Omar', 'last_name': 'Hassan'},
    {'username': 'lily_c', 'first_name': 'Lily', 'last_name': 'Chen'},
    {'username': 'david_k', 'first_name': 'David', 'last_name': 'Kim'},
    {'username': 'emma_w', 'first_name': 'Emma', 'last_name': 'Wilson'},
    {'username': 'reza_m', 'first_name': 'Reza', 'last_name': 'Moradi'},
    {'username': 'julia_s', 'first_name': 'Julia', 'last_name': 'Smith'},
    {'username': 'carlos_d', 'first_name': 'Carlos', 'last_name': 'Diaz'},
    {'username': 'hana_b', 'first_name': 'Hana', 'last_name': 'Brown'},
    {'username': 'tom_a', 'first_name': 'Tom', 'last_name': 'Anderson'},
    {'username': 'yasmin_f', 'first_name': 'Yasmin', 'last_name': 'Farahani'},
    {'username': 'ben_l', 'first_name': 'Ben', 'last_name': 'Lee'},
    {'username': 'zara_n', 'first_name': 'Zara', 'last_name': 'Nouri'},
    {'username': 'paul_g', 'first_name': 'Paul', 'last_name': 'Garcia'},
    {'username': 'maryam_z', 'first_name': 'Maryam', 'last_name': 'Zadeh'},
    {'username': 'jack_r', 'first_name': 'Jack', 'last_name': 'Roberts'},
    {'username': 'sofia_v', 'first_name': 'Sofia', 'last_name': 'Vega'},
    {'username': 'dan_h', 'first_name': 'Dan', 'last_name': 'Harris'},
    {'username': 'leila_a', 'first_name': 'Leila', 'last_name': 'Ahmadi'},
    {'username': 'chris_m', 'first_name': 'Chris', 'last_name': 'Miller'},
    {'username': 'nora_e', 'first_name': 'Nora', 'last_name': 'Evans'},
    {'username': 'sam_b', 'first_name': 'Sam', 'last_name': 'Baker'},
]

COMMENT_TEMPLATES = [
    'Great product, exactly what I needed. Would buy again.',
    'Fast delivery and good quality. Very satisfied with my purchase.',
    'Works as described. Noticed results within the first week.',
    'Good value for money. Packaging was secure and professional.',
    'Reliable product from a brand I trust. Recommended to friends.',
    'Easy to use and fits well into my daily routine.',
    'Solid quality. Better than similar products I tried before.',
    'Happy with this purchase. Customer service was helpful too.',
    'Effective and gentle. No issues so far after regular use.',
    'Exactly as shown on the site. Will reorder when I run out.',
    'Very pleased overall. Arrived on time and in perfect condition.',
    'Does the job well. A staple in my health and wellness kit.',
    'Impressed with the quality at this price point.',
    'My family uses this regularly and we are all happy with it.',
    'Five stars from me. Simple, practical, and trustworthy.',
    'Good experience from ordering to delivery. Product meets expectations.',
    'Helpful for daily care. I have already suggested it to others.',
    'Well-made and consistent. Will keep using it long term.',
    'Nice product with clear instructions. No complaints at all.',
    'Exceeded my expectations. Glad I found it on Medifit.',
    'Practical and effective. Fits my needs perfectly.',
    'Trustworthy quality. I feel confident using this every day.',
    'Smooth ordering process and a product that actually works.',
    'One of the better items I have bought from this shop.',
    'Comfortable to use and worth the price.',
    'Reliable results and good build quality throughout.',
    'Very good purchase. I would recommend it without hesitation.',
    'Clean design and works great. No side issues for me.',
    'Exactly what I was looking for. Medifit never disappoints.',
    'Quality feels premium. Happy to leave a positive review.',
]


class Command(BaseCommand):
    help = 'Create 25 users and 7 comments for each product'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Delete seeded users and all comments before seeding',
        )

    def handle(self, *args, **options):
        if options['clear']:
            usernames = [user['username'] for user in USERS]
            Comments.objects.all().delete()
            User.objects.filter(username__in=usernames).delete()
            self.stdout.write('Cleared existing comments and seeded users.')

        users = []
        for data in USERS:
            user, created = User.objects.get_or_create(
                username=data['username'],
                defaults={
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                    'email': f"{data['username']}@example.com",
                },
            )
            if created:
                user.set_password('medifit123')
                user.save()
            users.append(user)

        products = Product.objects.all().order_by('id')
        comments_to_create = []
        random.seed(42)

        for product in products:
            if Comments.objects.filter(product=product).count() >= 7:
                continue

            existing_count = Comments.objects.filter(product=product).count()
            needed = 7 - existing_count
            chosen_users = random.sample(users, k=min(needed, len(users)))

            for index, user in enumerate(chosen_users):
                comments_to_create.append(
                    Comments(
                        product=product,
                        user=user,
                        rate=random.randint(3, 5),
                        comment=f'{COMMENT_TEMPLATES[(product.id + index) % len(COMMENT_TEMPLATES)]} ({product.name})',
                    )
                )

        Comments.objects.bulk_create(comments_to_create, batch_size=500)

        self.stdout.write(
            self.style.SUCCESS(
                f'Done: {len(users)} users ready, {len(comments_to_create)} comments created. '
                f'Total comments: {Comments.objects.count()}.'
            )
        )
