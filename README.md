For creating this Backend Translation Microservice I followed the steps given below

Step-1: Create Project Directory:
To create a Project directory I opened a Command Prompt using the cmd shortcut in my Computer and then set the path to Downloads then I created a directory under this Downloads as project_udaan using the command below and it is given as mkdir project_udaan and then change the path into the respective directory using cd project_udaan.
-C:\Users\hp>cd Downloads
-C:\Users\hp\Downloads>mkdir project_udaan
-C:\Users\hp\Downloads>cd project_udaan  

Step-2: Initialize Virtual Environment:
After setting the path to our project directory and then initialize the Virtual Environment using python  -m venv venv and then activate the scripts using venv\Scripts\activate.
-C:\Users\hp\Downloads>cd project_udaan  
-C:\Users\hp\Downloads\project_udaan>python -m venv venv
-C:\Users\hp\Downloads\project_udaan>venv\Scripts\activate
It results in the creation of our Virtual Environment
(venv) C:\Users\hp\Downloads\project_udaan>

Step-3: Install Dependencies:
After creating a Virtual Environment for our project directory and then there is a need to install the dependencies as it is a requirement to build RESTful API(Preferably FAST API) and then the Translator API to include googletrans and then others are included that are required for our project. To install these dependencies there is a requirement of a pip command which is pip install fastapi uvicorn googletrans==4.0.0-rc1 pydantic.(install all these using this command).
(venv) C:\Users\hp\Downloads\project_udaan>pip install fastapi uvicorn googletrans==4.0.0-rc1 pydantic (All these dependencies are installed)
(venv) C:\Users\hp\Downloads\project_udaan>pip install pytest (Optional for testing our microservice it is installed using this command)

Step-4: Create Separate folders in our main directory(project_udaan):
Firstly, to enter this project I have assumed the architecture of this entire project like this 
project_udaan /
      -main.py 
       routes /
       -translator_routes.py  
    services  /
    -translator.py  
    utils /  
    -validators.py
   db /
   -logger.py
  models / 
  -schemas.py
  tests /
  -test_translation.py  

Step-5:Consider the main.py file:
After assuming the above structure of folders and their respective python files and then enter the creation of main.py file in our main directory of project_udaan. This file majorly contains the code of Home Page. 
Explanation:
In this file, the main entry points exist to return the home page of the entire project that describes the title and description, and the endpoint is also defined which can be given as GET /Read Root and we can majorly see that it was implemented by FastAPI which displays the final output present in the above.

Step-6:Consider the translator_routes.py file:
In the translator_routes.py file which is saved in the folder of routes to determine the API routes also I have included the Language reference ISO codes for the respective language to test it accordingly.
Explanation:
In this file of translator_routes.py I have created all the required schemas to provide the input and get the output such as SingleTranslationInput, SingleTranslationOutput, BulkTranslationInput, BulkTranslationOutput and TranslationLogRecord to perform various operations to convert to a particular language and also language reference is also provided with their ISO codes to notify by the user and then if any input validation is failed to provide the respective error messages are also provided in the file. Here the endpoints can be GET /Supported languages, POST /SingleTranslate, and, POST /Translate/Bulk.

Step-7:Consider the translator.py file:
In the translator.py file which is saved in the folder of services and here there is an introduction of Google Translate API which is googletrans where I installed initially and it is majorly used by the allowed languages above are available under googletrans API to translate to the particular destination language that we have chosen from the list of languages available and it is supported by googletrans API.
Explanation:
In this file, the major translation code is involved where from the googletrans the translator is imported and then the original text or input text of some chars is taken as input and then we choose the destination language as well to translate and then it determines the output if all the validations are either correct or incorrect. It means if any input validation fails it generates the output accordingly I have mentioned to generate the error message of that respective particular error and this can be well understood in the validators.py file.

Step-8:Consider the validators.py file:
In this file of validators.py which is saved in the folder of utils and here the input validation is involved and consists of length of text validation which is between 0 and 1000 chars and the allowed languages are involved which can be translated using googletrans API.
Explanation:
In this file, the input validation is provided. It means the length of the text is considered to give the input which is up to 1000 chars is allowed and then the allowed languages list is also provided. If any input validation is failed then it will generate the respective errors as I have mentioned in the translator_routes.py file.

Step-9:Consider the logger.py file:
In this file of logger.py which is saved in the folder of db and here SQLite3 is used as the database to store the records of executed ones which includes record_id, original_text, translated_text, language, and translated_at(particular time).
Explanation:
In this file, the SQLite3 database is used where the records are stored in the form of logs which are defined by the endpoint GET /logs Get Translation Logs.

Step-10:Consider the schemas.py file:
In the file schemas.py which is saved in the folder of models where the data validation is provided using the pydantic library where I installed previously and here the input is provided as input_text and destination_language.
Explanation:
In this file, we can check all the available schemas that I have mentioned in the translator_routes.py file are present perform all the operations, and store those operations in the form of logs as well as reflect the translator_routes.py file.

Step-11: Consider the test_translation.py file:
Explanation:
Here in this file of test_translation.py file, I have included all the test validations to check the input validation and provided various test cases to check and generate the output accordingly.

Step-12: Final Execution:
After all this installation and creation of folders and their respective python files in the root directory of project_udaan. To get this execution of this microservice I have executed using this command which is uvicorn main:app  - -reload.
(venv) C:\Users\hp\Downloads\project_udaan> uvicorn main:app  - -reload
1)After executing this the command prompt displays the Application Startup complete.
2)Then after this I have chosen to enhance this by having a Streamlit UI as frontend.
3)For this, in the project root directory of project_udaan I have created separate folders for 
   Backend as Backend-Translator and Frontend as Frontend-Translator.
4) So, to get the final execution change the path to Backend-Translator(a newly created folder 
    where all the previous folders and their respective python files are transferred and stored in 
    this folder) and then execute as shown below.
    (venv) C:\Users\hp\Downloads\project_udaan>cd Backend-Translator
    (venv) C:\Users\hp\Downloads\project_udaan>Backend-Translator> uvicorn main:app  --reload









 
