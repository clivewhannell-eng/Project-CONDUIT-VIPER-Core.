import time
import math
import random

class ViperOcularSystem:
    def __init__(self, frame_rate=500):
        self.frame_rate = frame_rate  
        self.current_mode = "STANDARD"

    def capture_frame(self):
        return {
            "timestamp": time.time(),
            "mode": self.current_mode,
            "hud_overlay": {
                "velocity_vector": round(random.uniform(0.0, 15.4), 2),
                "distance_to_target": round(random.uniform(1.2, 50.0), 1)
            }
        }


class LeakyIntegrateAndFireNeuron:
    def __init__(self, threshold=15.0, decay_rate=0.85):
        self.v_threshold = threshold       
        self.decay_rate = decay_rate        
        self.v_membrane = 0.0               

    def evaluate_tick(self, input_voltage):
        self.v_membrane *= self.decay_rate  
        self.v_membrane += input_voltage     
        
        if self.v_membrane >= self.v_threshold:
            self.v_membrane = 0.0  
            return True            
        return False


class RealDataIngestionEngine:
    def __init__(self, channel_count=128):
        self.channel_count = channel_count
        
    def read_human_dataset_row(self, line_index, intentional_movement=False):
        structured_row = []
        for channel in range(self.channel_count):
            if intentional_movement:
                simulated_human_spike = math.sin(line_index * 0.5) * random.uniform(15.0, 45.0)
            else:
                simulated_human_spike = math.sin(line_index * 0.1) * random.uniform(-4.0, 6.0)
            structured_row.append(simulated_human_spike)
        return structured_row


class BiomechanicalThermodynamicChassis:
    """Models System 3 mechanics with active Subdermal Heat-Pipe Mesh Cooling loops."""
    def __init__(self):
        self.core_temperature_celsius = 37.0       
        self.skeletal_strain_mpa = 12.0
        self.chassis_fractured = False
        self.thermal_shutdown_tripped = False
        
        # New Cooling Subsystem Metircs
        self.subdermal_cooling_pump_active = False
        self.cooling_loop_efficiency_rating = 0.0   # Current active heat extraction rate

    def execute_physics_tick(self, system_is_overclocked, titanium_reinforced=True, cooling_system_installed=True):
        """Calculates kinetic strain and thermodynamic balance under active dissipation loops."""
        heat_generation_coefficient = 4.2  # °C generated per tick under load
        biological_base_cooling = 0.5      # Normal homeostatic sweating/blood flow cooling
        subdermal_active_cooling = 3.6     # Active graphene heat-pipe loop dissipation capacity

        if system_is_overclocked:
            self.skeletal_strain_mpa = 145.0
            
            # Base generation from muscle friction
            self.core_temperature_celsius += heat_generation_coefficient
            
            # Activate Subdermal Cooling loops dynamically if hardware is present
            if cooling_system_installed:
                self.subdermal_cooling_pump_active = True
                self.cooling_loop_efficiency_rating = subdermal_active_cooling
                self.core_temperature_celsius -= subdermal_active_cooling
            else:
                self.subdermal_cooling_pump_active = False
                self.cooling_loop_efficiency_rating = 0.0
                
            self.core_temperature_celsius -= biological_base_cooling

            # Structural skeleton check
            structural_limit = 350.0 if titanium_reinforced else 110.0
            if self.skeletal_strain_mpa > structural_limit:
                self.chassis_fractured = True
        else:
            self.skeletal_strain_mpa = 12.0
            self.subdermal_cooling_pump_active = False
            self.cooling_loop_efficiency_rating = 0.0
            
            # Cool back down to standard resting baseline
            if self.core_temperature_celsius > 37.0:
                self.core_temperature_celsius -= 1.0  # Safe recovery drop
                if self.core_temperature_celsius < 37.0:
                    self.core_temperature_celsius = 37.0

        # Verify critical biological limit threshold (42°C causes severe damage/lethality)
        if self.core_temperature_celsius >= 42.0:
            self.thermal_shutdown_tripped = True


