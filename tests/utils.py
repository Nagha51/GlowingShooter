def fake_get_time(time_array):
    def time_generator():
        for time in time_array:
            yield time

    time_generated = time_generator()
    return lambda: next(time_generated)
