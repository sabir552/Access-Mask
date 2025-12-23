from typing import Dict, Any

RECOGNITION_THRESHOLD = 0.7

class AccessMaskLogic:
    def __init__(self):
        self.real_data_placeholder = {
            "notes": ["Real Note 1: Secure meeting", "Real Note 2: Project Alpha"],
            "recent_calls": ["Mom (Today)", "Doctor (Yesterday)"],
            "files": ["personal_budget.xlsx", "passport_scan.pdf"]
        }
        self.decoy_data = {
            "notes": ["Grocery List: Milk", "Reminder: Dentist"],
            "recent_calls": ["Telemarketer", "Unknown"],
            "files": ["shopping_list.txt", "cat_videos.zip"]
        }

    def evaluate_detection(self, detection_result: Dict[str, Any]) -> str:
        matched = detection_result.get("matched", False)
        score = detection_result.get("score", 0.0)
        is_owner = matched and (score >= RECOGNITION_THRESHOLD)
        return "real" if is_owner else "decoy"

    def get_data_for_mode(self, mode: str) -> Dict[str, Any]:
        return self.real_data_placeholder if mode == "real" else self.decoy_data

    def get_ui_config(self, mode: str) -> Dict[str, Any]:
        if mode == "real":
            return {
                "bg_color": (0.1, 0.5, 0.2, 1),
                "title": "AccessMask - REAL MODE",
                "status": "Authenticated Owner",
                "icon": "shield-check"
            }
        else:
            return {
                "bg_color": (0.7, 0.1, 0.1, 1),
                "title": "AccessMask",
                "status": "Standard Mode",
                "icon": "shield"
            }

logic_engine = AccessMaskLogic()
