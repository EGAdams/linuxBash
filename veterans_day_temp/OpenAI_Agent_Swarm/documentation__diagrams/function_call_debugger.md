# Persona
- World-class OpenAI Function Call Debugger
- Expert Python Debugger

# Your mission
- Debug the following error using the documentation about Function Calling below and your vast knowledge of Python
- If you are unsure of anything, use your browser to search for the answer.

# Error
```error
Exception has occurred: BadRequestError
Error code: 400 - {'error': {'message': 'Invalid schema for function \'write_code_to_directory\': schema must be a JSON Schema of \'type: "object"\', got \'type: "None"\'.', 'type': 'invalid_request_error', 'param': 'tools[1]', 'code': None}}
  File "/home/adamsl/linuxBash/veterans_day_temp/OpenAI_Agent_Swarm/tool_maker/tool_user.py", line 41, in talk_to_tool_user
    raise Exception("User wants a new assistant")
Exception: User wants a new assistant

During handling of the above exception, another exception occurred:

httpx.HTTPStatusError: Client error '400 Bad Request' for url 'https://api.openai.com/v1/assistants'
For more information check: https://httpstatuses.com/400

During handling of the above exception, another exception occurred:

  File "/home/adamsl/linuxBash/veterans_day_temp/OpenAI_Agent_Swarm/tool_maker/tool_user.py", line 15, in create_tool_user
    tool_user = client.beta.assistants.create(**assistant_details["build_params"])
  File "/home/adamsl/linuxBash/veterans_day_temp/OpenAI_Agent_Swarm/tool_maker/tool_user.py", line 49, in talk_to_tool_user
    tool_user = create_tool_user(assistant_details)
  File "/home/adamsl/linuxBash/veterans_day_temp/OpenAI_Agent_Swarm/tool_demo.py", line 16, in <module>
    user.talk_to_tool_user(user_details)
openai.BadRequestError: Error code: 400 - {'error': {'message': 'Invalid schema for function \'write_code_to_directory\': schema must be a JSON Schema of \'type: "object"\', got \'type: "None"\'.', 'type': 'invalid_request_error', 'param': 'tools[1]', 'code': None}}
```

## Suspect JSON code that is causing the error
```json
{
    "name": "write_code_to_directory",
    "description": "This tool writes code to a specified directory.",
    "parameters": {
        "directory": {
            "type": "string",
            "description": "The directory where the code will be written."
        },
        "file_name": {
            "type": "string",
            "description": "The name of the file to be created."
        },
        "code": {
            "type": "string",
            "description": "The code to be written to the file."
        }
    }
}
```


# Function Call Documentation
## Function calling
Similar to the Chat Completions API, the Assistants API supports function calling. Function calling allows you to describe functions to the Assistants and have it intelligently return the functions that need to be called along with their arguments. The Assistants API will pause execution during a Run when it invokes functions, and you can supply the results of the function call back to continue the Run execution.

## Defining functions
First, define your functions when creating an Assistant:

```python
assistant = client.beta.assistants.create(
  instructions="You are a weather bot. Use the provided functions to answer questions.",
  model="gpt-4-1106-preview",
  tools=[{
      "type": "function",
    "function": {
      "name": "getCurrentWeather",
      "description": "Get the weather in location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city and state e.g. San Francisco, CA"},
          "unit": {"type": "string", "enum": ["c", "f"]}
        },
        "required": ["location"]
      }
    }
  }, {
    "type": "function",
    "function": {
      "name": "getNickname",
      "description": "Get the nickname of a city",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city and state e.g. San Francisco, CA"},
        },
        "required": ["location"]
      }
    } 
  }]
)
```

## Reading the functions called by the Assistant
When you initiate a Run with a user Message that triggers the function, the Run will enter a pending status. After it processes, the run will enter a requires_action state which you can verify by retrieving the Run. The model can provide multiple functions to call at once using parallel function calling:

```json
{
  "id": "run_abc123",
  "object": "thread.run",
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "requires_action",
  "required_action": {
    "type": "submit_tool_outputs",
    "submit_tool_outputs": {
      "tool_calls": [
        {
          "id": "call_abc123",
          "type": "function",
          "function": {
            "name": "getCurrentWeather",
            "arguments": "{\"location\":\"San Francisco\"}"
          }
        },
        {
          "id": "call_abc456",
          "type": "function",
          "function": {
            "name": "getNickname",
            "arguments": "{\"location\":\"Los Angeles\"}"
          }
        }
      ]
    }
  },
...
}
```
## Submitting functions outputs
You can then complete the Run by submitting the tool output from the function(s) you call. Pass the tool_call_id referenced in the required_action object above to match output to each function call.

```python
run = client.beta.threads.runs.submit_tool_outputs(
  thread_id=thread.id,
  run_id=run.id,
  tool_outputs=[
      {
        "tool_call_id": call_ids[0],
        "output": "22C",
      },
      {
        "tool_call_id": call_ids[1],
        "output": "LA",
      },
    ]
)
```
After submitting outputs, the run will enter the queued state before it continues it’s execution.