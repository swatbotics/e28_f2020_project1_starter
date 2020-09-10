######################################################################
#
# starter.py 
# Matt Zucker
#
######################################################################

import numpy
import sys, os
from importlib_resources import open_text

from ursim import RoboSimApp, ctrl

######################################################################

class Project1Controller(ctrl.Controller):

    def __init__(self):
        super().__init__()
        self.app = None

    def initialize(self, time, odom_pose):
        print('initialize was called!')

    def setup_log(self, datalog):
        print('setup_log was called!')

    def update(self, time, dt, robot_state, camera_data):
        # TODO: writeme
        return None
            
######################################################################

def setup_sim(sim):

    sim.set_dims(8.0, 6.0)

    t = numpy.linspace(0, 1, 33)
    
    x = 1.0 + 6.0*t
    y = 3.0 + 0.5*numpy.sin(t*4*numpy.pi)

    pts = numpy.vstack((x, y)).transpose()

    sim.add_tape_strip(pts, 'blue')

    sim.initialize_robot((0.5, 3.0), 0.0)

######################################################################

def main():

    svg_file = None
    
    if len(sys.argv) > 1 and sys.argv[1].endswith('svg'):
        svg_file = sys.argv[1]
        if not os.path.exists(svg_file):
            svg_file = open_text('ursim.environments', svg_file)

    controller = Project1Controller()

    app = RoboSimApp(controller)

    if svg_file is not None:
        app.sim.load_svg(svg_file)
    else:
        setup_sim(app.sim)
    
    app.run()

if __name__ == '__main__':
    main()
