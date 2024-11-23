class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __innit__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        if self.get_status() == False:
            self.set_status(True)
        elif self.get_status() == True:
            self.set_status(False)

    def mute(self):
        if self.get_status() == True:
            if self.get_muted() == False:
                self.set_muted(True)
            elif self.get_muted() == True:
                self.set_muted(False)
        else:
            pass

    def channel_up(self):
        if self.get_status() == True:
            if self.get_channel() == self.MAX_CHANNEL:
                self.set_channel(self.MIN_CHANNEL)
            else:
                self.set_channel(self.get_channel() + 1)
        else:
            pass

    def channel_down(self):
        if self.get_status() == True:
            if self.get_channel() == self.MIN_CHANNEL:
                self.set_channel(self.MAX_CHANNEL)
            else:
                self.set_channel(self.get_channel() - 1)
        else:
            pass

    def volume_up(self):
        if self.get_status() == True:
            self.set_muted(False)
            if self.get_volume() == self.MAX_VOLUME:
                pass
            else:
                self.set_volume(self.get_volume() + 1)
        else:
            pass

    def volume_down(self):
        if self.get_status() == True:
            self.set_muted(False)
            if self.get_volume() == self.MIN_VOLUME:
                pass
            else:
                self.set_volume(self.get_volume() - 1)
        else:
            pass


    def get_status(self):
        return self.__status
    def set_status(self, value):
        self.__status = value

    def get_muted(self):
        return self.__muted
    def set_muted(self, value):
        self.__muted = value

    def get_volume(self):
        return self.__volume
    def set_volume(self, value):
        self.__volume = value

    def get_channel(self):
        return self.__channel
    def set_channel(self, value):
        self.__channel = value


    def __str__(self):
        return f'Power = {self.get_status()}, Channel = {self.get_channel()}, Volume = {self.get_volume()}'

