package com.bearinmind.equalizer314.audio;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.util.Log;

public class EqService extends Service {
    private static final String TAG = "EqService";
    private DynamicsProcessingManager dspManager;

    @Override
    public void onCreate() {
        super.onCreate();
        dspManager = new DynamicsProcessingManager();
        Log.d(TAG, "Servicio de Ecualización iniciado en segundo plano");
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        if (intent != null && intent.hasExtra("audio_session_id")) {
            int sessionId = intent.getIntExtra("audio_session_id", 0);
            if (sessionId != 0) {
                dspManager.initSession(sessionId);
            }
        }
        return START_STICKY;
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public void onDestroy() {
        if (dspManager != null) {
            dspManager.release();
        }
        super.onDestroy();
    }
}
