import sys
def error_message_details(error,error_detail:sys):
    _,_,exc_tb= error_detail.exc_info()
    file_name= exc_tb.tb_frame.f_code.co_filename
    error_message=f' error occured in python script name {file_name}   line number {exc_tb.tb_lineno}   error message {str(error)}'




class CustomException(Exception):
    