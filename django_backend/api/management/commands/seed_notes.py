from django.core.management.base import BaseCommand
from api.models import Note


# PUBLIC_INTERFACE
class Command(BaseCommand):
    """Seed the database with example notes."""
    help = "Seeds the database with sample notes for development/testing."

    def handle(self, *args, **options):
        samples = [
            {"title": "Welcome to Notes", "content": "This is your first note."},
            {"title": "Django REST Framework", "content": "Build APIs quickly."},
            {"title": "PostgreSQL Integration", "content": "Configured via env vars."},
        ]
        created = 0
        for data in samples:
            obj, was_created = Note.objects.get_or_create(title=data["title"], defaults={"content": data["content"]})
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Seed complete. Created {created} notes."))
