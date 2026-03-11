from django.core.management.base import BaseCommand
from django.db import connection
from ...models import MstQAReviewProcedure


class Command(BaseCommand):
    help = "Sync QA review stored procedures from database"

    def handle(self, *args, **options):
        query = """
            SELECT routine_name
FROM information_schema.ROUTINES
WHERE routine_schema = DATABASE()
  AND routine_type = 'PROCEDURE'
ORDER BY routine_name;
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

        created = 0
        for (proc_name,) in rows:
            _, is_created = MstQAReviewProcedure.objects.get_or_create(
                txt_proc_name=proc_name
            )
            if is_created:
                created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"QA Review Procedures synced successfully. New added: {created}"
            )
        )
