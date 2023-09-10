from django.contrib.sessions.backends.db import SessionStore as DbSessionStore

""" 
Custom session backend to preserve same session_key on login.
Ensures AnonymousUser cart is added to User cart on login.
"""


class SessionStore(DbSessionStore):
    def cycle_key(self):
        pass
