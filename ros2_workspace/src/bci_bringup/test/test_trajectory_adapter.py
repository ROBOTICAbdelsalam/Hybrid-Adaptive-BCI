"""Unit tests for the hand adapter's pure scaling logic (runs off-ROS)."""

from bci_bringup.scaling import scale_to_radians


def test_open_maps_to_zero():
    assert scale_to_radians([0.0] * 5, 1.4) == [0.0] * 5


def test_close_maps_to_max_flexion():
    assert scale_to_radians([1.0] * 5, 1.4) == [1.4] * 5


def test_midrange_scales_linearly():
    out = scale_to_radians([0.5], 1.4)
    assert abs(out[0] - 0.7) < 1e-9


def test_values_are_clamped_into_range():
    # Out-of-range inputs must never exceed the joint limit or go negative.
    out = scale_to_radians([-0.5, 1.5], 1.4)
    assert out == [0.0, 1.4]


def test_length_preserved():
    assert len(scale_to_radians([0.2, 0.9, 0.0, 1.0, 0.28], 1.4)) == 5
