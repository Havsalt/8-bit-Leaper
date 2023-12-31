from displaylib import *
from player import Player
from text_collider import TextCollider
from enemy import Enemy

# Made in pyhton using my own ASCII graphics library DisplayLib

CAMERA_FOLLOW_POWER = 0.3


@pull("width", "height")
class Rectangle(TextCollider, Sprite):
    def __init__(self, parent: Node | None = None, x: float = 0, y: float = 0, color=color.WHITE, width: int = 12, height: int = 8) -> None:
        super().__init__(parent, x=x, y=y, color=color)
        self.texture = [
            list("#"*width) for _ in range(height)
        ]


class App(Engine):
    def _on_start(self) -> None:
        self.camera = Camera(mode=Camera.CENTERED | Camera.INCLUDE_SIZE).as_current()
        self.player = Player(x=2, y=-20)
        self.rect1 = Rectangle(width=20, height=3, x=0, y=0, color=color.MEDIUM_VIOLET_RED)
        self.rect2 = Rectangle(width=30, height=3, x=30, y=0, color=color.SALMON)
        self.rect3 = Rectangle(width=30, height=3, x=40, y=-6, color=color.CRIMSON)
        self.rect4 = Rectangle(width=20, height=10, x=-25, y=-10, color=color.SEA_GREEN)
        self.enemy1 = Enemy(x=32, y=-3, color=color.RED)
        self.enemy2 = Enemy(x=46, y=-3, color=color.RED)
        self.enemy3 = Enemy(x=52, y=-9, color=color.RED)
        # self.audio_stream_player = AudioStreamPlayer("./audio/song.wav")
        # self.audio_stream_player.play()
    
    def _update(self, delta: float) -> None:
        target = self.camera.get_global_position().lerp(self.player.get_global_position(), CAMERA_FOLLOW_POWER)
        target.y = self.player.get_global_position().y
        self.camera.set_global_position(target)


def main() -> None:
    app = App(width=64, height=12, tps=18, auto_resize_screen=True)

if __name__ == "__main__":
    main()
