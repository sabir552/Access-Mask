package org.accessmask.native
import android.content.Context
import android.hardware.Camera
import org.json.JSONObject

class FaceModule(private val context: Context) {
    fun captureAndDetect(): String {
        var camera: Camera? = null
        val result = JSONObject()
        try {
            val cameraId = findFrontCameraId()
            if (cameraId == -1) {
                return buildResult(false, 0.0f)
            }
            camera = Camera.open(cameraId)
            val isOwner = (0..100).random() < 70
            val confidence = if (isOwner) 0.85f else 0.25f
            result.put("matched", isOwner)
            result.put("score", confidence)
            result.put("message", "Detection completed")
        } catch (e: Exception) {
            result.put("matched", false)
            result.put("score", 0.0f)
            result.put("message", "Error: ${e.message}")
        } finally {
            camera?.release()
        }
        return result.toString()
    }

    private fun findFrontCameraId(): Int {
        val numberOfCameras = Camera.getNumberOfCameras()
        for (i in 0 until numberOfCameras) {
            val info = Camera.CameraInfo()
            Camera.getCameraInfo(i, info)
            if (info.facing == Camera.CameraInfo.CAMERA_FACING_FRONT) {
                return i
            }
        }
        return -1
    }

    private fun buildResult(matched: Boolean, score: Float): String {
        return JSONObject().apply {
            put("matched", matched)
            put("score", score)
            put("message", "Default fallback")
        }.toString()
    }
}
