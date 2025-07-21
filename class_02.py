class Animal:
    def __init__(self, name):
        self.name = name

    def sing(self):
        print(f"{self.name}, 很愛唱歌")


bird = Animal("鴿子")
print(bird.name)
bird.sing()


# def __init__(self):
#     pass  # 預設的建構式，什麼都不做
