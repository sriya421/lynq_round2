# lynq_round2
SETUP INSTRUCTIONS - 
prerequesites(softwares):
1. llm_call [python]
2. pdf_reader[python]
3. weather_mcp [python]
4. client_agent [nodejs, python, gemini CLI]

Clone the Repository:

git clone https://github.com/sriya421/lynq_round2.git
cd lynq_round2

Install Dependencies:
pip install -r requirements.txt

Configuration - 
Set Up Environment Variables:
Create a .env file based on a provided example file (.env.example).
 cp .env.example .env

Edit the .env file with your specific settings:
 [GEMINI_API_KEY]=[your_value]

Running the Project -
If using Python:

python [your_main_file].py

1. llm_call:
   Input: "What is the capital of france?"
   Output: Paris

2. pdf_reader:
   Input: "Summarise the first page of the pdf."
   Output: (gives summary)

3. weather_mcp:
   Server acts a tool for llm client to give responses to questions regarding the weather.

4. client_agent:
   Input: "What is the weather in hyderabad?"
   Output: Heavy rain expected in Hyderabad, around 31°C.
 
