def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    input=x0
    for i in range(steps):
        f_i_x=(2*a*input)+b
        updated_x=input-lr*(f_i_x)
        input=updated_x
    return input
    