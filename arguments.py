# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"
import time

# Add your code after this line
def greet(name, template="Hello, <name>!"):
    x = template.replace("<name>", name)
    return x


print(greet("Mark Rutten"))


def force(mass, body="earth"):
    planet_gravity = {
        "sun": 274.0,
        "jupiter": 24.9,
        "neptune": 11.2,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6,
    }
    output = mass * planet_gravity[body]
    return output


print(force(10.0))


def pull(m1, m2, d):

    pull_force = 6.674e-11 * ((m1 * m2) / d**2)

    return pull_force


print(pull(1500, 800, 3))
