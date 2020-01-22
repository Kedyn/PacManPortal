class SceneManager:
    # Public:

    @staticmethod
    def get_instance():
        if SceneManager.__instance is None:
            SceneManager()

        return SceneManager.__instance

    def add_scene(self, name, scene):
        if name not in self.__scenes:
            self.__scenes[name] = scene

    def del_scene(self, name):
        if name in self.__scenes:
            self.__scenes.pop(name)

    def set_scene(self, name):
        if name in self.__scenes and self.__scenes[name] is not self.__current_scene:
            if self.__current_scene is None or self.__current_scene.on_exit():
                self.__current_scene = self.__scenes[name]

                self.__current_scene.reset()

    def on_key_down(self, key):
        if self.__current_scene is not None:
            self.__current_scene.on_key_down(key)

    def on_key_up(self, key):
        if self.__current_scene is not None:
            self.__current_scene.on_key_up(key)

    def on_mouse_button_down(self, button, position):
        if self.__current_scene is not None:
            self.__current_scene.on_mouse_button_down(button, position)

    def update(self):
        if self.__current_scene is not None:
            self.__current_scene.update()

    def draw(self):
        if self.__current_scene is not None:
            self.__current_scene.draw()

    # Private:

    __instance = None

    __scenes = None
    __current_scene = None

    def __init__(self):
        if SceneManager.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            SceneManager.__instance = self

            self.__scenes = {}
