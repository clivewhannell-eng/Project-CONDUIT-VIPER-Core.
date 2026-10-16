import time

class LeakyIntegrateAndFireNeuron:
    """A mathematically accurate simulation of a single biological spiking neuron."""
    def __init__(self, threshold=15.0, decay_rate=0.8, reset_potential=0.0):
        self.v_threshold = threshold       # Spike threshold (mV)
        self.decay_rate = decay_rate        # Percentage of voltage kept per millisecond (the 'leak')
        self.v_reset = reset_potential      # Baseline reset voltage
        self.v_membrane = 0.0               # Current internal voltage of the neuron

    def process_time_tick(self, input_voltage):
        """Executes one millisecond of time, applying the leak and checking for a spike."""
        # 1. Apply the Leaky Mechanism (voltage decays over time)
        self.v_membrane = self.v_membrane * self.decay_rate
        
        # 2. Integrate Step (add incoming electricity from the graphene sensors)
        self.v_membrane += input_voltage
        
        # 3. Check for Spike Condition
        spike_fired = False
        if self.v_membrane >= self.v_threshold:
            spike_fired = True
            self.v_membrane = self.v_reset  # Instant hyperpolarization / reset
            
        return spike_fired, self.v_membrane


if __name__ == "__main__":
    # Initialize our virtual processing neuron
    neuron = LeakyIntegrateAndFireNeuron(threshold=20.0, decay_rate=0.85)
    
    # Simulate a 20-millisecond window of someone trying to move
    # We will feed a small voltage (5.0 mV) into the neuron every millisecond
    mock_input_stream = [5.0] * 20 
    
    print("=" * 65)
    print(" TIMESTEP | INPUT CURRENT | NEURON VOLTAGE | SNN OUTPUT STATE")
    print("=" * 65)
    
    for ms, input_current in enumerate(mock_input_stream):
        # Run one millisecond of the calculus loop
        spike, current_voltage = neuron.process_time_tick(input_current)
        
        # Determine the visual printout for the spike
        status = "💥 SPIKE FIRED (1)" if spike else "  DORMANT (0)"
        
        print(f"  ms {ms:02d}   |    {input_current:.1f} mV     |    {current_voltage:05.2f} mV   | {status}")
        time.sleep(0.05) # Slight pause to simulate real-time processing ticker
        
    print("=" * 65)
