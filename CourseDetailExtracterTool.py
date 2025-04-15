#First we must import the Google genai module to make API requests to the required model.
#and other required modules
from google import genai
from os import getenv   #This is used for API KEY retreival

#Creating client using our API Keys
client = genai.Client(api_key=getenv("GeminiAPI"))

"""
As our goal is just to make a specialized tool that gets the Course info from in a specified 
JSON schema, we can make the promt to the model as a constant with a placeholder for the course name.
"""

#The promt has to give the model some context and should be minimal (to reduce number of tokens used).
prompt ='''For a given coursera course name, give me just the data of it in the following form, {
    "name": "Course Name",
    "provider": "Provider Name",
    "courseType": "spl" or "pc" or "sa",
    "subCourses": [ "Course 1", "Course 2", ... ] or [],
    "desc": "Description about the course",
    "certVal": 1 / 3 / 5 / 7 => 1 for low, 3 for special knowledge, 5 - moderate, 7 - high
}
My Aim is to become ML Engineer. I'm strong in Python. I know basic ML.
Now, the course name is '''
#Our prompt will use somewhere around 110 - 130 tokens.

#Now, we can test our model
def getCourseDetails(course_name :str):
    full_res = ""           #This will let us save the whole output
    #Passing on the contents to our model.
    response_stream = client.models.generate_content_stream(       
        model="gemini-2.0-flash-lite", 
        contents= prompt + course_name      
    )

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