import os
import sys
import importlib

from happyMirror.widget import Widget


class WidgetsLoader:
    def __init__(self):
        self.__loaded_widgets = []

    def load(self, enabled_widgets=None) -> list[Widget]:
        loaded_widgets = []

        if enabled_widgets is None:
            enabled_widgets = []

        for root, dirs, files in self.__walk_level(os.curdir + '/widgets'):
            for dir_name in dirs:
                single_widget = self.__load_single_widget(dir_name, enabled_widgets, root)
                loaded_widgets.append(single_widget)


        self.__loaded_widgets = self.__sanitize(loaded_widgets)
        return self.__loaded_widgets

    def __sanitize(self, loaded_widgets) -> list:
        return list(filter(lambda w: w is not None, loaded_widgets))

    def __load_single_widget(self, dir_name, enabled_widgets, root) -> Widget:
        if dir_name in enabled_widgets:
            try:
                sys.path.append(f"{root}/{dir_name}")
                print(f"Importing widget '{dir_name}'")
                widget_renderer = importlib.import_module(dir_name)
                print(f"Widget '{dir_name}' loaded")

                return Widget(module=widget_renderer, instance=widget_renderer.Renderer())
            except ModuleNotFoundError:
                print("Module not found")
            except AttributeError:
                print("The module does not have the specified class or function.")
            except Exception as e:
                print(f"An error occurred while loading widget '{dir_name}': {e}")


    def __walk_level(self, some_dir, level=1):
        some_dir = some_dir.rstrip(os.path.sep)
        assert os.path.isdir(some_dir)
        num_sep = some_dir.count(os.path.sep)
        for root, dirs, files in os.walk(some_dir):
            yield root, dirs, files
            num_sep_this = root.count(os.path.sep)
            if num_sep + level <= num_sep_this:
                del dirs[:]

