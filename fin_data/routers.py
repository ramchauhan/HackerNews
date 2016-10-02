from django.conf import settings

class FinAppDatabaseRouter(object):
    """
    A router to control all database operations on models in
    the fina_data application
    """

    def db_for_read(self, model, **hints):
        """
        Point all operations on find_data models to mysql DB
        """
        import pdb; pdb.set_trace()
        if settings.DATABASE_APPS_MAPPING.has_key(model._meta.app_label):
            return settings.DATABASE_APPS_MAPPING[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        """
        Point all operations on find_data models to mysql DB
        """
        if settings.DATABASE_APPS_MAPPING.has_key(model._meta.app_label):
            return settings.DATABASE_APPS_MAPPING[model._meta.app_label]
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """All find_data models end up in this pool."""
        if db in settings.DATABASE_APPS_MAPPING.values():
            return settings.DATABASE_APPS_MAPPING.get(app_label) == db
        return None
