import numpy as np
if __name__ == '__main__':
    # Make data.
    X = np.arange(-5, 5, 0.25)
    xlen = len(X)
    Y = np.arange(-5, 5, 0.25)
    ylen = len(Y)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)

    print(X.shape, Y.shape, Z.shape)

    print(type(Z))