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
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.status = False

    def mute(self):
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            elif self.__muted == True:
                self.__muted = False
        else:
            pass

    def channel_up(self):
        if self.__status == True:
            if self.__channel == self.MAX_CHANNEL:
                self._channel = self.MIN_CHANNEL
            else:
                self.__channel += 1
        else:
            pass

    def channel_down(self):
        if self.__status == True:
            if self.__channel == self.MIN_CHANNEL:
                self._channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1
        else:
            pass

    def volume_up(self):
        if self.__status == True:
            self.__muted = False
            if self.__volume == self.MAX_VOLUME:
                pass
            else:
                self.__volume += 1
        else:
            pass

    def volume_down(self):
        if self.__status == True:
            self.__muted = False
            if self.__volume == self.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1
        else:
            pass
        
    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
    
my_tv = Televison