# -*- coding: utf-8 -*-
"""Lactate Threshold VO2Max & Aerobic Zone 2 Training Copilot for GenPark Personal Agent."""
import json
import math
from typing import Dict, Any

class LactateThresholdVO2MaxOptimizer:
    """Endurance sports telemetry, VO2Max estimation, and aerobic zone optimizer."""

    @staticmethod
    def estimate_vo2max_and_zones(resting_heart_rate: int, max_heart_rate: int, age_years: int, sex: str, best_5k_time_minutes: float = None) -> Dict[str, Any]:
        """Estimate VO2 Max via Heart Rate Reserve (Uth-Sorensen-Overgaard-Pedersen formula) and compute 5 training zones."""
        # VO2 max = 15.3 * (HR_max / HR_rest)
        vo2_hrr = 15.3 * (float(max_heart_rate) / float(resting_heart_rate))
        
        # Karvonen HR Reserve Zones
        hrr = max_heart_rate - resting_heart_rate
        zones = {
            "Zone_1_Active_Recovery": {"min_hr": int(resting_heart_rate + 0.50 * hrr), "max_hr": int(resting_heart_rate + 0.60 * hrr)},
            "Zone_2_Aerobic_Endurance": {"min_hr": int(resting_heart_rate + 0.60 * hrr), "max_hr": int(resting_heart_rate + 0.70 * hrr)},
            "Zone_3_Tempo_Glycolytic": {"min_hr": int(resting_heart_rate + 0.70 * hrr), "max_hr": int(resting_heart_rate + 0.80 * hrr)},
            "Zone_4_Lactate_Threshold": {"min_hr": int(resting_heart_rate + 0.80 * hrr), "max_hr": int(resting_heart_rate + 0.90 * hrr)},
            "Zone_5_VO2Max_Anaerobic": {"min_hr": int(resting_heart_rate + 0.90 * hrr), "max_hr": max_heart_rate}
        }

        # Aerobic fitness tier
        if sex.lower() == "male":
            tier = "SUPERIOR" if vo2_hrr >= 52 else ("EXCELLENT" if vo2_hrr >= 45 else ("GOOD" if vo2_hrr >= 38 else "FAIR"))
        else:
            tier = "SUPERIOR" if vo2_hrr >= 46 else ("EXCELLENT" if vo2_hrr >= 39 else ("GOOD" if vo2_hrr >= 32 else "FAIR"))

        return {
            "estimated_vo2max_ml_kg_min": round(vo2_hrr, 1),
            "cardiorespiratory_fitness_tier": tier,
            "heart_rate_reserve_bpm": hrr,
            "karvonen_zones_bpm": zones,
            "target_zone2_window": f"{zones['Zone_2_Aerobic_Endurance']['min_hr']} - {zones['Zone_2_Aerobic_Endurance']['max_hr']} bpm",
            "metabolic_benefit": "Zone 2 maximizes fatty acid substrate oxidation while keeping lactate < 2.0 mmol/L."
        }

    @staticmethod
    def generate_zone2_mitochondrial_plan(weekly_available_hours: float, zone2_lower_hr: int, zone2_upper_hr: int, current_vo2max: float = 45.0) -> Dict[str, Any]:
        """Generate polarized 80/20 training plan focusing on mitochondrial capillary density."""
        z2_hours = weekly_available_hours * 0.80
        z5_hours = weekly_available_hours * 0.20
        sessions = max(3, int(weekly_available_hours // 1.2))

        return {
            "training_philosophy": "Polarized 80/20 Aerobic Base Polarization",
            "weekly_zone2_hours": round(z2_hours, 1),
            "weekly_high_intensity_hours": round(z5_hours, 1),
            "recommended_sessions_per_week": sessions,
            "zone2_prescribed_heart_rate": f"{zone2_lower_hr} - {zone2_upper_hr} bpm",
            "session_structure": [
                f"Session 1: {int(z2_hours * 60 / sessions)} mins steady-state Zone 2 (Cycling or Low-incline Treadmill).",
                f"Session 2: {int(z2_hours * 60 / sessions)} mins steady-state Zone 2 with nasal breathing check.",
                "Session 3: 4x4 min Norwegian VO2 Max intervals (Zone 5) with 3-minute active recovery.",
                f"Session 4 (Weekend Long): {int(z2_hours * 60 / sessions * 1.5)} mins progressive fat-adaptation aerobic volume."
            ],
            "biofeedback_guard": "If breathing prevents speaking a full sentence comfortably, decrease pace by 15-20 sec/km."
        }
