import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.lang import Builder
from kivy.utils import platform

# Integración con el motor nativo Java/Kotlin vía Pyjnius en Android
if platform == 'android':
    from jnius import autoclass
    try:
        DynamicsProcessingManager = autoclass('com.bearinmind.equalizer314.audio.DynamicsProcessingManager')
        ParametricEqualizer = autoclass('com.bearinmind.equalizer314.dsp.ParametricEqualizer')
    except Exception as e:
        print(f"Error cargando clases nativas: {e}")
        DynamicsProcessingManager = None
        ParametricEqualizer = None
else:
    DynamicsProcessingManager = None
    ParametricEqualizer = None

class TextInputPopup(ModalView):
    pass

class ZeusStudioAppUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.active_filter_type = "PEAK"
        self.dp_engine = DynamicsProcessingManager() if DynamicsProcessingManager else None

    def set_filter_type(self, filter_type):
        self.active_filter_type = filter_type
        self.on_param_change()

    def on_param_change(self):
        freq = self.ids.freq_slider.value
        q = self.ids.q_slider.value
        gain = self.ids.gain_slider.value
        pass

    def on_limiter_change(self):
        if self.dp_engine:
            try:
                self.dp_engine.limiterThresholdDb = float(self.ids.lim_thresh.value)
                self.dp_engine.limiterAttackMs = float(self.ids.lim_attack.value)
                self.dp_engine.limiterReleaseMs = float(self.ids.lim_release.value)
                self.dp_engine.pushLimiterUpdate()
            except Exception as e:
                print(f"Error actualizando limitador: {e}")

    def reset_crossovers(self):
        self.ids.xover_1.text = "120 Hz"
        self.ids.xover_2.text = "1000 Hz"
        self.ids.xover_3.text = "4000 Hz"

class ZeusStudioApp(App):
    def build(self):
        Builder.load_file('zeus_studio.kv')
        self.ui = ZeusStudioAppUI()
        self.target_widget = None
        return self.ui

    def open_manual_input(self, title, target_widget):
        self.target_widget = target_widget
        self.popup = TextInputPopup()
        self.popup.title_text = f"Ajustar {title}:"
        
        if hasattr(target_widget, 'value'):
            self.popup.ids.popup_input.text = str(round(target_widget.value, 2))
        elif hasattr(target_widget, 'text'):
            val = target_widget.text.replace(' Hz', '').replace(' dB', '').replace(' ms', '')
            self.popup.ids.popup_input.text = val
            
        self.popup.open()

    def apply_manual_value(self):
        if not hasattr(self, 'popup') or not self.popup.ids.popup_input.text.strip():
            return
        
        raw_text = self.popup.ids.popup_input.text.strip()
        try:
            val = float(raw_text)
            if hasattr(self.target_widget, 'value'):
                val = max(self.target_widget.min, min(self.target_widget.max, val))
                self.target_widget.value = val
            elif hasattr(self.target_widget, 'text'):
                if 'Hz' in self.target_widget.text or 'xover' in str(getattr(self.target_widget, 'id', '')):
                    self.target_widget.text = f"{int(val)} Hz"
                elif 'dB' in self.target_widget.text:
                    self.target_widget.text = f"{val:.1f} dB"
                else:
                    self.target_widget.text = str(val)
        except ValueError:
            pass

if __name__ == '__main__':
    ZeusStudioApp().run()
