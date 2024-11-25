class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        """
        Initializes new Television objects.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self):
        """
        Toggles Power on the given TV Object.\n
        True = On\n
        False = Off
        """
        if self.get_status() == False:
            self.set_status(True)
        elif self.get_status() == True:
            self.set_status(False)

    def mute(self):
        """
        Toggles Mute on the given TV Object.\n
        True = Mute on\n
        False = Mute off
        """
        if self.get_status() == True:
            if self.get_muted() == False:
                self.set_muted(True)
            elif self.get_muted() == True:
                self.set_muted(False)
        else:
            pass

    def channel_up(self):
        """
        If given TV Object is Off: passes.\n
        If given TV Object is On: Increases the given TV Object's Channel by 1.\n
        If currently on max channel loops to the min channel.
        """
        if self.get_status() == True:
            if self.get_channel() == self.MAX_CHANNEL:
                self.set_channel(self.MIN_CHANNEL)
            else:
                self.set_channel(self.get_channel() + 1)
        else:
            pass

    def channel_down(self):
        """
        If given TV Object is OFF: passes.\n
        If given TV Object is ON: Decreases the given TV Object's Channel by 1.\n
        If currently on MIN channel loops to the MAX channel.
        """
        if self.get_status() == True:
            if self.get_channel() == self.MIN_CHANNEL:
                self.set_channel(self.MAX_CHANNEL)
            else:
                self.set_channel(self.get_channel() - 1)
        else:
            pass

    def volume_up(self):
        """
        If given TV Object is OFF: passes.\n
        If given TV Object is ON: Increases the given TV Object's Volume by 1.\n
        If currently on MAX volume: passes.
        """
        if self.get_status() == True:
            self.set_muted(False)
            if self.get_volume() == self.MAX_VOLUME:
                pass
            else:
                self.set_volume(self.get_volume() + 1)
        else:
            pass

    def volume_down(self):
        """
        If given TV Object is OFF: passes.\n
        If given TV Object is ON: Decreases the given TV Object's Volume by 1.\n
        If currently on MIN volume: passes.
        """
        if self.get_status() == True:
            self.set_muted(False)
            if self.get_volume() == self.MIN_VOLUME:
                pass
            else:
                self.set_volume(self.get_volume() - 1)
        else:
            pass


    def get_status(self):
        """
        Retrieves the value of the private variable: __status
        :return: if TV is ON or OFF (ON = True | OFF = False)
        """
        return self.__status
    def set_status(self, value):
        """
        Sets the value of __status to the given value.
        :param value: value to set __status to. (Must be True or False.)
        """
        self.__status = value

    def get_muted(self):
        """
        Retrieves the value of the private variable: __muted
        :return: if TV is muted or not
        """
        return self.__muted
    def set_muted(self, value):
        """
        Sets the value of __muted to the given value.
        :param value: value to set __muted to.
        """
        self.__muted = value

    def get_volume(self):
        """
        If given TV Object is NOT Muted:
            Returns the value of the private variable: __volume
        If given TV Object IS Muted:
            Returns the value: 0
        :return: current volume
        """
        if self.get_muted() == True:
            return 0
        else:
            return self.__volume
    def set_volume(self, value):
        """
        Sets the value of __volume to the given value.
        :param value: value to set __volume to.
        """
        self.__volume = value

    def get_channel(self):
        """
        Returns the value of __channel.
        :return: current channel
        """
        return self.__channel
    def set_channel(self, value):
        """
        Sets the value of __channel to the given value.
        :param value: value to set __channel to.
        """
        self.__channel = value


    def __str__(self):
        """
        Prints a string giving the status of given TV's attributes.
        :return: a string stating TV Object's Power, Channel, and Volume values
        """
        return f'Power = {self.get_status()}, Channel = {self.get_channel()}, Volume = {self.get_volume()}'

