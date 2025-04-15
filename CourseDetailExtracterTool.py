#First we must import the Google genai module to make API requests to the required model.
#and other required modules
from google import genai
from os import getenv, makedirs   #This is used for API KEY retreival
from time import sleep
from re import sub
import sys


class CourseDetailExtracterTool:
    """
    This is a tool that uses the Google Gemini model to extract course details from a given course name.
    """
    def __init__(self) -> None:
        #Creating client using our API Keys
        self.__client = genai.Client(api_key=getenv("GeminiAPI"))   #Making a client using the API key from the environment variable.
        self.__model = "gemini-2.0-flash-lite"   #The model we are using is the Gemini 2.0 Flash Lite model.
        """
        As our goal is just to make a specialized tool that gets the Course info from in a specified 
        JSON schema, we can make the promt to the model as a constant with a placeholder for the course name.
        """
        self.__prompt = '''For a given coursera course name, give me just the data of it in the following form, {
        "name": "Course Name",
        "provider": "Provider Name",
        "courseType": "spl" or "pc" or "sa",
        "subCourses": [ "Course 1", "Course 2", ... ] or [],
        "desc": "Description about the course",
        "certVal": 1 / 3 / 5 / 7 => 1 for low, 3 for special knowledge, 5 - moderate, 7 - high
    }
    My Aim is to become ML Engineer. I'm strong in Python. I know basic ML.
    Now, the course name is '''
    #The promt has to give the model some context and should be minimal (to reduce number of tokens used).
    #Our prompt will use somewhere around 110 - 130 tokens.

    def getCourseDetails(self, course_name :str, print_res:bool = False, write_file: bool = True) -> None:
        #Passing on the contents to our model.
        response = self.__client.models.generate_content(       
            model=self.__model, 
            contents= self.__prompt + course_name      
        )
        cleaned_json = sub(r"```(?:json)?\s*([\s\S]*?)\s*```", r"\1", response.text)  #Cleaning the response to get the JSON data.
        if print_res:
            self.printContent(cleaned_json)
        if write_file:
            self.writeFile(course_name, cleaned_json)
        
    def printContent(self, response, stream_delay = 0.01) -> None:
        for char in response:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(stream_delay)
        print()  # For newline after the stream

    def writeFile(self, course_name: str, content: str) -> None:
        """
        This function will write the content to a file.
        """
        try:
            makedirs("Course Details")   #Creating the directory if it does not exist.
        except FileExistsError:
            pass
        with open(f"Course Details//{course_name}.json", "w") as f:         #Writing the output to a file for later access.
            f.write(content)
