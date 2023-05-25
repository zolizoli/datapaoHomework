import csv
import itertools
from datetime import datetime


def preprocess_data(csv_path):
    """
    Correcting errors
    Returns the file name of the corrected csv
    """
    # correct the input since we have UPPER and lower case versions of some fields
    # the tasks says >>They provided data for 2023 February<< but we have data for January and March too
    fname = csv_path.split(".")[0] + "_corrected.csv"
    with open(fname, "w") as outfile:
        with open(csv_path, "r") as infile:
            gatein = 0
            gateout = 0
            for line in infile:
                if "2023-03-" not in line and "2023-01-" not in line:
                    line = line.replace("gate_in", "GATE_IN").replace(
                        "gate_out", "GATE_OUT"
                    )
                    gatein += line.count("GATE_IN")
                    gateout += line.count("GATE_OUT")
                    outfile.write(line)
            assert gatein == gateout
    return fname


# we need a generator of the rows, so the solution can be scaled up to bigger csv-s
def rows_from_a_csv_file(filename, skip_first_line=False):
    """
    Reads a csv file and returns a generator of the rows
    Source: https://gist.github.com/pfigue/7950818 - slightly modified
    """
    with open(filename, "r") as csv_file:
        reader = csv.DictReader(
            csv_file,
        )
        if skip_first_line:
            next(reader, None)
        for row in reader:
            yield row


def calculate_stats(rows):
    """calculate stats on generators using itertools.groupby"""
    ## helper functions for sorting
    def by_user_id(row):
        return row["user_id"]

    def by_event_day(row):
        return datetime.fromisoformat(row["event_time"]).day

    sorted_rows = sorted(rows, key=by_user_id)
    grouped_by_user = itertools.groupby(sorted_rows, by_user_id)

    res1 = []
    res2 = []
    for k, infos in grouped_by_user:
        sorted_infos = sorted(infos, key=by_event_day)
        grouped_by_day = itertools.groupby(sorted_infos, by_event_day)
        no_of_days_in_office = (
            0  # days - the number of calendar days the user was present in the office
        )
        total_time_in_office = 0  # time - net hours spent in the office
        for day, v in grouped_by_day:
            grouping = list(v)
            intimes = [
                datetime.fromisoformat(e["event_time"])
                for e in grouping
                if e["event_type"] == "GATE_IN"
            ]
            outtimes = [
                datetime.fromisoformat(e["event_time"])
                for e in grouping
                if e["event_type"] == "GATE_OUT"
            ]
            if len(outtimes) > len(intimes):
                intimes.insert(
                    0,
                    datetime.fromisoformat(
                        grouping[0]["event_time"].split("T")[0] + "T00:00:00.000Z"
                    ),
                )  # intime was yesterday
            if len(outtimes) < len(intimes):
                outtimes.append(
                    datetime.fromisoformat(
                        grouping[0]["event_time"].split("T")[0] + "T23:59:59.999Z"
                    )
                )  # outtime should be midnight
            assert len(intimes) == len(outtimes)

            # total time
            paired_events = list(zip(intimes, outtimes))
            paired_deltas = [(e[1] - e[0]).seconds / (60 * 60) for e in paired_events]

            # breaks
            breaks_btw_sessions = list(zip(intimes[1:], outtimes[:-1]))
            assert len(breaks_btw_sessions) == len(paired_deltas) - 1
            break_deltas = [(e[0] - e[1]).seconds / 3600 for e in breaks_btw_sessions]
            significant_break_point_indices = [
                break_deltas.index(e) + 1 for e in break_deltas if e >= 2
            ]
            if significant_break_point_indices:
                significant_break_point_indices.append(
                    len(paired_deltas)
                )  # extra index for easier looping
                sessions = []
                onset = 0
                for i in significant_break_point_indices:
                    offset = i
                    sessions.append(paired_deltas[onset:offset])
                    onset = offset
                sessions = [sum(e) for e in sessions]
            else:
                sessions = [sum(paired_deltas)]

            # stats
            daily_total_time = sum(paired_deltas)
            no_of_days_in_office += 1
            total_time_in_office += daily_total_time
        if no_of_days_in_office:
            avg_daily_time_in_office = total_time_in_office / no_of_days_in_office
        else:
            avg_daily_time_in_office = (
                0  # maybe someone is on holiday or working from home
            )
        res1.append(
            (
                k,
                str(total_time_in_office),
                str(no_of_days_in_office),
                str(avg_daily_time_in_office),
            )
        )
        res2.append((k, str(max(sessions))))

    res1 = sorted(res1, key=lambda t: t[3], reverse=True)
    res2 = sorted(res2, key=lambda t: t[1], reverse=True)

    return res1, res2


def write_output(res1, res2, outdir):
    with open(f"{outdir}/first.csv", "w") as outfile_res1:
        h = "user_id,time,days,average_per_day,rank\n"
        outfile_res1.write(h)
        i = 1
        for e in res1:
            outfile_res1.write(",".join(e) + f",{i}\n")
            i += 1

    with open(f"{outdir}/second.csv", "w") as outfile_res2:
        h = "user_id,session_length,rank\n"
        outfile_res2.write(h)
        j = 1
        for e in res2:
            outfile_res2.write(",".join(e) + f",{j}\n")
            j += 1


if __name__ == "__main__":
    corrected_csv = preprocess_data("data/datapao_homework_2023.csv")
    rows = rows_from_a_csv_file(corrected_csv, skip_first_line=True)
    res1, res2 = calculate_stats(rows)
    write_output(res1, res2, "output")
