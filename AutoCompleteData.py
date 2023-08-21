from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    """
    @summary:
        A class that represents data for a single completion of a sentence.
    @completed_sentence: str
        The completed sentence for a user's search.
    @source_text: str
        The source text from which the sentence was completed.
    @offset: int
        The offset of the completed sentence in the source text.
        In other words, the position of the first word of the completed sentence in the full sentence.
    @score: int
        The score of the completion.
        Higher score means higher confidence in the completion.
    """
    def __init__(self: object, completed_sentence: str, source_text: str, offset: int, score: int) -> None:
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.offset = offset
        self.score = score

    def __gt__(self: object, other: object) -> bool:
        """
        @summary:
            Operator overloading for the '>' operator.
            Compares two AutoCompleteData objects by their score.
        @param self:
            This AutoCompleteData object.
        @param other:
            AN other AutoCompleteData object.
        @return bool:
            True if self.score > other.score, False otherwise.
        """
        return self.score > other.score

    def __str__(self: object) -> str:
        """
        @summary:
            Operator overloading for the 'str()' function.
            Returns
        @param self:
            This AutoCompleteData object.
        @return str:
            the completed sentence.
        """
        return self.completed_sentence

    def get_score(self: object) -> int:
        """
        @summary:
            Returns the score of this AutoCompleteData object.
        @param self:
            This AutoCompleteData object.
        @return int:
            The score of this AutoCompleteData object.
        """
        return self.score

    def get_completed_sentence(self: object) -> str:
        """
        @summary:
            Returns the completed sentence of this AutoCompleteData object.
        @param self:
            This AutoCompleteData object.
        @return str:
            The completed sentence of this AutoCompleteData object.
        """
        return self.completed_sentence

    def get_source_text(self: object) -> str:
        """
        @summary:
            Returns the source text of this AutoCompleteData object.
        @param self:
            This AutoCompleteData object.
        @return str:
            The source text of this AutoCompleteData object.
        """
        return self.source_text

    def get_offset(self: object) -> int:
        """
        @summary:
            Returns the offset of this AutoCompleteData object.
        @param self:
            This AutoCompleteData object.
        @return int:
            The offset of this AutoCompleteData object.
        """
        return self.offset

    def copy(self: object) -> object:
        """
        @summary:
            Returns a copy of this AutoCompleteData object.
        @param self:
            This AutoCompleteData object.
        @return object:
            A copy of this AutoCompleteData object.
        """
        return AutoCompleteData(self.completed_sentence, self.source_text, self.offset, self.score)




