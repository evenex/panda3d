from PandaModules import Vec3, Point3

UNPICKABLE = ['x-disc-visible', 'y-disc-visible', 'z-disc-visible',
              'gridBack', 'unpickable']

# For linmath operations
X_AXIS = Vec3(1,0,0)
Y_AXIS = Vec3(0,1,0)
Z_AXIS = Vec3(0,0,1)
NEG_X_AXIS = Vec3(-1,0,0)
NEG_Y_AXIS = Vec3(0,-1,0)
NEG_Z_AXIS = Vec3(0,0,-1)
ZERO_VEC = ORIGIN = Vec3(0)
UNIT_VEC = Vec3(1)
ZERO_POINT = Point3(0)

DIRECT_FLASH_DURATION = 1.5

MANIPULATION_MOVE_DELAY = 0.65

Q_EPSILON = 1e-10

DIRECT_NO_MOD = 0
DIRECT_SHIFT_MOD = 1
DIRECT_CONTROL_MOD = 2
DIRECT_ALT_MOD = 4

SKIP_NONE = 0
SKIP_HIDDEN = 1
SKIP_BACKFACE = 2
SKIP_CAMERA = 4
SKIP_UNPICKABLE = 8
SKIP_ALL = SKIP_HIDDEN | SKIP_BACKFACE | SKIP_CAMERA | SKIP_UNPICKABLE

