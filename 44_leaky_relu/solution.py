def leaky_relu(z: float, alpha: float = 0.01) -> float|int:
    if z > 0:
        return z
    else:
        return z * alpha

