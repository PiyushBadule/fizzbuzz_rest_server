from typing import List

from pydantic import BaseModel, Field

from logs.logger import logger  # Import your custom logger


class FizzBuzzRequest(BaseModel):
    """
    Pydantic schema for FizzBuzz request data.

    Attributes:
        first_integer (int): First integer for FizzBuzz calculation.
        second_integer (int): Second integer for FizzBuzz calculation.
        sequence_limit (int): Limit for the FizzBuzz sequence.
        first_string (str): String to replace multiples of the first integer.
        second_string (str): String to replace multiples of the second integer.
    """
    first_integer: int = Field(..., gt=0, description="First integer for the FizzBuzz calculation")
    second_integer: int = Field(..., gt=0, description="Second integer for the FizzBuzz calculation")
    sequence_limit: int = Field(..., gt=0, description="Upper limit of the sequence for the FizzBuzz calculation")
    first_string: str = Field(..., min_length=1, description="String to replace multiples of the first integer")
    second_string: str = Field(..., min_length=1, description="String to replace multiples of the second integer")

    def __init__(self, **data):
        super().__init__(**data)
        # Example of adding logging within the model initialization
        logger.info(f"Initialized FizzBuzzRequest with data: {data}")


class FizzBuzzResponse(BaseModel):
    """
    Pydantic schema for FizzBuzz response data.

    Attributes:
        result (List[str]): List of strings representing the FizzBuzz sequence.
    """
    result: List[str] = Field(..., description="The result of the FizzBuzz calculation")

    class Config:
        schema_extra = {
            "example": {
                "result": ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "..."]
            }
        }

    def __init__(self, **data):
        super().__init__(**data)
        # Example of adding logging within the model initialization
        logger.info(f"Initialized FizzBuzzResponse with result: {data.get('result', [])}")
