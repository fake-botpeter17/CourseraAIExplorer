#First we must import the Google genai module to make API requests to the required model.
#and other required modules
from google import genai
from os import getenv   #This is used for API KEY retreival


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

    def getCourseDetails(self, course_name :str):
        full_res = ""           #This will let us save the whole output
        #Passing on the contents to our model.
        response_stream = self.__client.models.generate_content_stream(       
            model=self.__model, 
            contents= self.__prompt + course_name      
        )
        #The response_stream is a generator that yields the response from the model in chunks.
        #We can use this to print the response as it is generated.
        for chunk in response_stream:       #This will print our response to the terminal
            if chunk.text:
                print(chunk.text, end="", flush=True)
                full_res += chunk.text
        
        print()

        with open(f"Course Details//{course_name}.json", "w") as f:         #Writing the output to a file for later access.
            f.write(full_res)

if __name__ == "__main__":
    course = input("Enter the course name to fetch the details for:\t") #Mathematics for Machine Learning
    getCourseDetails(course)