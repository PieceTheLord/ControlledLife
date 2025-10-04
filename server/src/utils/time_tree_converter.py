from collections import defaultdict
from typing import Any


def time_tree_converter(sessions: list[Any]):
    """
    @parms mainTitle, subtitle1, subtitle2, startTime, endTime, spentTime
    Convert Db.calculate_each_spent_time qeury into
    good structured tree
    """
    # Create base tree's structure
    time_tree = defaultdict(
        lambda: {
            "total_spent_time": 0,
            "subtitles": defaultdict(
                lambda: {
                    "total_spent_time": 0,
                    "subtitles": defaultdict(lambda: {"total_spent_time": 0}),
                }
            ),
        }
    )
    for mainTitle, subtitle1, subtitle2, startTime, endTime, spentTime in sessions:
        # Check the if the mainTitle isn't equalt to ""
        if mainTitle:
            time_tree[mainTitle]["total_spent_time"] += spentTime
        # Check the if the subtitle1 isn't equalt to ""
        if subtitle1:
            time_tree[mainTitle]["subtitles"][subtitle1][
                "total_spent_time"
            ] += spentTime
        # Check the if the subtitle2 isn't equalt to ""
        if subtitle2:
            time_tree[mainTitle]["subtitles"][subtitle1]["subtitles"][subtitle2][
                "total_spent_time"
            ] += spentTime
    # Convert all sessions into the tree
    time_tree = {
        main_title: {
            "total_spent_time": main_title_data["total_spent_time"],
            "subtitles": {
                subtitle1: {
                    "total_spent_time": subtitle1_data["total_spent_time"],
                    "subtitles": {
                        subtitle2: {
                            "total_spent_time": subtitle2_data["total_spent_time"]
                        }
                        for subtitle2, subtitle2_data in subtitle1_data[
                            "subtitles"
                        ].items()
                    },
                }
                for subtitle1, subtitle1_data in main_title_data["subtitles"].items()
            },
        }
        for main_title, main_title_data in time_tree.items()
    }
    return time_tree
