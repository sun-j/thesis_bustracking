class BusKalman:
    def __init__(self, time, pos = 0):
        self.start = time
        self.time_step = 1
        self.iterations = 0

        # Model
        # Estimates
        self.estimate_position = 0.0
        self.estimate_velocity = 0.0

        # Covariance matrix
        self.P_xx = 0.1 # Variance of the position
        self.P_xv = 0.1 # Covariance of position and velocity
        self.P_vv = 0.1 # Variance of the velocity

        # Model parameters
        self.position_process_variance = 0.01
        self.velocity_process_variance = 0.01
        self.R = 30.0 # Measurement noise variance

    def update(self, time, pos):
        # We need to boot strap the estimates for temperature and
        # rate
        if self.iterations == 0: # First measurement
            self.estimate_position = pos       
        elif self.iterations == 1: # Second measurement
            self.estimate_velocity = ( pos - self.estimate_position ) / self.time_step
            self.estimate_position = pos
        else: # Can apply model
            ##################################################################
            # Temporal update (predictive)

            self.time_step = (time - self.start)
            self.estimate_position += self.estimate_velocity * self.time_step

            # Update covariance
            self.P_xx += self.time_step * ( 2.0 * self.P_xv + self.time_step * self.P_vv )
            self.P_xv += self.time_step * self.P_vv
        
            self.P_xx += self.time_step * self.position_process_variance
            self.P_vv += self.time_step * self.velocity_process_variance
        
            ##################################################################       
            # Observational update (reactive)
            vi = 1.0 / ( self.P_xx + self.R )
            kx = self.P_xx * vi
            kv = self.P_xv * vi

            self.estimate_position += (pos - self.estimate_position) * kx
            self.estimate_velocity += (pos - self.estimate_position) * kv

            self.P_xx *= ( 1 - kx )
            self.P_xv *= ( 1 - kx )
            self.P_vv -= kv * self.P_xv

        self.start = time
        self.iterations += 1
        
        print(self.estimate_position)


