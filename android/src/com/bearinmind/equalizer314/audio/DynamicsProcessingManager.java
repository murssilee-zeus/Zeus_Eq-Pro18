package com.bearinmind.equalizer314.audio;

import android.media.audiofx.DynamicsProcessing;
import android.media.audiofx.DynamicsProcessing.Config;
import android.media.audiofx.DynamicsProcessing.Eq;
import android.media.audiofx.DynamicsProcessing.Limiter;
import android.util.Log;

public class DynamicsProcessingManager {
    private static final String TAG = "ZeusDSP";
    private DynamicsProcessing dp;
    public float limiterThresholdDb = -2.0f;
    public float limiterAttackMs = 1.0f;
    public float limiterReleaseMs = 60.0f;

    public DynamicsProcessingManager() {
        // Inicialización del motor DynamicsProcessing
    }

    public void initSession(int audioSessionId) {
        try {
            Config.Builder builder = new Config.Builder(
                Config.VARIANT_FAVOR_FREQUENCY_RESOLUTION,
                2, // Estéreo
                true, 18, // Eq Post de 18 bandas
                false, 0,
                false, 0,
                true // Limitador activo
            );
            dp = new DynamicsProcessing(0, audioSessionId, builder.build());
            dp.setEnabled(true);
            Log.d(TAG, "DynamicsProcessing iniciado en sesión: " + audioSessionId);
        } catch (Exception e) {
            Log.e(TAG, "Error iniciando DynamicsProcessing", e);
        }
    }

    public void setBandParameters(int bandIndex, float freq, float gain, float q) {
        if (dp != null && dp.getEnabled()) {
            try {
                // Ajuste de banda en tiempo real
                dp.setPostEqBandAllChannelsTo(bandIndex, new DynamicsProcessing.EqBand(true, freq, gain));
            } catch (Exception e) {
                Log.e(TAG, "Error al ajustar banda " + bandIndex, e);
            }
        }
    }

    public void pushLimiterUpdate() {
        if (dp != null && dp.getEnabled()) {
            try {
                Limiter limiter = new Limiter(true, true, 0, limiterAttackMs, limiterReleaseMs, 10.0f, limiterThresholdDb, 0.0f);
                dp.setLimiterAllChannelsTo(limiter);
            } catch (Exception e) {
                Log.e(TAG, "Error actualizando limitador", e);
            }
        }
    }

    public void release() {
        if (dp != null) {
            dp.setEnabled(false);
            dp.release();
            dp = null;
        }
    }
}
