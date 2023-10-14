"""
Numerical integratoin using different numberical methods to solve them

"""




def trapezoidal_rule(func, a, b, n):
    """
    Numerical integration using the trapezoidal rule.
    
    Parameters:
        func (function): The function to be integrated.
        a (float): The lower limit of the integration.
        b (float): The upper limit of the integration.
        n (int): Number of trapezoids to use for approximation.
        
    Returns:
        float: Approximation of the definite integral of the function from a to b.
    """
    h = (b - a) / n
    integral = 0.5 * (func(a) + func(b))  # Area of the first and last trapezoids
    
    for i in range(1, n):
        integral += func(a + i * h)  # Area of intermediate trapezoids
    
    integral *= h  # Multiply by the width of each trapezoid
    return integral


def gaussian_quadrature(func, a, b, nodes, weights):
    """
    Numerical integration using Gaussian quadrature.
    
    Parameters:
        func (function): The function to be integrated.
        a (float): The lower limit of the integration.
        b (float): The upper limit of the integration.
        nodes (list): List of nodes for Gaussian quadrature.
        weights (list): List of corresponding weights for Gaussian quadrature.
        
    Returns:
        float: Approximation of the definite integral of the function from a to b.
    """
    integral = 0
    for i in range(len(nodes)):
        x_i = ((b - a) * nodes[i] + (b + a)) / 2  # Change of variable
        integral += weights[i] * func(x_i)
    integral *= (b - a) / 2
    return integral

# Define the function to be integrated
def example_function(x):
    return x**2

# Define the integration limits
a = 0
b = 1

# Define nodes and weights for Gaussian quadrature (for n=2)
nodes = [-1 / ((3) ** 0.5), 1 / ((3) ** 0.5)]
weights = [1, 1]

# Calculate the integral using Gaussian quadrature
result = gaussian_quadrature(example_function, a, b, nodes, weights)

# Print the result
print("Approximated Integral:", result)




# Example usage:
# Define the function to be integrated
def example_function(x):
    return x**2

# Define the integration limits
a = 0
b = 1

# Define the number of trapezoids
n = 1000

# Calculate the integral using the trapezoidal rule
result = trapezoidal_rule(example_function, a, b, n)

# Print the result
print("Approximated Integral:", result)
