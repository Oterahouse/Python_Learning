class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsatfe = "unsafe"

    def public_method(self):
        pass

    def _unsafe_method(self):
        pass