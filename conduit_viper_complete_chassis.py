import time
import math
import random

class ViperOcularSystem:
    """Simulates high-speed visual acquisition, dynamic autofocus, and HUD layers."""
    def __init__(self, frame_rate=500):
        self.frame_rate = frame_rate  # Hz
        self.resolution = (1920, 1080)
        self.modes = ["STANDARD", "THERMAL", "NIGHT_VISION"]
        self.current_mode = "STANDARD"

    def capture_frame(self):
        """Generates a synthetic frame object containing environmental visual metadata."""
        detected_objects = ["target_alpha", "pathway_vector_01"] if random.random() > 0.3 else []
        return {
            "timestamp": time.time(),
            "mode": self.current_mode,
            "fps": self.frame_rate,
            "hud_overlay": {
                "velocity_vector": round(random.uniform(0.0, 15.4), 2),
                "distance_to_target": round(random.uniform(1.2, 50.0), 1),
                "render_objects": detected_objects
            }
        }

    def toggle_mode(self, new_mode):
        if new_mode in self.modes:
            self.current_mode = new_mode


class ConduitSpikingNeuralNetwork:
    """Simulates the SNN software layer handling noise-filtering and intent classification."""
    def __init__(self, channels=128):
        self.channels = channels
        self.voltage_threshold = 15.0  # mV threshold to register a spike
        self.synaptic_weights = [random.uniform(0.5, 2.0) for _ in range(channels)]
        self.accumulated_membrane_potential = 0.0

    def fast_fourier_transform_filter(self, raw_signals):
        """Strips out low-frequency autonomic biometrics (heartbeat, respiration noise)."""
        return [0.0 if abs(voltage) < 5.0 else voltage for voltage in raw_signals]

    def evaluate_intent(self, raw_mesh_data):
        """Processes signals through a Leaky Integrate-and-Fire virtual neuron framework."""
        filtered = self.fast_fourier_transform_filter(raw_mesh_data)
        self.accumulated_membrane_potential *= 0.1  # Leaky potential decay
        
        for i in range(self.channels):
            if filtered[i] > 10.0:
                self.accumulated_membrane_potential += filtered[i] * self.synaptic_weights[i]

        if self.accumulated_membrane_potential >= self.voltage_threshold:
            self.accumulated_membrane_potential = 0.0  # Reset
            return True
        return False


class ConduitPharmacokineticPump:
    """Manages internal chemical delivery matrices and monitors neurotransmitter toxicity."""
    def __init__(self):
        self.norepinephrine_level = 0.0
        self.gaba_buffer_level = 100.0
        self.is_overloaded = False

    def inject_dilation_cocktail(self):
        """Injects stimulants to induce tachypsychia, draining the safety GABA buffer."""
        self.norepinephrine_level += 45.5
        self.gaba_buffer_level -= 30.0
        if self.norepinephrine_level > 90.0 or self.gaba_buffer_level < 20.0:
            self.is_overloaded = True

    def flush_stabilizer(self):
        """Floods the network with GABA-A agonists to safely force a neuro-baseline."""
        self.norepinephrine_level = 0.0
        self.gaba_buffer_level = 100.0
        self.is_overloaded = False


class BiomechanicalOutputChassis:
    """Simulates System 3: Optical joint relays, EAP muscle actuators, and bone G-forces."""
    def __init__(self):
        self.muscle_contraction_velocity = 0.0  # meters/sec
        self.skeletal_strain_mpa = 12.0          # Megapascals of force on bone
        self.g_forces_experienced = 1.0          # Earth Gs
        self.chassis_fractured = False

    def convert_optical_packet_to_voltage(self, fiber_optic_signal_active):
        """Simulates solid-state joint relays turning laser pulses into high-voltage bursts."""
        return 400.0 if fiber_optic_signal_active else 0.0  # 400V burst to drive actuators

    def execute_kinetic_movement(self, fiber_optic_signal_active, titanium_reinforced=True):
        """Calculates mechanical strain on the body under hyper-acceleration physics."""
        voltage = self.convert_optical_packet_to_voltage(fiber_optic_signal_active)
        
        if voltage > 0:
            # Carbon-nanotube muscles contract 100x faster than meat
            self.muscle_contraction_velocity = 120.0  # m/s
            self.g_forces_experienced = 16.5          # Catastrophic G-force spike
            self.skeletal_strain_mpa = 145.0          # Heavy physical torque load
            
            # Physics Calculation: Human bone breaks around 120-150 MPa without titanium reinforcement
            structural_limit = 350.0 if titanium_reinforced else 110.0
            if self.skeletal_strain_mpa > structural_limit:
                self.chassis_fractured = True
        else:
            # Return to rest physics
            self.muscle_contraction_velocity = 1.2
            self.g_forces_experienced = 1.0
            self.skeletal_strain_mpa = 12.0


