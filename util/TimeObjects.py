class TimeCycleTrigger:
    def __init__(self, cycle_duration):
        self.cycle = cycle_duration
        self.time_elapsed = 0
        self.last_triggered_cycle = -1

    def trigger(self, dt):
        self.time_elapsed += dt
        current = int(self.time_elapsed // self.cycle)
        if current > self.last_triggered_cycle:
            self.last_triggered_cycle = current
            return True
        return False


class CountdownTimer:
    def __init__(self, duration):
        self.duration = duration
        self.remaining = 0

    def start(self):
        self.remaining = self.duration

    def is_alive(self, dt):

        if self.remaining > 0:
            self.remaining -= dt
            if self.remaining < 0:
                self.remaining = 0

        return self.remaining > 0
