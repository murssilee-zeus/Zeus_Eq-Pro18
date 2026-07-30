import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import platform

# Puente Pyjnius para conectar Python con Java en Android
if platform == 'android':
    from jnius import autoclass
    try:
        # Importamos las clases nativas desde la carpeta de paquetes
        DynamicsProcessingManager = autoclass('com.bearinmind.equalizer314.audio.DynamicsProcessingManager')
        EqService = autoclass('com.bearinmind.equalizer314.audio.EqService')
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
    except Exception as e:
        print(f"Error importando clases Java: {e}")

class ZeusEQEngine:
    def __init__(self):
        self.dsp_manager = None
        if platform == 'android':
            try:
                self.dsp_manager = DynamicsProcessingManager()
                # Inicia sesión global (session_id 0 para master mix)
                self.dsp_manager.initSession(0)
            except Exception as e:
                print(f"No se pudo inicializar DynamicsProcessingManager: {e}")

    def update_band(self, band_index, freq, gain, q=1.414):
        if self.dsp_manager:
            try:
                self.dsp_manager.setBandParameters(int(band_index), float(freq), float(gain), float(q))
            except Exception as e:
                print(f"Error actualizando banda {band_index}: {e}")

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 20

        self.engine = ZeusEQEngine()

        self.add_widget(Label(text="Zeus EQ Pro 18 - Engine Native", font_size=24, size_hint_y=None, height=50))

        # Ejemplo de deslizadores para probar el motor nativo
        self.frequencies = [31, 62, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
        
        for idx, freq in enumerate(self.frequencies):
            row = BoxLayout(orientation='horizontal')
            lbl = Label(text=f"{freq} Hz", size_hint_x=0.3)
            slider = Slider(min=-12, max=12, value=0, size_hint_x=0.7)
            
            # Conectamos cada slider a la función Java
            slider.bind(value=lambda instance, val, b_idx=idx, f=freq: self.on_gain_change(b_idx, f, val))
            
            row.add_widget(lbl)
            row.add_widget(slider)
            self.add_widget(row)

    def on_gain_change(self, band_index, freq, gain_val):
        self.engine.update_band(band_index, freq, gain_val)

class ZeusEqPro18App(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    ZeusEqPro18App().run()
