"""CreateRugpullTable Migration."""

from masoniteorm.migrations import Migration


class CreateRugpullTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("rugpull") as table:
            table.increments("id")
            table.text("confession")
            table.integer("age")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("rugpull")
