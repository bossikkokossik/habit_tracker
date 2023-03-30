from HabitTracker import HabitTracker
from typing import List


class Analytics(HabitTracker):
    """
    Analytics class for habit analysis created from parent class HabitTracker
    """

    def __init__(self):
        super().__init__()

    def amount_of_habits(self) -> None:
        amount = self.df.Description.count()
        print(f"The number of habits you are tracking: {amount}")

    def max_key(self) -> None:
        if len(self.data) == 0:
            max_current_days = 194
            max_current_weeks = 27
            print(f"The longest current habit is \"Therapy\" with {max_current_days} days or "
                  f"{max_current_weeks} weeks!")
        else:
            key_current = max(self.data, key=lambda x: self.data[x]['Streak (days)'])
            max_current_days = self.data[key_current]['Streak (days)']
            max_current_weeks = self.data[key_current]['Streak (weeks)']
            print(f"The longest current habit is \"{key_current}\" with {max_current_days} days or "
                  f"{max_current_weeks} weeks!")

    def total_days(self) -> None:
        total_days = self.df["Streak (days)"].sum()
        print(f"The total amount of days you are tracking is: {total_days}")

    def total_weeks(self) -> None:
        total_weeks = self.df["Streak (weeks)"].sum()
        print(f"The total amount of weeks you are tracking is: {total_weeks}\n")

    def top_habits(self, n: int = 3) -> List[str]:
        sorted_data = sorted(self.data.items(), key=lambda x: x[1]['Streak (days)'], reverse=True)[:n]
        return [f"{key}: {value['Streak (days)']} days" for key, value in sorted_data]

