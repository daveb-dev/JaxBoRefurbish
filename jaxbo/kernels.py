
import jax.numpy as np
from jax import jit
from jax import lax

@jit
def RBF(x1, x2, params):
    output_scale = params[0]
    lengthscales = params[1:]
    diffs = np.expand_dims(x1 / lengthscales, 1) - \
            np.expand_dims(x2 / lengthscales, 0)
    r2 = np.sum(diffs**2, axis=2)
    return output_scale * np.exp(-0.5 * r2)

@jit
def RBF_frac(x1, x2, params):
    output_scale = params[0]
    lengthscales = params[1:]
    diffs = np.expand_dims(x1 / lengthscales, 1) - \
            np.expand_dims(x2 / lengthscales, 0)
    r2 = np.sum(lax.pow(lax.abs(diffs),0.2) , axis=2)
    return output_scale * np.exp(-0.5 * r2)

@jit
def Matern52(x1, x2, params):
    output_scale = params[0]
    lengthscales = params[1:]
    diffs = np.expand_dims(x1 / lengthscales, 1) - \
            np.expand_dims(x2 / lengthscales, 0)
    r2 = np.sum(diffs**2 + 1e-9, axis=2)
    return output_scale * (1.0 + np.sqrt(5.0*r2) + 5.0*r2/3.0) * np.exp(-np.sqrt(5.0*r2))

@jit
def Matern32(x1, x2, params):
    output_scale = params[0]
    lengthscales = params[1:]
    diffs = np.expand_dims(x1 / lengthscales, 1) - \
            np.expand_dims(x2 / lengthscales, 0)
    r2 = np.sum(diffs**2 + 1e-9, axis=2)
    return output_scale * (1.0 + np.sqrt(3.0*r2)) * np.exp(-np.sqrt(3.0*r2))

@jit
def RatQuad(x1, x2, params):
    alpha = 1.0
    output_scale = params[0]
    lengthscales = params[1:]
    diffs = np.expand_dims(x1 / lengthscales, 1) - \
            np.expand_dims(x2 / lengthscales, 0)
    r2 = np.sum(diffs**2, axis=2)
    return output_scale * np.power(1.0 + (0.5/alpha) * r2, -alpha)
