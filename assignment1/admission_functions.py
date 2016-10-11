SPECIAL_CASE_SCHOOL_1 = 'Fort McMurray Composite High'
SPECIAL_CASE_SCHOOL_2 = 'Father Mercredi High School'
SPECIAL_CASE_YEAR = '2016'
NO_EXAM = 'NE'

# Add other constants here

def second(record, coursework_mark, exam_mark):
    if exam_mark != 'NE':
        return (float(coursework_mark) + float(exam_mark)) / 2
    if is_special_case(record):
        return float(coursework_mark)
    else:
        return float(coursework_mark) / 2 
def is_special_case(record):
    """ (str) -> bool

    Return True iff the student represented by record is a special case.

    >>> is_special_case('Jacqueline Smith,Fort McMurray Composite High,2016,MAT,90,94,ENG,92,88,CHM,80,85,BArts')
    True
    >>> is_special_case('Jacqueline Smith,Father Something High School,2016,MAT,90,94,ENG,92,88,CHM,80,85,BArts')
    False
    >>> is_special_case('Jacqueline Smith,Fort McMurray Composite High,2015,MAT,90,94,ENG,92,88,CHM,80,85,BArts')
    False
    """

    # Complete the body of the function here
    record_list = record.split(',')
    if record_list[1] == SPECIAL_CASE_SCHOOL_1 or record_list[1] == \
    SPECIAL_CASE_SCHOOL_2:
        if record_list[2] == SPECIAL_CASE_YEAR:
            return True
    return False

def get_final_mark(record, coursework_mark, exam_mark):
    
    """(str, str, str) => float
    
    Return a student's final mark in a certain course considering if the student
    experienced the special case
    
    >>> get_final_mark('Jacqueline Smith,Fort McMurray Composite High,2016,MAT,90,94,ENG,92,88,CHM,80,85,BArts', '90', '85')
    87.5
    >>> get_final_mark('Jacqueline Smith,Fort McMurray Composite High,2016,MAT,90,94,ENG,92,88,CHM,80,85,BArts', '90', 'NE')
    90.0
    >>> get_final_mark('Jacqueline Smith,Whatever high school,2015,MAT,90,94,ENG,92,88,CHM,80,85,BArts', '90', 'NE')
    45.0
    """
    
    if exam_mark == NO_EXAM and is_special_case(record):
        return float(coursework_mark)
    elif exam_mark == NO_EXAM and not is_special_case(record):
        return float(coursework_mark)/2
    else:
        return (float(coursework_mark) + float(exam_mark))/2
    
def get_both_marks(course_record, course_code):
    
    """(str, str) -> str
    
    Return a string containing a student's both marks in the certain course passed in parameters
    seperated by a comma, or an empty string if the course code doesn't match the
    course record.
    
    >>>get_both_marks('MAT,90,94', 'MAT')
    '90 94'
    >>>get_both_marks('MAT,90,94', 'ENG')
    ''
    """
    
    course_record_list = course_record.split(',')
    if course_record_list[0] == course_code:
        return course_record_list[1] + ' ' + course_record_list[2]
    else:
        return ''
    
def extract_course(transcript, course_index):
    
    """(str, int) -> str
    
    Precondition: course_index should be equal to or less the the amount of course
    records in transcript
    
    Return a course record selected according to the student transcript and 
    course_index passed as parameters
    
    >>>extract_course('MAT,90,94,ENG,92,NE', 2)
    'ENG,92,NE'
    >>>extract_course('MAT,90,94,ENG,92,NE,CHM,80,85', 1)
    'MAT,90,94'
    """
    transcript_list = transcript.split(',')
    course_code_index = (course_index - 1) * 3
    return transcript_list[course_code_index] + ',' + transcript_list[
        course_code_index + 1] + ',' + transcript_list[course_code_index + 2]
     
def applied_to_degree(record, degree):
    
    """(str, str) -> bool
    Return true if and only if the student from the record as the first paramter
    has applied to the degree passed as the second parameter.
    
    >>>applied_to_degree('Jacqueline Smith,Fort McMurray sComposite High,2016,MAT,90,94,ENG,92,88,CHM,80,85,BArts', 'BEng')
    False
    >>>applied_to_degree('Jacqueline Smith,Fort McMurray sComposite High,2016,MAT,90,94,ENG,92,88,CHM,80,85,BArts', 'BArts')
    True
    """
    
    record_list = record.split(',')
    return record_list[-1] == degree

def decide_admission(average_mark, course_cutoff):
    
    """(number, number) -> str
    
    Return corresponding admission decisions from school based on the 
    course_cutoff and average_mark
    
    >>>decide_admission(90, 91)
    'reject'
    >>>decide_admission(92, 91)
    'accept'
    >>>decide_admission(90, 85)
    'accept with scholarship'
    """
    
    if average_mark < course_cutoff:
        return 'reject'
    elif average_mark >= course_cutoff and average_mark < (course_cutoff + 5):
        return 'accept'
    else:
        return 'accept with scholarship'
    
