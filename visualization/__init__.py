import os

from visualization.graphs import Vis
from visualization.json_2_video import video_parser
from visualization.web_visualization import Web_vis

initial_and_final_schedule = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   'data_for_visualization/initial_and_final_schedule.json')
schedule = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                           'data_for_visualization/schedule.json')

allocation_method_vis = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   'data_for_visualization/allocation_method_visualization')
