"""
Computational Physiology & Telemetry Integration Engine
=======================================================
Core mathematical engine implementing non-linear, cubic polynomial progression 
algorithms to model multi-system physiological strain, microvascular rheology, 
and autonomic workloads based on the continuous restriction curve.

Includes a fast-converging Newton-Raphson iterative solver for real-time 
embedded diagnostic systems and microcontrollers.
"""

import math
from typing import Dict, Any, Union

class ComputationalPhysiologyEngine:
    def __init__(self, scaling_multiplier: float = 1.25, base_baseline: float = 1405.0):
        """
        Initializes the telemetry simulation engine.
        
        :param scaling_multiplier: Regional or biometric scaling constant (Omega/Lambda).
        :param base_baseline: Nominal physiological baseline value when D = 0.
        """
        self.omega = scaling_multiplier
        self.base_constant = base_baseline

    def calculate_forward_workload(self, D: float) -> float:
        """
        The Core Continuous Equation. 
        Calculates the Systemic Overload/Workload (P) given a Restriction/Adaptation Index (D).
        
        Formula: f(D) = 1/12 * D^3 + 1013/120 * D^2 + 14027/50 * D + 1405
        """
        if not (0 <= D <= 100):
            raise ValueError("Index D must be bounded between 0 and 100 inclusive.")
            
        f_D = (1.0 / 12.0) * (D ** 3) + (1013.0 / 120.0) * (D ** 2) + (14027.0 / 50.0) * D + self.base_constant
        return f_D

    def calculate_derivative(self, D: float) -> float:
        """
        Calculates the first derivative f'(D) representing the instantaneous velocity 
        of physiological decline or marginal cost acceleration.
        
        Formula: f'(D) = 1/4 * D^2 + 1013/60 * D + 14027/50
        """
        return 0.25 * (D ** 2) + (1013.0 / 60.0) * D + (14027.0 / 50.0)

    def solve_for_restriction_index(self, P_target: float, tolerance: float = 1e-5, max_iterations: int = 100) -> float:
        """
        Newton-Raphson Iterative Root-Finding Loop.
        Decodes measured sensor telemetry (P) backwards to isolate the internal 
        physiological degradation state (D) with quadratic convergence.
        """
        # Seed Value Selection (D_0) via a linear baseline approximation
        D_n = (P_target - self.base_constant) / (14027.0 / 50.0)
        D_n = max(1.0, min(99.0, D_n)) # Safely clamp initial seed within boundaries

        for _ in range(max_iterations):
            # Evaluate objective function F(D_n) = f(D_n) - P_target
            F_D = self.calculate_forward_workload(D_n) - P_target
            
            # Evaluate derivative F'(D_n) = f'(D_n)
            F_prime_D = self.calculate_derivative(D_n)
            
            if F_prime_D == 0:
                break
                
            # Perform Newton-Raphson update step: D_{n+1} = D_n - F(D_n)/F'(D_n)
            D_next = D_n - (F_D / F_prime_D)
            D_next = max(1.0, min(100.0, D_next)) # Enforce bounding conditions
            
            # Check tolerance threshold for convergence
            if abs(D_next - D_n) < tolerance:
                return round(D_next, 4)
                
            D_n = D_next
            
        return round(D_n, 4)

    def profile_patient_system(self, system_type: str, measured_value: float) -> Dict[str, Any]:
        """
        Maps telemetry metrics across the multi-system clinical modules.
        
        :param system_type: One of 'hemodynamics', 'orthopedics', 'pulmonary', 'autonomic', 'trauma'
        :param measured_value: The target output value (P) recorded by biometric sensors.
        """
        D_resolved = self.solve_for_restriction_index(measured_value)
        
        # Determine clinical risk tier stratification
        if D_resolved <= 15:
            tier = "Tier I: Controlled / Nominal Baseline"
        elif D_resolved <= 35:
            tier = "Tier II: Mild / Compensated Adaptation"
        elif D_resolved <= 55:
            tier = "Tier III: Moderate / Progressive Decompensation"
        elif D_resolved <= 75:
            tier = "Tier IV: Severe / High-Risk Hyperviscosity"
        else:
            tier = "Tier V: Critical / Irreversible Structural Collapse"
            
        return {
            "System Context": system_type.upper(),
            "Resolved Index (D)": D_resolved,
            "Risk Stratification": tier,
            "Target Output (P)": measured_value,
            "Marginal Velocity": round(self.calculate_derivative(D_resolved), 4)
        }

# --- Module Demonstration & Verification Validation Tests ---
if __name__ == "__main__":
    engine = ComputationalPhysiologyEngine()
    
    print("================================================================")
    print("RUNNING COMPUTATIONAL PHYSIOLOGY SIMULATION VERIFICATION TESTS")
    print("================================================================\n")
    
    # Test 1: Verify Forward Workload Calculations across Key Milestone Tiers
    milestones = [1.0, 20.0, 40.0, 60.0, 100.0]
    for m in milestones:
        p_val = engine.calculate_forward_workload(m)
        print(f"Forward Checkpoint -> Index D: {m:<5} | Resulting Calculated Output P: {round(p_val, 2)}")
        
    print("\n----------------------------------------------------------------")
    print("VERIFYING INVERSE RECOVERY RESOLUTION (NEWTON-RAPHSON LOOPS)")
    print("----------------------------------------------------------------")
    
    # Test 2: Invert a measured signal to isolate the patient's biological state
    sample_telemetry_signals = [5406.0, 22257.0, 57445.0, 200000.0]
    for signal in sample_telemetry_signals:
        resolved_profile = engine.profile_patient_system(system_type="hemodynamics", measured_value=signal)
        print(f"\nSensor Output Readout (P): {signal}")
        print(f"  -> Decoded Biological State (D): {resolved_profile['Resolved Index (D)']}")
        print(f"  -> Assigned Clinical Safety Tier: {resolved_profile['Risk Stratification']}")
        print(f"  -> Instantaneous Local Friction Drift (f'(D)): {resolved_profile['Marginal Velocity']}")
