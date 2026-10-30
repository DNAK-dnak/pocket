"""Beats, onsets and timing feel."""


def beats(y, sr):
    """Return beat times in seconds and the estimated tempo."""
    raise NotImplementedError


def onsets(y, sr):
    """Return note onset times in seconds."""
    raise NotImplementedError


def timing_deviations(onset_times, beat_times, subdivision=4):
    """Return each onset's offset in milliseconds from the nearest grid position.

    Negative values are early (rushing), positive values are late (laid back).
    """
    raise NotImplementedError


def tempo_drift(beat_times):
    """Return local tempo over time, to show rushing or dragging across a take."""
    raise NotImplementedError


def swing_ratio(onset_times, beat_times):
    """Return the ratio between long and short eighth-note subdivisions."""
    raise NotImplementedError
