# database_router.py

class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'user_app':
            return 'user_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'user_app':
            return 'user_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._state.db in ('default', 'user_db') and obj2._state.db in ('default', 'user_db'):
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'user_app':
            return db == 'user_db'
        return db == 'default'
