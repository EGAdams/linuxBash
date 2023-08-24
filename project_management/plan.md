
# August 20, 2023

Make Agents one at a time for tasks.


Here are the LangChain components:
# Agents
## Tools
---
# Memory
- How to add memory to an agent - https://docs.langchain.com/docs/components/agents/

- plan and execute - https://python.langchain.com/docs/modules/agents/agent_types/plan_and_execute.html

---  

# Document Loaders

# Text Splitters

# Vector Stores
- The latest python code for this is in the agents/pinecone_dave_s directory.  Looks like the embeddings work for the conversation, but I think the unique ids are storing too much data at a time.  That's one reason why I want to try the tree-sitter methods.

- The LangChain Document Loaders and Text Splitters are not being used in this code.  Dave S. does not use langchain in his example code which we are using.

- We are in the process of embedding a directory code using the tree-sitter repository code.

Next steps:
- We need an example folder full of code that we can use to test the embedding. aug 21 3:32pm
- git cloned cpp tree-sitter code into the tree-sitter directory.

### Summary: Debugging Python Errors

### Issue 1: TypeError with `set_language` Method

**Error:**
TypeError: Argument to set_language must be a Language

**Cause:**  
The `set_language` method was expecting an argument of type `Language`, but a tuple was being provided.

**Solution:**  
Modified the line in the `get_functions` function to pass only the `Language` instance (the first element of the tuple) to the `set_language` method:
From: `parser.set_language(current_language)`
To: `parser.set_language(current_language[0])`

### Issue 2: AttributeError with `node_type` Attribute

**Error:**
AttributeError: 'tree_sitter.TreeCursor' object has no attribute 'node_type'

**Cause:**  
The code was trying to access the `node_type` attribute of a `tree_sitter.TreeCursor` object, which doesn't exist.

**Solution:**  
Modified the line in the `get_functions` function to use the correct attribute to determine the type of node the cursor is currently on:
From: `if cursor.node_type == 'function':`
To: `if cursor.node.type == 'function':`

### Conclusion:
Both issues were successfully identified and resolved, allowing the script to run without errors.

# Update August 21, 2023
The embeddings seem to go in fine now, but the can not be read by the python file that writes the embeddings.  They can be read by the original python script for some reason. 
``` file
chat_with_vector_database.py   
```
This is good news.  We will be able to piece together a tool with this.  do not lose this information.
### 
### 
## Next Steps
### Output Raven's code to a file.  It is to hard to decipher in the terminal.
- How are we supposed to "output code to a file"?
- this is the spinning sand that I always talk about.
We need a FileWriter Agent or an HTMLWriter Agent.
---
### 
---
# Next Steps
---
### 
---
# Build an Agent from the meta stack.  This will be the first agent that we build.  
## will be a Plan and Execute Agent.  It will be able to do the following:
- Plan and Execute something if I ask it to.


### Add a menu item for the Plan and Execute Agent.  Put the Agent into the conversation with vdb.


---
## Operation SnowBall is born.
---
    


# Models

# Prompt


---
## Then there are the ones that I don't understand yet:
# Output Parsers

# Example Selectors

