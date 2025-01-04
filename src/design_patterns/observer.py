

class AppObserver:

    def __init__(self, name: str) -> None:

        self.name = name
        self.users: list[AppUser] = []

    def register(self, user) -> None:

        self.users.append(user)

    def notify(self, event) -> None:

        for user in self.users:
            user.update(event)


class AppUser:

    def __init__(self, name: str) -> None:

        self.name = name

    def update(self, event) -> None:

        print(f'{self.name} received event: {event}')