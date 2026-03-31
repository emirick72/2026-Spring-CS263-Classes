from dataclasses import dataclass, field
from typing import Optional


class EssayQuestion:
    def __init__(self, title: str):
        """
        Standard constructor
        Function must accept a single str parameter (title) which serves as the question text.
        """
        self.question_text = title
        self.feedback_correct = None
        self.feedback_incorrect = None
        self.points = 0

    def __eq__(self, other):
        """
        Compares two EssayQuestion objects by comparing question text and no other fields.
        """
        if not isinstance(other, EssayQuestion):
            return NotImplemented
        return self.question_text == other.question_text

    def __repr__(self):
        """
        Generates debugging output.
        """
        return(
            f"EssayQuestion(\n"
            f'    question_text="{self.question_text}",\n'
            f'    feedback_correct="{self.feedback_correct}",\n'
            f'    feedback_incorrect="{self.feedback_incorrect}",\n'
            f"    points={self.points}\n"
            f")"
        )

    def __str__(self):
        """
        Generates production output.
        """
        return(
            f"Points: {self.points}\n\n"
            f"{self.question_text}\n\n"
            f"Feedback:\n\n"
            f"    Correct:\n"
            f"        {self.feedback_correct}\n\n"
            f"    Incorrect:\n"
            f"        {self.feedback_incorrect}"
        )