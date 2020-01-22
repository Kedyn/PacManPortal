from framework.AssetsManager import AssetsManager


def load_characters():
    assets_manager = AssetsManager.get_instance()

    # Ghosts
    assets_manager.add_asset("image", "blinky_normal", "assets/blinky_normal.png")
    assets_manager.add_asset("image", "blinky_step", "assets/blinky_step.png")
    assets_manager.add_asset("image", "pinky_normal", "assets/pinky_normal.png")
    assets_manager.add_asset("image", "pinky_step", "assets/pinky_step.png")
    assets_manager.add_asset("image", "inky_normal", "assets/inky_normal.png")
    assets_manager.add_asset("image", "inky_step", "assets/inky_step.png")
    assets_manager.add_asset("image", "clyde_normal", "assets/clyde_normal.png")
    assets_manager.add_asset("image", "clyde_step", "assets/clyde_step.png")

    assets_manager.add_asset("image", "blue_normal", "assets/blue_normal.png")
    assets_manager.add_asset("image", "blue_step", "assets/blue_step.png")

    assets_manager.add_asset("image", "white_normal", "assets/white_normal.png")
    assets_manager.add_asset("image", "white_step", "assets/white_step.png")

    assets_manager.add_asset("image", "left_eyes", "assets/left_eyes.png")
    assets_manager.add_asset("image", "up_eyes", "assets/up_eyes.png")
    assets_manager.add_asset("image", "right_eyes", "assets/right_eyes.png")
    assets_manager.add_asset("image", "down_eyes", "assets/down_eyes.png")
    assets_manager.add_asset("image", "front_eyes", "assets/front_eyes.png")

    # Pacman
    assets_manager.add_asset("image", "pacman_opened", "assets/pacman_opened.png")
    assets_manager.add_asset("image", "pacman_closed", "assets/pacman_closed.png")
