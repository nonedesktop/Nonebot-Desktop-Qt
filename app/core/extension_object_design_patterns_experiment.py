# The idea here is that our plugins always have two states,
# installed and uninstalled,
# and in the future maybe include enabled and disabled, etc...
# Do you see a problem? We're always in a finite state,
# so here I think we can solve it with a finite state machine,
# or state pattern. This would solve a lot of dirty judgment and reduce errors.


from __future__ import annotations
from abc import ABC, abstractmethod


class Extension:
    _state = None

    def __init__(self, state: State) -> None:
        self.trans_to(state)

    def trans_to(self, state: State):
        self._state = state
        self._state.context = self

    def install(self):
        self._state.handle_install()

    def uninstall(self):
        self._state.handle_uninstall()

    def mannage(self):
        self._state.handle_manage()


class State(ABC):
    @property
    def context(self) -> Extension:
        return self._context

    @context.setter
    def context(self, context: Extension) -> None:
        self._context = context

    @abstractmethod
    def handle_install(self) -> None:
        pass

    @abstractmethod
    def handle_uninstall(self) -> None:
        pass

    @abstractmethod
    def handle_manage(self) -> None:
        pass


class UninstalledState(State):
    def handle_install(self) -> None:
        print("Install Extension Done")
        print("Here you go baby, you should trans you state")
        self.context.trans_to(InstalledState())

    def handle_uninstall(self) -> None:
        print("You can not uninstall this cause you dont have it fool")

    def handle_manage(self) -> None:
        print("Install first!!")


class InstalledState(State):
    def handle_install(self) -> None:
        print("You already installed")

    def handle_uninstall(self) -> None:
        print("Uninstall extension")
        print("trans state")
        self.context.trans_to(UninstalledState())

    def handle_manage(self) -> None:
        print("manage")


if __name__ == "__main__":
    # The client code.

    context = Extension(UninstalledState())
    context.install()
    context.uninstall()
