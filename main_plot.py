import argparse
import json
import time
import streamlit as st

import numpy as np

from visualization import Vis, initial_and_final_schedule, schedule, video_parser

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", type=str,
                        help='Select the simulation you want to render: sim_vis or plot_schedule')
    args = parser.parse_args()

    save_file_name = ''
    if args.mode == "video":
        video_parser()
    elif args.mode == "sim_vis":
        with open(initial_and_final_schedule, "r+") as json_file:
            data = json.load(json_file)
        save_file_name = 'simulation.png'
    else:

        progress_bar = st.sidebar.progress(0)
        status_text = st.sidebar.empty()
        last_rows = np.random.randn(1, 1)
        chart = st.line_chart(last_rows)

        for i in range(1, 101):
            new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
            status_text.text("%i%% Complete" % i)
            chart.add_rows(new_rows)
            progress_bar.progress(i)
            last_rows = new_rows
            time.sleep(0.05)

        progress_bar.empty()

        # Streamlit widgets automatically run the script from top to bottom. Since
        # this button is not connected to any other logic, it just causes a plain
        # rerun.
        st.button("Re-run")
        # with open(schedule, "r+") as json_file:
        #     data = json.load(json_file)
        # save_file_name = 'schedule.png'

    gantt = Vis(data=data, from_file=True)
    gantt.plot_schedule(save_file_name)
