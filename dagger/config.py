from math import *

MAP_IMAGE_FILENAME="map.png"
MAP_OBSTACLES_FILENAME="map_obstacles.txt"
APF_DATA_FILENAME="apf_data.csv"
NOISE=0.0
AGENT_RADIUS=10
AGENT_SUBGOALS=[[(227, 145, 0), (226, 211, 0), (230, 281, 0)]]
# For map.png
AGENT_SUBGOALS1=[[(166, 99, 0), (225, 246, 0), (427, 249, 0), (607, 202, 0), (638, 65, 0)], [(635, 101, 0), (547, 228, 0), (285, 248, 0), (218, 244, 0), (199, 85, 0)], [(599, 516, 0), (425, 523, 0), (364, 451, 0), (334, 386, 0)], [(301, 340, 0), (345, 423, 0), (397, 500, 0), (482, 524, 0), (625, 493, 0)], [(451, 341, 0), (430, 420, 0), (393, 519, 0), (295, 557, 0)]]
# For small_map.png
AGENT_SUBGOALS2=[[(227, 145, 0), (226, 211, 0), (230, 281, 0)]]
# For small_map2.png
AGENT_SUBGOALS3=[[(121, 148, 0), (123, 280, 0)]]
# For map2.png
AGENT_SUBGOALS4=[[(619, 187, 0), (416, 250, 0), (403, 83, 0)]]
# For map3.png
AGENT_SUBGOALS5=[[(564, 227, 0), (405, 227, 0), (406, 91, 0)], [(407, 119, 0), (436, 239, 0), (591, 188, 0)]]
# For map4.png
AGENT_SUBGOALS6=[[(163, 562, 0), (61, 468, 0)], [(68, 463, 0), (167, 554, 0)]]
# For squares_map.png
AGENT_SUBGOALS7=[[(400, 391, 0), (397, 222, 0)]]

#For warehouse scenarios
AGENT_SUBGOALS_W_1=[[(63, 545, 0), (173, 443, 0), (297, 302, 0)], [(235, 255, 0), (291, 422, 0), (54, 513, 0)]]
AGENT_SUBGOALS_W_2=[[(283, 555, 0), (398, 443, 0), (736, 546, 0)], [(740, 552, 0), (522, 445, 0), (302, 558, 0)], [(536, 272, 0), (529, 562, 0)]]

# For intersection_1.png
AGENT_SUBGOALS_I_1=[[(27, 291, 0), (237, 289, 0), (460, 278, 0), (714, 278, 0)], [(323, 541, 0), (329, 386, 0), (331, 215, 0), (330, 45, 0)], [(379, 67, 0), (374, 192, 0), (182, 324, 0), (53, 315, 0)], [(663, 313, 0), (476, 319, 0), (375, 228, 0), (370, 34, 0)]]



FIELD_OF_VIEW=radians(180)
NUMBER_OF_LIDAR_ANGLES=50
MAX_LIDAR_DISTANCE=1e9
VMAX=2
WMAX=radians(20)

class APF_PARAMS_1:
    kAttr=50
    distanceThresholdAttraction=1
    kRep=1e5
    sigma=2
    kParam=0.5

# For small_map2
class APF_PARAMS_2:
    kAttr=1000
    distanceThresholdAttraction=1
    kRep=1e5
    sigma=7
    kParam=0.5

# For map4
class APF_PARAMS_3:
    kAttr=50
    distanceThresholdAttraction=1
    kRep=1e5
    sigma=3
    kParam=0.5

# For squares_map
class APF_PARAMS_4:
    kAttr=1000
    distanceThresholdAttraction=1
    kRep=1e5
    sigma=1
    kParam=0.5

# For intersection_1
class APF_PARAMS_5:
    kAttr=50
    distanceThresholdAttraction=1
    kRep=1e5
    sigma=2
    kParam=0.5

class APF_PARAMS_S:
    kAttr=500
    distanceThresholdAttraction=1
    kRep=1e5
    sigma=4
    kParam=0.5