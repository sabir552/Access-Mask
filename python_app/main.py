import kivy
kivy.require('2.2.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.properties import StringProperty, ListProperty
from kivy.core.window import Window
import bridge
from accessmask_logic import logic_engine

class AccessMaskRoot(BoxLayout):
    status_text = StringProperty("Initializing...")
    bg_color = ListProperty([0.2, 0.2, 0.2, 1])
    title_text = StringProperty("AccessMask")
    icon_name = StringProperty("shield")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20
        self.mode = "unknown"
        Clock.schedule_once(lambda dt: self.perform_security_check(), 1)

    def perform_security_check(self):
        self.status_text = "Performing security check..."
        print("[MAIN] Triggering face detection")
        detection_result = bridge.call_face_detection()
        self.mode = logic_engine.evaluate_detection(detection_result)
        self.update_ui_for_mode()

    def update_ui_for_mode(self):
        ui_config = logic_engine.get_ui_config(self.mode)
        data = logic_engine.get_data_for_mode(self.mode)
        self.title_text = ui_config["title"]
        self.status_text = ui_config["status"]
        self.bg_color = ui_config["bg_color"]
        self.icon_name = ui_config["icon"]
        while len(self.children) > 3:
            self.remove_widget(self.children[-1])
        self.add_data_section("Notes", data["notes"])
        self.add_data_section("Recent Calls", data["recent_calls"])
        self.add_data_section("Files", data["files"])
        refresh_btn = Button(
            text="Simulate App Resume",
            size_hint=(1, 0.1),
            background_color=(0.3, 0.3, 0.8, 1)
        )
        refresh_btn.bind(on_press=lambda x: self.perform_security_check())
        self.add_widget(refresh_btn)

    def add_data_section(self, title, items):
        self.add_widget(Label(
            text=title,
            size_hint=(1, 0.08),
            bold=True,
            color=(1, 1, 1, 1)
        ))
        for item in items:
            self.add_widget(Label(
                text=f"  • {item}",
                size_hint=(1, 0.06),
                color=(0.9, 0.9, 0.9, 1)
            ))

    def on_bg_color(self, instance, value):
        Window.clearcolor = value

class AccessMaskApp(App):
    def build(self):
        Window.size = (360, 640)
        return AccessMaskRoot()

    def on_resume(self):
        print("[MAIN] App resumed. Triggering security check...")
        Clock.schedule_once(lambda dt: self.root.perform_security_check(), 0.2)
        return True

if __name__ == '__main__':
    AccessMaskApp().run()
