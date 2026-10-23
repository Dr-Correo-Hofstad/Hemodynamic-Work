import pytest
from hemo_models import ComputationalPhysiologyEngine

@pytest.fixture
def engine():
    """Initializes a fresh instances of the engine for isolated test states."""
    return ComputationalPhysiologyEngine()

def test_baseline_forward_calculation(engine):
    """Verifies that the continuous equation resolves boundaries properly."""
    # D = 0 should return the exact base baseline constant
    assert engine.calculate_forward_workload(0.0) == 1405.0

def test_forward_milestones(engine):
    """Validates forward calculation accuracy against documented clinical tiers."""
    # Verify Tier II (D=20) matches documented forward limits
    p_20 = engine.calculate_forward_workload(20.0)
    assert abs(p_20 - 11043.33) < 1.0
    
    # Verify Tier III (D=40) matches documented forward limits
    p_40 = engine.calculate_forward_workload(40.0)
    assert abs(p_40 - 31390.0) < 1.0

def test_index_out_of_bounds(engine):
    """Ensures that values outside the physiological boundary (0-100) trigger errors."""
    with pytest.raises(ValueError):
        engine.calculate_forward_workload(-1.0)
    with pytest.raises(ValueError):
        engine.calculate_forward_workload(101.0)

def test_inverse_solver_convergence(engine):
    """Tests the Newton-Raphson engine's capability to invert measured parameters precisely."""
    # Target standard forward calculation outputs
    test_signals = [5406.0, 22257.0, 57445.0, 200000.0]
    
    for signal in test_signals:
        # Solve backward for D
        resolved_d = engine.solve_for_restriction_index(signal)
        # Re-evaluate forward to test absolute numerical loop integrity
        recalculated_p = engine.calculate_forward_workload(resolved_d)
        
        # Verify delta falls within strict clinical tolerances
        assert abs(recalculated_p - signal) < 50.0

def test_patient_profiling_output(engine):
    """Validates structural dictionary outputs for EMR/EHR system telemetry piping."""
    profile = engine.profile_patient_system("trauma", 57445.0)
    
    assert profile["System Context"] == "TRAUMA"
    assert "Resolved Index (D)" in profile
    assert "Risk Stratification" in profile
    assert isinstance(profile["Marginal Velocity"], float)
