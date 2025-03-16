**Prompt Software description - 1**: (o3 mini)
You are a product expert with experience in ATS (Applicant tracking System). What are the core functionalities of an ATS? List them in order of priority. The expected output must be in a markdown format I can copy paste

**Prompt Software description - 2**: (Cursor agent claude 3.7-sonnet-thinking)
You are a product expert with experience in ATS (Applicant tracking System). Use the file @core_fonctionalities.md to add the following data in the file @LTI-OS.md  :
1. a brief description of the ATS software
2. The benefits to use this software
3. Explian the core fonctionalities

The expected output is a markdown format


Lean canvas created with Canvanizer

=================================================================================

**Prompt Use cases - 1**: (Cursor agent claude 3.7-sonnet-thinking)
You are a senior software analyst with strong knowledge in use cases and diagrams. You use @core_fonctionalities.md to perform the following actions:
1. create a markdown file with the 3 main use cases, you call it main_use_cases.md
2. For each one of these use cases you will create the corresponding diagram written as mermaid. You will add these instructions in the main_use_cases.md file at the corresponding place.

**Prompt Use cases - 2**: (Cursor agent claude 3.7-sonnet-thinking)
You are a senior software analyst with strong knowledge in use cases and diagrams. You use @core_fonctionalities.md to perform the following actions:
1. create a markdown file with the 3 main use cases, you call it main_use_cases.md
2. For each one of these use cases you will create the corresponding diagram written as mermaid. You will add these instructions in the main_use_cases.md file at the corresponding place.

**Prompt Uses cases - 3**: (Cursor agent claude 3.7-sonnet-thinking)
In the same way I want you to update the 2 other use cases from mermaid to UML format for the same reasons



**Prompt Database - 1**: (Cursor agent claude 3.7-sonnet-thinking)
You are a senior software architect, you use the @v2 folder to create the needed database architecture. It includes all the entities and all their attributes with all the needed relationships. The expected output is a UML format to be able to generate an image from it. You will then explain all your choices below this output.


**Prompt Hih level architecture**:

You are a senior software architect with a lot of experience and knowledge in microservices and cloud architecture. You use the data from @v2 to create an architecture serve in cloud with microservices to fit all the requirements for the software. The expected output is a very detailed description of the final architecture using cloud AWS solutiions. Here is an example of the expected output but it is only a short description, I expect a much more detailed one:
"a microservices architecture for an ATS , each MS has its own database. It also has a frontend that communicates throught out API. The cloud provider is AWS, it use proper services including CDN and cloud balancing.". After the ouput is written,  you will explain briefly your design and add this explanation at the end of @LTI-OS.md 


**Prompt C4 diagram - 1**:
use the @LTI-OS.md file and list me all the existing existing containers in a bullet list with only the names of the containers.

**Prompt C4 diagram - 2**:
Now I want you to list me all the componenst in a bullet list of the job service container

**Prompt C4 diagram - 3**:
Now I want you to list me all the componenst in a bullet list of the job service container

**Prompt C4 diagram - 4**:

I want you to generate a UML code to create a multi-level c4 diagram for the container Job Service and its component Job posting Service. The expected diagram to generate with your UML code looks like @c4_template2.png