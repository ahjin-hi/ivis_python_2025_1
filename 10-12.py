class TV:
    MIN_VOLUME = 0
    MAX_VOLUME = 100
    MIN_CHANNEL = 0
    MAX_CHANNEL = 200

    def __init__(self):
        self._volume = 5
        self._channel = 0
        self._is_on = False

    def __str__(self):
        status = "TV가 켜짐 상태입니다." if self._is_on else "TV가 꺼짐 상태입니다."
        return f"{status}\n볼륨 = {self._volume}, 채널 = {self._channel}"

    def toggle_power(self):
        self._is_on = not self._is_on

    def set_channel(self, c):
        if self.MIN_CHANNEL <= c <= self.MAX_CHANNEL:
            self._channel = c

        else :
          print("채널 오류")

    def get_channel(self):
        return self._channel

    def set_volume(self, v):
        if self.MIN_VOLUME <= v <= self.MAX_VOLUME:
            self._volume = v
        else :
          print("볼륨 오류")

    def get_volume(self):
        return self._volume

    def volume_up(self):
        if self._volume < self.MAX_VOLUME:
            self._volume += 1
        else :
            self._volume = self.MAX_VOLUME

    def volume_down(self):
        if self._volume > self.MIN_VOLUME:
            self._volume -= 1

        else :
            self._volume = self.MIN_VOLUME

    def channel_up(self):
        if self._channel < self.MAX_CHANNEL:
            self._channel += 1
        else :
            self._channel = self.MAX_CHANNEL

    def channel_down(self):
        if self._channel > self.MIN_CHANNEL:
            self._channel -= 1
        else :
            self._channel = self.MIN_CHANNEL



my_tv = TV()
print(my_tv)             
my_tv.toggle_power()
my_tv.set_channel(45)
print(my_tv)
my_tv.volume_up()
my_tv.channel_up()
print(my_tv)    
