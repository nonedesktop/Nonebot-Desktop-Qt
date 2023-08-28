from typing import Callable

from PySide6.QtCore import QObject, QTimer, Signal


class CustomError(Exception):
    def __init__(self, function_name, error_type, error_message) -> None:
        self.function_name = function_name
        self.error_type = error_type
        self.error_message = error_message
        super().__init__(f"Function '{function_name}' encountered a {error_type} error: {error_message}")


class AsyncLoader(QObject):
    Started: Signal = Signal()
    Completed: Signal = Signal()
    Failed: Signal = Signal(CustomError)

    def __init__(self) -> None:
        super().__init__()
        self.timer = QTimer(parent=self)
        self.registered_callable_list: list[Callable] = []
        self._init_timer()

    def _init_timer(self) -> None:
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self._execute)

    def _execute(self) -> None:
        for callable_obj in self.registered_callable_list:
            try:
                callable_obj()
            except Exception as e:
                function_name: str = callable_obj.__name__ if hasattr(callable_obj, "__name__") else str(callable_obj)
                error_type: str = type(e).__name__
                error_message = str(e)
                custom_error = CustomError(function_name, error_type, error_message)
                self.Failed.emit(custom_error)
                continue

        self.Completed.emit()

    def register(self, callable_obj: Callable) -> None:
        if not callable(callable_obj):
            raise ValueError(f"Only callable objects can be registered, got {type(callable_obj)} instead.")

        self.registered_callable_list.append(callable_obj)

    def start_async(self, delay_msec: int = 10) -> None:
        if delay_msec < 0:
            raise ValueError("Delay time must be a non-negative integer.")

        if delay_msec == 0:
            self._execute()
        else:
            self.timer.start(delay_msec)