class MasterSystemIntegrator:
    def __init__(self, titanium_installed=True, cooling_installed=True):
        self.viper = ViperOcularSystem()
        self.dataset_engine = RealDataIngestionEngine()
        self.processing_neuron = LeakyIntegrateAndFireNeuron()
        self.chassis = BiomechanicalThermodynamicChassis()
        self.titanium_installed = titanium_installed
        self.cooling_installed = cooling_installed
        self.system_state = "MONITORING_BASELINE"
        self.clock_tick = 0

    def process_cycle(self, user_is_moving_in_dataset=False):
        start_time = time.perf_counter()
        self.clock_tick += 1

        viper_frame = self.viper.capture_frame()
        live_human_voltages = self.dataset_engine.read_human_dataset_row(self.clock_tick, user_is_moving_in_dataset)
        mean_voltage_input = sum(live_human_voltages) / len(live_human_voltages)
        overclock_signal_triggered = self.processing_neuron.evaluate_tick(mean_voltage_input)

        if overclock_signal_triggered:
            self.system_state = "PROJECT_CONDUIT_ENGAGED_OVERCLOCK"
        elif not user_is_moving_in_dataset and self.system_state == "PROJECT_CONDUIT_ENGAGED_OVERCLOCK":
            self.system_state = "SAFE_COOLDOWN_FLUSH"
        elif self.system_state == "SAFE_COOLDOWN_FLUSH":
            self.system_state = "MONITORING_BASELINE"

        active_overclock_flag = (self.system_state == "PROJECT_CONDUIT_ENGAGED_OVERCLOCK")
        
        # Execute tick with active cooling switch
        self.chassis.execute_physics_tick(
            system_is_overclocked=active_overclock_flag, 
            titanium_reinforced=self.titanium_installed,
            cooling_system_installed=self.cooling_installed
        )

        if self.chassis.thermal_shutdown_tripped:
            self.system_state = "CRITICAL_HALT: THERMAL CELLULAR BIOLOGICAL BURNS (OVERHEATING)"
        if self.chassis.chassis_fractured:
            self.system_state = "CRITICAL_HALT: MUSCULOSKELETAL SHATTER"

        end_time = time.perf_counter()
        latency_us = (end_time - start_time) * 1_000_000

        cooling_status = f"ACTIVE ({self.chassis.cooling_loop_efficiency_rating}°C/t Extraction)" if self.chassis.subdermal_cooling_pump_active else "DORMANT"

        print(f"[{self.system_state}]")
        print(f" ├── Computing Latency   : {latency_us:.2f} μs")
        print(f" ├── Subdermal Coolers   : Loop Status: {cooling_status}")
        print(f" └── Thermodynamic Core  : Core Temp: {self.chassis.core_temperature_celsius:.1f}°C | Load: {self.chassis.skeletal_strain_mpa} MPa")
        print("." * 95)


if __name__ == "__main__":
    print("="*95)
    print("INITIALIZING PROJECT CONDUIT / VIPER CORE COMPUTER LOOPS v2.5 [THERMAL MATRIX REWRITE]...")
    print("="*95)
    
    # Run simulation with the cooling loops installed to witness stabilization
    print("\n--- TEST RUN A: SYSTEM ENGAGED WITH ACTIVE SUBDERMAL HEAT-PIPE SYSTEMS ---")
    engine = MasterSystemIntegrator(titanium_installed=True, cooling_installed=True)
    engine.process_cycle(user_is_moving_in_dataset=True)
    engine.process_cycle(user_is_moving_in_dataset=True)
    engine.process_cycle(user_is_moving_in_dataset=True) # Observe how the temperature balances smoothly now!
    engine.process_cycle(user_is_moving_in_dataset=False)
    
    # Run simulation WITHOUT cooling loops to verify physics failure threshold protection
    print("\n--- TEST RUN B: SYSTEM ENGAGED WITHOUT ACTIVE SUBDERMAL HARDWARE ---")
    uncooled_engine = MasterSystemIntegrator(titanium_installed=True, cooling_installed=False)
    uncooled_engine.process_cycle(uncooled_engine.clock_tick) # Setup
    uncooled_engine.process_cycle(user_is_moving_in_dataset=True)
    uncooled_engine.process_cycle(user_is_moving_in_dataset=True) # Fails due to unmitigated internal friction burns

    print("="*95)
