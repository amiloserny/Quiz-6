#Amanda Miloserny
import math
class Ambulance:
    """The associated features are priority, speed, and capacity."""

amb_1 = Ambulance()
amb_1.priority = 0
amb_1.capacity = 4
amb_1.speed = 100

# def self(priority):
#     if priority == 0:
#         print("There is no patient in the ambulance.")
#     elif priority == 1:
#         print("There is a patient in the ambulance.")

# def max(speed):

def controlled_velocity(priority, speed, capacity):
    velocity = (1 - priority) + 2.37 * (speed / 10) ** 3.98 + 30 * (capacity + 1.2)
    return velocity

print(controlled_velocity(amb_1.priority, amb_1.speed, amb_1.capacity))
