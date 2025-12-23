import json
import os
from typing import Dict, Any

IS_ANDROID = os.getenv("ANDROID_ARGUMENT") is not None or os.getenv("P4A_BOOTSTRAP") is not None

if IS_ANDROID:
    try:
        from jnius import autoclass, cast
        FaceModule = autoclass("org.accessmask.native.FaceModule")
        Context = autoclass("android.content.Context")
        PythonActivity = autoclass("org.kivy.android.PythonActivity")
        _face_module_instance = None

        def get_face_module():
            global _face_module_instance
            if _face_module_instance is None:
                context = cast(Context, PythonActivity.mActivity.getApplicationContext())
                _face_module_instance = FaceModule(context)
            return _face_module_instance

        def call_face_detection() -> Dict[str, Any]:
            try:
                instance = get_face_module()
                json_str = instance.captureAndDetect()
                result = json.loads(json_str)
                return result
            except Exception as e:
                return {"matched": False, "score": 0.0, "message": f"Bridge error: {e}"}
    except Exception as e:
        IS_ANDROID = False

if not IS_ANDROID:
    def call_face_detection() -> Dict[str, Any]:
        import random
        is_owner = random.choice([True, False])
        confidence = 0.9 if is_owner else 0.3
        return {
            "matched": is_owner,
            "score": confidence,
            "message": "Fallback simulation mode"
              }
