from flask import Flask, jsonify, request
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio

app = Flask(__name__)

# Define the prompt
prompt = '''
Follow the exact same steps
1. Go to https://accounts.clickbank.com/login.htm.
2. Login with username "akashnikku1234@gmail.com" and password "Bhureshwar@505O@".
3. After logging in, navigate to the "Affiliate Marketplace" tab.
4. In the Affiliate Marketplace, open the "Top Offers" section.
5. Sort the offers by "Gravity: High to Low" given on the right side of the page.
6. Go to the bottom of the page and set "Results per page" to 50.
7. For each offer in the container, extract the offer name (the part before the first hyphen).
8. Create a comma-separated list of the first 50 offer names and print it.
'''

@app.route('/extract_offers', methods=['GET'])
async def extract_offers():
    llm = ChatOpenAI(model="gpt-4o")
    agent = Agent(task=prompt, llm=llm)

    # Running the agent to complete the task
    history = await agent.run()

    # Getting the final result from the agent (which is a string)
    result = history.final_result()

    if result:
        # Return the result as JSON
        return jsonify({"offers": result})
    else:
        return jsonify({"error": "No result"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
