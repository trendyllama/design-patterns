

from src.design_patterns.observer import AppObserver, AppUser, Message


def test_observer():
    observer = AppObserver('observer')

    observer.register(AppUser('user1'))
    observer.register(AppUser('user2'))
    observer.register(AppUser('user3'))

    observer.notify(Message('A new feature was just released!'))
