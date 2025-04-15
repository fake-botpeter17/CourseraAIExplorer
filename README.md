The current Idea is to create a Tool that uses Google's Gemini API to fetch the course details that I want in a JSON format which I'll be able to use for further processing using Python.


-------------------------------------------------------------------

Errors to be fixed:
1. The response contains prefix and ```json and suffix of ```. We must remove it before writing to the JSON file.
2. Files should be saved to "Course Details/" direc.
3. The function must be callable from other files as well. (Make this as a class maybe)
4. The connection to the API should not be initialised for each course request. (The class approach will fix this too).