class SystemIntegrator:
    """The central master controller core coordinating all modules simultaneously."""
    def __init__(self, titanium_chassis_installed=True):
        self.viper = ViperOcularSystem()
        self.conduit_snn = ConduitSpikingNeuralNetwork()
        self.pump = ConduitPharmacokineticPump()
        self.chassis = BiomechanicalOutputChassis()
        self.titanium_chassis_installed = titanium_chassis_installed
        self.overclock_active = False

    def generate_live_brainstem_voltages(self, user_is_trying_to_move=False):
        """Generates mock electrical signals from the graphene mesh."""
        signals = []
        for _ in range(self.conduit_snn.channels):
            if user_is_trying_to_move:
                signals.append(random.uniform(12.0, 30.0))  # Clear action potentials
            else:
                signals.append(random.uniform(-3.0, 4.9))   # Chaotic baseline noise
        return signals

    def run_system_tick(self, user_intent_flag=False):
        """Executes one clock cycle of the entire integrated framework."""
        start_time = time.perf_counter()
        
        # 1. Image Capture Step (VIPER)
        visual_frame = self.viper.capture_frame()
        
        # 2. Neural Capture Step (CONDUIT Graphene Matrix)
        raw_brain_data = self.generate_live_brainstem_voltages(user_is_trying_to_move=user_intent_flag)
        
        # 3. Intent Processing Step (SNN Filter & Evaluation)
        intent_verified = self.conduit_snn.evaluate_intent(raw_brain_data)
        
        # 4. Actuation and Pharmacological Step
        execution_status = "IDLE_MONITORING"
        
        if intent_verified and not self.overclock_active:
            self.overclock_active = True
            self.pump.inject_dilation_cocktail()
            execution_status = "OVERCLOCK_CONDUIT_ENGAGED"
        elif self.overclock_active and not user_intent_flag:
            self.overclock_active = False
            self.pump.flush_stabilizer()
            execution_status = "SAFE_COOLDOWN_FLUSH_COMPLETED"
        elif self.overclock_active:
            execution_status = "OVERCLOCK_ACTIVE_PERCEPTION_DILATED"

        # Drive mechanical chassis based on system state
        self.chassis.execute_kinetic_movement(
            fiber_optic_signal_active=self.overclock_active, 
            titanium_reinforced=self.titanium_chassis_installed
        )

        # 5. Safety Diagnostics & Failure Verification
        if self.pump.is_overloaded:
            execution_status = "CRITICAL_ERROR: BRAIN EXCITOTOXICITY NEURAL OVERLOAD"
        if self.chassis.chassis_fractured:
            execution_status = "CRITICAL_FAILURE: STRUCTURAL ENDOSKELETAL SHATTER"

        end_time = time.perf_counter()
        latency_us = (end_time - start_time) * 1_000_000

        # Render complete live system log stream
        print(f"[{execution_status}]")
        print(f" └── Computing Latency : {latency_us:.2f} μs")
        print(f" └── Ocular HUD Vector  : Target Dist {visual_frame['hud_overlay']['distance_to_target']}m")
        print(f" └── Bio-Chemistry     : Norepinephrine {self.pump.norepinephrine_level} units")
        print(f" └── Structural Load   : Strain {self.chassis.skeletal_strain_mpa} MPa | G-Force: {self.chassis.g_forces_experienced}G")
        print("-" * 90)


# --- LIVE SIMULATION EXECUTION BENCHMARK ---
if __name__ == "__main__":
    print("="*90)
    print("RUNNING END-TO-END PROJECT CONDUIT & VIPER INTEGRATED CHASSIS SIMULATION")
    print("="*90)
    
    # Test Scenario A: System running with Titanium Skeleton Installed
    print("\n--- RUNNING SCENARIO A: INTEGRATED REINFORCED CHASSIS ---")
    master_loop = SystemIntegrator(titanium_chassis_installed=True)
    master_loop.run_system_tick(user_intent_flag=False) # Monitor state
    master_loop.run_system_tick(user_intent_flag=True)  # Engagement state
    master_loop.run_system_tick(user_intent_flag=True)  # Sustained state
    master_loop.run_system_tick(user_intent_flag=False) # Cool-down flush
    
    # Test Scenario B: System running WITHOUT Titanium Skeleton (Testing Physics Failure)
    print("\n--- RUNNING SCENARIO B: UNREINFORCED BIOLOGICAL CHASSIS FAILURE ---")
    unreinforced_loop = SystemIntegrator(titanium_chassis_installed=False)
    unreinforced_loop.run_system_tick(user_intent_flag=True) # Immediate acceleration step
