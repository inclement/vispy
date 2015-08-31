'''
Kivy backend for Vispy
'''

from ..base import (BaseApplicationBackend, BaseCanvasBackend,
                    BaseTimerBackend)
from ...util import keys, logger
from ...util.ptime import time
from ... import config

class ApplicationBackend(BaseApplicationBackend):


    def initialise_kivy(self):
        from kivy.core.window import Window
        
    def _vispy_get_backend_name(self):
        return 'kivy'

    def _vispy_process_events(self):
        print('events being processed...')

    def _vispy_run(self):
        print('vispy run!')
        from kivy.clock import Clock
        Clock.schedule_interval(self._vispy_process_events, 0.5)

    def _vispy_reuse(self):
        pass  # Can always pass?

    def _vispy_quit(self):
        pass  # Should quit kivy

    def _vispy_get_native_app(self):
        from kivy.app import App
        return App.get_running_app()

from kivy.uix.widget import Widget
class CanvasBackend(BaseCanvasBackend):

    def __init__(self, *args, **kwargs):
        super(CanvasBackend, self).__init__(*args)
        p = self._process_backend_kwargs(kwargs)

        from kivy.core.window import Window
        # We should set any settings here, but just take what we're
        # given for now

    def _vispy_set_current(self):
        pass  # Kivy has only one window anyway

    def _vispy_swap_buffers(self):
        return  # Kivy will be doing this anyway?
        from kivy.core.window import Window
        Window.flip()

    def _vispy_set_title(self, title):
        pass

    def _vispy_set_size(self, w, h):
        pass

    def _vispy_set_position(self, x, y):
        pass

    def _vispy_set_visible(self, visible):
        pass

    def _vispy_set_fullscreen(self, fullscreen):
        pass

    def _vispy_update(self):
        pass

    def _vispy_close(self):
        pass

    def _vispy_get_size(self):
        return (100, 100)

    def _vispy_get_position(self):
        return (0, 0)

    def _vispy_get_fullscreen(self):
        return False

    def _vispy_get_geometry(self):
        from kivy.core.window import Window
        return 0, 0, Window.size[0], Window.size[1]

class TimerBackend(BaseTimerBackend):

    def __init__(self, vispy_timer):
        BaseTimerBackend.__init__(self, vispy_timer)
        vispy_timer._app._backend._add_timer(self)
        self._vispy_stop()

    def _vispy_start(self, interval):
        self._interval = interval
        self._next_time = time() + self._interval

    def _vispy_stop(self):
        self._next_time = float('inf')

    def _tick(self):
        if time() >= self._next_time:
            self._vispy_timer._timeout()
            self._next_time = time() + self._interval

available = True
testable = False
why_not = '???'

# This isn't all True, but most could be added in principle.
capability = dict(  # things that can be set by the backend
    title=True,
    size=True,
    position=True,
    show=True,
    vsync=True,
    resizable=True,
    decorate=True,
    fullscreen=True,
    context=True,
    multi_window=True,
    scroll=True,
    parent=False,
    always_on_top=False,
)
