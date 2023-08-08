from scheduling.scheduling_split_tasks import Schedule, schedule_as_dict
from control.control_logic import ControlLogic
from visualization.json_2_video import video_parser
from visualization import schedule
from control.jobs import Job
import argparse
import logging
import json

if __name__ == '__main__':
    cases = ['1', '2', '3', '4', '5', '6']
    # execute_job = ControlLogic('5')
    # execute_job.run(online_plot=True)

    parser = argparse.ArgumentParser()
    parser.add_argument("case", type=str, help='Choose one of this: 1, 2, 3, 4, 5, 6')
    parser.add_argument('--only_schedule', action=argparse.BooleanOptionalAction)
    parser.add_argument('--animation', action=argparse.BooleanOptionalAction)
    parser.add_argument('--log_error', action=argparse.BooleanOptionalAction)
    parser.add_argument('--log_debug', action=argparse.BooleanOptionalAction)
    parser.add_argument('--online_plot', action=argparse.BooleanOptionalAction)


    args = parser.parse_args()
    if args.log_error:
        lvl = logging.ERROR
    elif args.log_debug:
        lvl = logging.DEBUG
    else:
        lvl = logging.INFO
        logging.basicConfig(level=lvl,
                            format=f"%(levelname)-8s: - %(message)s")
    logging.getLogger("mylogger")

    if args.case in cases:
        case = args.case
    else:
        logging.error("The case does not exist")
        raise SystemExit(1)

    if not args.only_schedule:
        execute_job = ControlLogic(case)
        execute_job.run(online_plot=True) if args.online_plot else execute_job.run(online_plot=False)
        execute_job.run(animation=True) if args.animation else execute_job.run(animation=False)
        if args.animation:
            video_parser()
    else:
        job = Job(case)
        schedule_model = Schedule(job)
        output = schedule_model.set_schedule()
        with open(schedule, "w") as outfile:
            json.dump(schedule_as_dict(output), outfile)
            logging.info(f'Save data to {schedule}')


