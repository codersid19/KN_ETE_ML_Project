import sys
import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    e = str(error)

    error_msg = f"Error occured in python script name {filename} at line number {line_number} : error message {e}"

    return error_msg


class CustomException(Exception):
    def __init__(self, error_msg, error_details:sys):
        super.__init__(error_msg)
        self.error_msg = error_message_detail(error_msg, error_details=error_details)
    
    def __str__(self):
        return self.error_msg
    







