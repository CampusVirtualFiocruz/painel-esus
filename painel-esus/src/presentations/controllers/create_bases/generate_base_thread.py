import threading


class GenerateBase:
    _instance = None
    _running_thread = None
    _event = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def start(self, target):
        self._event = threading.Event()
        self._running_thread = threading.Thread(
            target=target,
            args=(self._event,),
        )
        self._running_thread.start()

    def stop(self):
        print("Stoping thread")
        self._event.set()

    def join(self):
        self._running_thread.join()

    def get_event(self):
        return self._event
